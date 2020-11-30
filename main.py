from flask import Flask, render_template, logging, request, send_from_directory
from src.predictions import predictionClass

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='images/favicon.ico')

@app.route('/getPredictions', methods=['POST'])
def getPredictions():
    # Call your methods here and return other template
    data = request.form

    p_cost = data.get('p_cost')
    loan = data.get('loan')
    l_interest = data.get('l_interest')
    years = data.get('years')
    rent = data.get('rent')
    savings = data.get('savings')
    s_interest = data.get('s_interest')
    houseType = data.get('houseType')
    
    predClass = predictionClass()
    predictions = predClass.getPredictions(p_cost,loan,l_interest,years,rent,savings,s_interest,houseType)
    result = predictions[0]

    data = {
        "status" : True,
        "result" : str(result)
    }
    return data

if __name__ == "__main__":
    app.run(debug = True)