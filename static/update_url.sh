#/bin/sh
# lambda_url env variable that will be replaced in all js files
# lambda_temp env variable that express template to be replaced in files


lambda_url=$(echo $lambda_url | sed -e 's/\//\\\//g')
[ -z $lambda_temp ] && lambda_temp="__LAMBDA_URL__"
lambda_temp=$(echo $lambda_temp | sed -e 's/\//\\\//g')
name=$(basename $1)
sed -e "s/$lambda_temp/$lambda_url/g" "$1" > "/tmp/$name" && mv /tmp/$name "$1"

