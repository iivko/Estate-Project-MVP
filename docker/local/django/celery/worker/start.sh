#! /bin/bash

sed -o errexit
sed -o nounset

exec watchfiles --filter python celery.__main__.main --args '-A config.celery_app worker -l INFO'
