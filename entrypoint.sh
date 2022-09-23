#!/bin/bash

wait_for () {
    for _ in `seq 0 100`; do
        (echo > /dev/tcp/$1/$2) >/dev/null 2>&1
        if [[ $? -eq 0 ]]; then
            echo "$1:$2 accepts connections"
            break
        fi
        sleep 1
    done
}

case "$PROCESS" in
"DEV_DJANGO")
    wait_for "${POSTGRES_HOST}" "${POSTGRES_PORT}"
    python manage.py makemigrations &&
    python manage.py migrate &&
    uvicorn config.asgi:application --reload-dir apps --debug --host 0.0.0.0 --port 8080 --log-level info --use-colors
    ;;
"DJANGO")
    wait_for "${POSTGRES_HOST}" "${POSTGRES_PORT}"
    python manage.py makemigrations &&
    python manage.py migrate &&
    gunicorn --config gunicorn.conf.py config.wsgi:application --reload --capture-output --log-level info --access-logfile -
    ;;
"DEV_CELERY_WORKER")
    wait_for "${CELERY_BROKER_HOST}" "${CELERY_BROKER_PORT}"
    python manage.py celery_worker
    ;;
"CELERY_WORKER")
    wait_for "${CELERY_BROKER_HOST}" "${CELERY_BROKER_PORT}"
    echo 'vm.overcommit_memory = 1' >> /etc/sysctl.conf
    case "$NODE" in
    "SCHEDULER")
        celery -A apps.taskapp beat --loglevel=INFO
        ;;
    "CONSUMER")
        celery -A apps.taskapp worker --loglevel=INFO \
        --concurrency=3 --max-tasks-per-child=2048
        ;;
    *)
        echo "NO NODE SPECIFIED!"
        exit 1
        ;;
    esac
    ;;
esac
