# 291-virtualisation
Code for the CSE 291-virtualisation project

## File Structure
The code is structured in following folders:

### 1. EC2

- predict.py - contains function to predict the image
- app.py - runs flask server to run inference

### 2. ECS

- predict.py - contains function to predict the image
- app.py - runs flask server to run inference
- Dockerfile - dockerfile to create a docker image of the code

### 3. Sagemaker

- digits/nginx.conf - contains nginx server configuration
- digits/predict.py - contains function to predict the image
- digits/wsgi.py - contains gunicorn configurations
- digits_model_training.ipynb - Jupyter notebook to train the digits classification model
- Dockerfile - dockerfile to create a docker image of the code
- build_push.sh - code to push the docker image to ECR

### 4. client_request_script.py

Contains code to send multiple parallel request to a given public url of the server and print latency. Used to test the service performance.