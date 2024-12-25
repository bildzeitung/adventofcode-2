#!/bin/bash -ex

python -m venv venv
. ./venv/bin/activate \
    && pip install -U uv \
    && uv pip install wheel \
    && uv pip install \
        -r requirements.txt
