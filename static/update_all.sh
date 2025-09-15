#!/bin/sh


find . -type f -iname '*.js' -exec ./update_url.sh {}\;

