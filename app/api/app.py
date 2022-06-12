from distutils.log import debug
from flask import Flask, jsonify, request
from utilities import predict_pipeline

app = Flask(__name__)

@app.post('/predict')
def predict():
    data = request.json
    try:
        sample = data['text']
    except KeyError as e:
        return jsonify({'error': f'No text sent => {e}'})
    
    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        return jsonify({'error': str(e)})
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)