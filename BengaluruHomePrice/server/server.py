from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/getlocation', methods= ['GET'])
def get_location_names():
    response = jsonify({'locations': util.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/predictprice', methods = ['POST'])
def predict_prce():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({'estimated_price': util.get_estimated_price(location, bhk, bath, total_sqft)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == '__main__':
    print('Starting python flask server')
    util.load_saved_artifacts()
    app.run(debug=True)
