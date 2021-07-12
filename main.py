import os
import csv
import numpy
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

model = pickle.load(open('algo.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("homepage.html")
    if request.method == 'POST':
        return """
            <h1>hello world</h1>
        """

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
            header = ['Sepal Length', 'Sepal Width','Petal Length', 'Petal Width', 'Target']

            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename)) as file:
                csvfile = csv.DictReader(file)
                for row in csvfile:
                    data.append(dict(Sepal_Length = row['Sepal Length'], Sepal_Width = row['Sepal Width'], 
                                    Petal_Length = row['Petal Length'], Petal_Width = row['Petal Width'], target = row['target']))
            return render_template("table.html", data=data, header=header)
        return render_template("table.html")

if __name__ == "__main__":
    app.run(debug=True)