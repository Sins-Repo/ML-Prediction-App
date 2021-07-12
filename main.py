import os
import csv
import numpy as np
import pickle
import sklearn 
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Store the uploaded files into the file system (localhost)
UPLOAD_FOLDER = './uploaded/'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# To prevent injection attack
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load the pickled machine learning algorithm
model = pickle.load(open('algo.pkl', 'rb'))

# Class name of the dataset
class_name = {
    0 : "Setosa",
    1 : "Versicolor",
    2 : "Virginica"
}

# Helper function for pickled algorithm
def prediction(attr1, attr2, attr3, attr4):
    data = np.array([[attr1, attr2, attr3, attr4]])
    pred = model.predict(data)
    score = model.predict_proba(data)[0][pred[0]] * 100
    return pred, score

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("homepage.html")
    if request.method == 'POST':
        attr1 = request.form['Sepal_Length']
        attr2 = request.form['Sepal_Width']
        attr3 = request.form['Petal_Length']
        attr4 = request.form['Petal_Width']

        pred, score = prediction(attr1, attr2, attr3, attr4)
        return render_template("homepage.html", pred=class_name[pred[0]], score=score)

@app.route('/predict_by_batch', methods=['GET', 'POST'])
def table():
    if request.method == 'GET':
        return render_template("table.html")
    if request.method == 'POST':
        file = request.files['csvfile']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            data = []
            header = ['Sepal Length', 'Sepal Width','Petal Length', 'Petal Width', 'Class', 'Score']

            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename)) as file:
                csvfile = csv.DictReader(file)
                for row in csvfile:
                    pred, score = prediction(row['Sepal Length'], row['Sepal Width'], row['Petal Length'], row['Petal Width'])
                    data.append(dict(Sepal_Length = row['Sepal Length'], Sepal_Width = row['Sepal Width'], 
                                    Petal_Length = row['Petal Length'], Petal_Width = row['Petal Width'], Class = class_name[pred[0]], Score = score ))
            return render_template("table.html", data=data, header=header)
        return render_template("table.html")

if __name__ == "__main__":
    app.run(debug=True)