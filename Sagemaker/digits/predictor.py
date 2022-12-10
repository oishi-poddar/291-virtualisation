# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:32:40 2019

@author: naresh.gangiredd
"""

import os
import json
from sklearn.externals import joblib
import flask
import boto3
import time
import pyarrow
from pyarrow import feather
#from boto3.s3.connection import S3Connection
#from botocore.exceptions import ClientError
#import pickle
import modin.pandas as pd
import io

import logging

#Define the path
prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')
logging.info("Model Path" + str(model_path))

# Load the model components
regressor = joblib.load(os.path.join(model_path, 'digits.pkl'))
logging.info("Digits Classifier " + str(regressor))

# The flask app for serving predictions
app = flask.Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    # Check if the classifier was loaded correctly
    try:
        status = 200
        logging.info("Status : 200")
    except:
        status = 400
    return flask.Response(response= json.dumps(' '), status=status, mimetype='application/json' )

@app.route('/invocations', methods=['POST'])
def transformation(X_test):
    start = time.time()

    runtime_client = boto3.client("runtime.sagemaker")
    endpoint_name = "MNIST_MODEL"
    X_test_record = X_test[:1]
    csv_file = io.StringIO()
    X_test_record.to_csv(csv_file, sep=",", header=False, index=False)
    payload = csv_file.getvalue()
    response = runtime_client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType="text/csv", Body=payload
    )

    print("Results :\n")

    result = response["Body"].read().decode("ascii")

    # Unpack response
    print("\nPredicted Class Probabilities: {}.".format(result))

    total_time = (time.time()-start)
    result = {
        'output': total_time
    }
    resultjson = json.dumps(result)
    return flask.Response(response=resultjson, status=200, mimetype='application/json')