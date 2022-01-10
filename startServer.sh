#!/usr/bin/env bash
gunicorn --bind next-lab-test.bms.utwente.nl:8080 -k eventlet --reload --threads 50 app:app &
python3 chatServer.py 130.89.6.69 8082 &
python3 serverforRobot.py &

