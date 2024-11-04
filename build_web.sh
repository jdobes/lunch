#!/bin/bash

set -e

tmpdir="/tmp/"
dockerfile="Dockerfile-web-builder"

for runtime in podman docker; do
    cmd=$(command -v $runtime)
    if [[ "$cmd" != "" ]] && $cmd ps &> /dev/null; then
        if [[ "$runtime" == "docker" ]]; then
            change_owner_docker="chown -R $(id -u):$(id -g) ./build/"
        else
            change_owner_docker="true"
        fi
        break
    else
        echo "Unable to use $runtime"
        cmd=""
    fi
done

if [[ "$cmd" != "" ]]; then
    echo "Using: $cmd"
else
    echo "No container runtime found!"
    exit 1
fi

rm -rf ./web/build/

cat <<EOF > $tmpdir$dockerfile
FROM registry.access.redhat.com/ubi8/ubi-minimal

RUN microdnf module enable nodejs:20 && \
    microdnf install npm python2 make gcc-c++

ADD web/*.json  /web-build/
ADD web/public/ /web-build/public/
ADD web/src/    /web-build/src/

WORKDIR /web-build

CMD ["/bin/sh", "-c", "npm ci && npm run build && $change_owner_docker"]
EOF

$cmd build -t lunch-web-builder -f $tmpdir$dockerfile .
mkdir -p ./web/build
$cmd run --rm -v ./web/build/:/web-build/build/:Z --name lunch-web-builder lunch-web-builder

$cmd rmi -f lunch-web-builder
rm $tmpdir$dockerfile
