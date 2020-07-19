#!/bin/sh
# install-requirements.sh

set -e

MODE="$1"

if [ "x$MODE" = "xprod" ]; then
    echo "Installing PRODUCTION dependencies" &&
        pip install -r /user/requirements/prod.txt &&
        rm -rf /root/.cache/pip/*
elif [ "x$MODE" = "xstage" ]; then
    echo "Installing STAGE dependencies" &&
        pip install -r /user/requirements/stage.txt &&
        rm -rf /root/.cache/pip/*
else
    echo "Installing DEVELOPMENT dependencies" &&
        pip install -r /user/requirements/dev.txt &&
        rm -rf /root/.cache/pip/*
fi
