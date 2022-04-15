import streamlit as st 
import numpy as np
import pandas as pd
import random
import pickle

def get_classifier(clf_name,jobid,all_about_job):
    clf = None
    if clf_name == 'SVC':
        st.write('SVC Accuracy: 0.98')
        with open('C:\\Users\\ergou\\Documents\\pipe_svc.pkl', 'rb') as pickle_in_svc:
            pipe_svc = pickle.load(pickle_in_svc)
        predicted_svc = pipe_svc.predict([[jobid,all_about_job]])
        st.success('The output is {}'.format(predicted_svc))
        st.write('svc Accuracy: 0.98') 
        return predicted_svc
    elif clf_name == 'LogisticRegression':
        st.write('lr Accuracy: 0.98')  
        with open('C:\\Users\\ergou\\Documents\\pipe_lr.pkl', 'rb') as pickle_in_lr:
            pipe_lr = pickle.load(pickle_in_lr)
        predicted_lr = pipe_lr.predict([[jobid,all_about_job]])
        st.success('The output is {}'.format(predicted_lr))
        st.write('lr Accuracy: 0.98') 
        return predicted_lr  
    else:
        with open('C:\\Users\\ergou\\Documents\\pipe_rf.pkl', 'rb') as pickle_in_rf:
            pipe_rf = pickle.load(pickle_in_rf)
        predicted_rf = pipe_rf.predict([[jobid,all_about_job]])
        st.success('The output is {}'.format(predicted_rf))
        st.write('SVC Accuracy: 0.98')
        return predicted_rf

# clf = get_classifier(classifier_name)

def main():
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
    


if __name__=='__main__':
	main()

