#!/usr/bin/env bash
echo "base.in"
pip-compile requirements/base.in "$@"

echo "code_quality.in"
pip-compile requirements/code_quality.in "$@"

echo "deploy.in"
pip-compile requirements/deploy.in "$@"

echo "dev.in"
pip-compile requirements/dev.in "$@"

echo "docs.in"
pip-compile requirements/docs.in "$@"

echo "documentation.in"
pip-compile requirements/documentation.in "$@"

echo "test.in"
pip-compile requirements/test.in "$@"

echo "testing.in"
pip-compile requirements/testing.in "$@"
