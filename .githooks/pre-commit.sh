#!/usr/bin/env bash

echo "pre-commit template by github.com/NobinKhan"
set -eux ;\
    poetry run pre-commit run -a ;\
    poetry run ruff check ;