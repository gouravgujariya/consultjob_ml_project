import numpy as np
import streamlit as st
import joblib
# filename = 'finalized_model.sav'
# loaded_model = joblib.load(filename)


def main():
    # giving a title
    st.title('job fraud detection')

    # getting the input data from the user
    # input_data = (
    # 'job_id', 'title', 'location', 'department', 'salary_range', 'company_profile', 'description', 'requirements',
    # 'benefits', 'telecommuting', 'has_company_logo', 'has_questions', 'employment_type', 'required_experience',
    # 'required_education', 'industry', 'function', 'fraudulent')

    job_id = st.text_input('Number of job id')
    title = st.text_input('title of job')
    location = st.text_input('location of job')
    department = st.text_input('department of job')
    salary_range = st.text_input('salary range of job')
    company_profile = st.text_input('company profile')
    description = st.text_input('description')
    requirements = st.text_input('requirements for job')
    benefits = st.text_input('benefits')
    telecommuting = st.text_input('telecommuting')
    has_company_logo= st.text_input('do company have a logo 0,1')
    has_questions = st.text_input('has questions 0,1')
    employment_type = st.text_input('employment type eg internship..')
    required_experience = st.text_input('required experience 0,1')
    required_education = st.text_input('required education level')
    industry = st.text_input('industry')
    function = st.text_input('function')

    # code for Prediction
    job = ''

    # creating a button for Prediction

    if st.button('prediction results are:'):
        job = job_pri(
            ['job_id', 'title', 'location', 'department', 'salary_range', 'company_profile', 'description', 'requirements',
    'benefits', 'telecommuting', 'has_company_logo', 'has_questions', 'employment_type', 'required_experience',
    'required_education', 'industry', 'function'])

    st.success(job)

# filename = 'C:/Users/ergou/Documents/PythonScripts/consultjob1_1/finalized_model.sav'
# loaded_model = joblib.load(filename)

def job_pri(input_data):
    input_data_as_array = np.asarray(input_data)

    prediction = loaded_model.predict(input_data_as_array)
    print(prediction)
    if (prediction[0] == 0):
      return 'job is not fraud'
    else:
      return 'job is fraud'

if __name__ == '__main__':
    filename = 'C:/Users/ergou/Documents/PythonScripts/consultjob1_1/rf_trained_model.sav'
    loaded_model = joblib.load(filename)
    main()
