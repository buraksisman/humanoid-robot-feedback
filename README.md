# HumanoidRobotFeedback
This project aims to provide socket communication between the humanoid robot and the web application.

To start server;
gunicorn --bind next-lab-test.bms.utwente.nl:8080 -k eventlet --reload --threads 50 app:app
and then;
python3 chatServer.py 130.89.6.69 8082
