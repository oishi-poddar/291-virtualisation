from flask import Flask
import predict
import os

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/predict')
def predict_matrix():
    return predict.classify()  

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 3000))
  app.run(host="0.0.0.0", port=port)