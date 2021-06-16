from flask import Flask, request, render_template
from model_pred import ModelPred

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    alloy_name = request.form['alloy_name']
    model = ModelPred()
    prediction = model.predict(alloy_name)

    return render_template('index.html', tx1=alloy_name, tx2=prediction)

if __name__ == "__main__":
    app.run(debug=True)