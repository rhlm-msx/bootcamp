#!/bin/sh

sum=$(find app -type f -exec md5sum {} \; | sort -k 2 | md5sum - Dockerfile | md5sum - | cut -d' ' -f1)
remote=$(aws ssm get-parameter --name docker_image_hash --query Parameter.Value --output text || echo None)


function del {
	aws ssm delete-parameter --name docker_image_hash
}

function not_changed {
	echo Docker Image Already Updated..
}

function changed {
	echo Updating Docker Image...
	aws ssm put-parameter --name docker_image_hash --value $sum --overwrite --type "String"
	remote=$sum
	docker built -t lambda_docker:$sum
	docker tag lambda_docker:$sum $ECR_URL:$sum
	docker tag lambda_docker:$sum $ECR_URL:latest

	docker push $ECR_URL:$sum
	docker push $ECR_URL:latest
}



case "$1" in
 destroy)
	 echo "Deleting the docker checksum"
	 del
	 ;;
   *)
	echo "Checking Docker Checksum"
	[ $sum != $remote ] && changed || not_changed;
    ;;

esac
