%%writefile app.py
import streamlit as st 
import numpy as np
import pandas as pd
import random
import pickle
from pathlib import Path

filename1 = Path("/content/trained_lr_model.sav")
filename2 = Path("/content/trained_model.sav")
filename3 = Path("/content/trained_rf_model.sav")
loaded_model = pickle.load(open(filename1, 'rb'))
loaded_lr_model = pickle.load(open(filename2, 'rb'))
loaded_rf_model = pickle.load(open(filename3, 'rb'))

# prediction = loaded_model.predict(X_test[[1]])
# print(prediction)

def get_classifier(clf_name,jobid,all_about_job):
    clf = None
    if clf_name == 'SVC':
        st.write('SVC Accuracy: 0.98')
        predicted_svc = loaded_model.predict([[jobid,all_about_job]])
        print(predicted_svc)
        return predicted_svc
    elif clf_name == 'LogisticRegression':
        st.write('lr Accuracy: 0.98')  
        predicted_lr = loaded_model.predict([[jobid,all_about_job]])
        print(predicted_lr)
        return predicted_lr  
    else:
        prediction_rf = loaded_model.predict([[jobid,all_about_job]])
        print(prediction_rf)
        st.write('SVC Accuracy: 0.98')
        return prediction_rf


if __name__=='__main__':
    st.title("hello streamlit")
    st.write("""#explore diff clasifier
    which one is best""")
    classifier_name = st.sidebar.selectbox("select classifier",(" LogisticRegression"," RandomForestClassifier"," SVC"))
    
    # this is usefuull for manything
    jobid = st.text_input(" job", "Type Here")
    all_about_job = st.text_input("proper description of job", "Type Here")
    if st.button("Predict"):
        predicted = get_classifier(classifier_name,jobid,all_about_job)
        st.success('The output is {}'.format(predicted))

