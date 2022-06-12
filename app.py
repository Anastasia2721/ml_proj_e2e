from flask import Flask, request, jsonify
import joblib
import numpy

MODEL_PATH = 'model/model.pkl'
SCALER_X_PATH = 'model/scaler_x.pkl'
SCALER_Y_PATH = 'model/scaler_y.pkl'

app = Flask(__name__)
model = joblib.load(MODEL_PATH)
sc_x = joblib.load(SCALER_X_PATH)
sc_y = joblib.load(SCALER_Y_PATH)


@app.route('/')
def hello_world():
    return 'POST /api/predict'


# JSON for prediction:
# {
#   "open_plan": 1,
#   "rooms": 1,
#   "area": 2.2,
#   "renovation": 1
# }
@app.route('/api/predict', methods=['POST'])
def predict():
    content = request.json
    app.logger.info('request: %s ', content)

    open_plan = content['open_plan']
    rooms = content['rooms']
    area = content['area']
    renovation = content['renovation']

    x = numpy.array([open_plan, rooms, area, renovation]).reshape(1, -1)
    x = sc_x.transform(x)
    result = model.predict(x)
    result = sc_y.inverse_transform(result.reshape(1, -1))
    price = {'price': result[0][0]}
    app.logger.info('predicted price: %s ', price)

    return jsonify(price)


if __name__ == '__main__':
    app.run(debug=True)
