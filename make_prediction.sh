#!/usr/bin/env bash

PORT=5000
echo "Port: $PORT"

# POST method predict
curl -d '{
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
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict
