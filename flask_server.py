from flask import Flask, request, Response
import jsonpickle
import json
import numpy as np
import cv2

# Initialize the Flask application
app = Flask(__name__)

@app.route('/api/test', methods=['POST'])
def test():
    nparr = np.frombuffer(request.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}
    return Response(response=json.dumps(response), status=200, mimetype="application/json")

app.run(host="0.0.0.0", port=5000)
