
"""

Recognizing hand-written digits

"""

import sklearn
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import time
import boto3
import io
from io import StringIO

# Inference on digits dataset


def classify(X_test):
    start = time.time()

    runtime_client = boto3.client("runtime.sagemaker")
    endpoint_name = "MNIST_MODEL"
    # converting X_test which is a dataframe to csv to invoke endpoint
    X_test_record = X_test[:1]
    csv_file = io.StringIO()
    # by default sagemaker expects comma seperated
    X_test_record.to_csv(csv_file, sep=",", header=False, index=False)
    payload = csv_file.getvalue()
    response = runtime_client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType="text/csv", Body=payload
    )

    print("Results :\n")

    result = response["Body"].read().decode("ascii")

    # Unpack response
    print("\nPredicted Class Probabilities: {}.".format(result))

    print(time.time()-start)
    return str(time.time()-start)
