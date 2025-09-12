#! /bin/bash

sed -o errexit
sed -o nounset

rm -f './celerybeat.pid'

exec watchfiles --filter python celery.__main__.main --args '-A config.celery_app beat -l INFO'
