# flask, skikit-learn, pandas, pickle-mixin


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():

    locations = sorted(data['location'].unique())
    return render_template("index.html", locations= locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk= request.form.get('bhk')
    bath = request.form.get('bath')
    sqft=request.form.get('total_sqft')

    print|(locaton, bhk, bath. sqft)
    input= pd.DataFrame([[lacation,sqft,bath,bhk]],columns=["location", 'total_sqft', 'bath', 'bhk'])
    prediction= pipe.predict(input)[0]



    return str(prediction)


if __name__== "__main__":
    app.run(debug=True, port=5001)