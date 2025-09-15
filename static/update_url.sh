#/bin/sh
lambda_url=$(echo $lambda_url | sed -e 's/\//\\\//g')
sed -e "s/__LAMBDA_URL__/$lambda_url/g" "$1"

