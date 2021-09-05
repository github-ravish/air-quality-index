#!/bin/sh

set -e

celery -A app worker -l DEBUG

celery -A app beat -l DEBUG --scheduler django_celery_beat.schedulers:DatabaseScheduler
