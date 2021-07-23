# A simple Machine Learning Prediction Application 
This project will demonstrate how a pickled machine learning algorithm can be used by a web application to perform prediction. The chosen dataset in this project is Iris dataset.

### Flask
A web framework written in Python

<br />

How to run this app
```
% cd <project directory>
% source env/bin/activate

% export FLASK_APP=sample
% export FLASK_ENV=development
% flask run
```

Enter 127.0.0.1:5000 in your browser tab and you will see the web app

<br />

How to quit this app
```
% ctrl + c
% deactivate 
```

## Output
#### Single instance
Make prediction on a single instance. Enter all required info and hit on the *single* button. The predicted class along with the confidence score will then be returned.

<br />

![Sample Output I](https://github.com/Sins-Repo/ML-Prediction-App/blob/master/static/single-prediction.png?raw=true)

<br />
<br />

#### Batch prediction
Make prediction by batch. Simply upload your csv file (with or without index will do) and hit on the *Predict* button. The predicted class along with the confidence score will then be returned and displayed in the table.

<br />

![Sample Output I](https://github.com/Sins-Repo/ML-Prediction-App/blob/master/static/batch-prediction.png?raw=true)
