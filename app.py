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
def root_method():
    return 'GET and POST /api/predict'


# JSON for prediction:
# {
#   "open_plan": 1,
#   "rooms": 1,
#   "area": 2.2,
#   "renovation": 1
# }
@app.route('/api/predict', methods=['POST'])
def predict_post():
    content = request.json
    app.logger.info('request: %s ', content)
    open_plan = content['open_plan']
    rooms = content['rooms']
    area = content['area']
    renovation = content['renovation']
    return predict(open_plan, rooms, area, renovation)


# GET http://localhost:5000?open_plan=1&rooms=4&area=1000.53&renovation=1
@app.route('/api/predict', methods=['GET'])
def predict_get():
    args = request.args
    app.logger.info('request: %s ', args)
    open_plan = args.get('open_plan', default=-1, type=int)
    rooms = args.get('rooms', default=-1, type=int)
    area = args.get('area', default=-1, type=float)
    renovation = args.get('renovation', default=-1, type=int)
    return predict(open_plan, rooms, area, renovation)


def predict(open_plan, rooms, area, renovation):
    x = numpy.array([open_plan, rooms, area, renovation]).reshape(1, -1)
    x = sc_x.transform(x)
    result = model.predict(x)
    result = sc_y.inverse_transform(result.reshape(1, -1))
    price = {'price': result[0][0]}
    app.logger.info('predicted price: %s ', price)

    return jsonify(price)


if __name__ == '__main__':
    app.run(debug=True)
