#!/bin/bash
# Enable strict mode for safer Bash scripts


# Tells the script to exit immediately if a command exits with a non-zero status
set -o errexit

# The pipeline’s exit status is the last non-zero exit code in the pipeline.
set -o pipefail

# Treat unset variables as an error when substituting.
# Useful for catching missing environment variables (e.g., from .env).    Thank you ChatGPT!!!
set -o nounset

# This script checks if the PostgresSQL database is available before starting the Django application.
python << END
import sys
import time
import psycopg2

suggest_unrecovarable_after = 30
start = time.time()

while True:
  try:

    # Tries to connect to the PostgresSQL database container
    psycopg2.connect(
      dbname="${POSTGRES_DB}",
      user="${POSTGRES_USER}",
      password="${POSTGRES_PASSWORD}",
      host="${POSTGRES_HOST}",
      port="${POSTGRES_PORT}"
    )
    break

  except psycopg2.OperationalError as error:
    sys.stderr.write("Waiting for PostgresSQL to become available...\n")

    # if it can't connect to the database after 30 seconds, it will exit.    And make my life much simpler.
    if time.time() - start > suggest_unrecovarable_after:
      sys.stderr.write("This is taking longer than expected.\n The following exception appears: '{}'\n".format(error))

      time.sleep(1)
END


>&2 echo "PostgresSQL is available."

exec "$@"