#!/bin/sh


find . -type f -iname '*.js' -exec sh -c "./update_url.sh {}" \;

