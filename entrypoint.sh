#!/bin/sh

cd $(dirname $0)

if [[ ! -z $1 ]]; then
    if [[ "$1" == "api" ]]; then
        exec python3 -m lunch.lunch
    elif [[ "$1" == "web" ]]; then
        exec nginx -g 'daemon off;'
    fi
fi

echo "Please specify service name as the first argument."
