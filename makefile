ECR_URL=$(shell cd infra3 && terraform output -raw ecr_url)


container:
	docker build -t lambda_docker:latest .
	docker tag lambda_docker:latest $(ECR_URL):latest
	docker push $(ECR_URL):latest

infra:
	find app -type f -exec md5sum {} \; | sort -k 2 | md5sum - > sum
	cd infra; terraform init; terraform apply --auto-approve

login:
	aws ecr get-login-password | docker login --username AWS --password-stdin $(ECR_URL)

