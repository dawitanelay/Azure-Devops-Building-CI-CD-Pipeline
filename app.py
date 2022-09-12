from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Scales Payload"""

    LOG.info("Scaling Payload: %s payload")
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

# TO DO:  Log out the prediction value!
@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction
    input looks like:
        {
   "CRIM": {
      "0":0.21124
   },
   "ZN":{
      "0":12.5
   },
   "INDUS":{
      "0":7.87
   },
   "CHAS":{
      "0":0
   },
   "NOX":{
      "0":0.524
   },
   "RM":{
      "0":5.631
   },
   "AGE":{
      "0":100.0
   },
   "DIS":{
      "0":6.0821
   },
   "RAD":{
      "0":5.0
   },
   "TAX":{
      "0":311.0
   },
   "PTRATIO":{
      "0":15.2
   },
   "B":{
      "0":386.63
   },
   "LSTAT":{
      "0":29.93
   }
}
    result looks like:
    { "prediction": [ 20.35373177134412 ] }
    """

    try:
        clf = joblib.load("boston_housing_prediction.joblib")
    except:
        LOG.info("JSON payload: %s json_payload")
        return "Model not loaded"

    json_payload = request.json
    LOG.info("JSON payload: %s json_payload")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info("inference payload DataFrame: %s inference_payload")
    scaled_payload = scale(inference_payload)
    prediction = list(clf.predict(scaled_payload))
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
