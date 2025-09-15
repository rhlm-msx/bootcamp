#!/bin/sh

lambda_url=$(echo $lambda_url | sed -e 's/\//\\\//g')
[ -z $lambda_temp ] && lambda_temp="__LAMBDA_URL__"
lambda_temp=$(echo $lambda_temp | sed -e 's/\//\\\//g')
update_url() {

name=$(basename $1)
sed -e "s/$lambda_temp/$lambda_url/g" "$1" > "/tmp/$name" && mv /tmp/$name "$1"

}

for file in $(find . -type f -iname '*.js')
do
	echo [INFO]: Updating $file.
	update_url $file
done

