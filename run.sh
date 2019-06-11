#!/bin/sh

docker run --privileged --rm -it \
    -v $PWD:/hello \
    -v /lib/modules:/lib/modules:ro \
    -v /usr/src:/usr/src:ro \
    -v /sys:/sys:ro \
    --workdir /hello \
    westonsteimel/bcc python hello.py

