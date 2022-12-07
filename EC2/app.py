from flask import Flask
import predict
from sklearn import datasets
from sklearn.model_selection import train_test_split

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/predict')
def inference():
  digits = datasets.load_digits()
  data = digits.images.reshape((n_samples, -1))
  X_train, X_test, y_train, y_test = train_test_split(
        data, digits.target, test_size=0.9, shuffle=False
    )
	return predict.classify(X_test)

if __name__ == "__main__":
	app.run(debug=True)
