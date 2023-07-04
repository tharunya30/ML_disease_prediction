# -*- coding: utf-8 -*-
"""
Created on Mon Jul 3 15:07:42 2023
@author: Dell
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

#page name and icon
st.set_page_config(page_title='Disease Prediction', page_icon='🩺')

# loading the saved models
diabetes_loaded_model = pickle.load(open('C:/Users/Dell/OneDrive/Documents/ML webapp/diabetes_model.sav','rb'))

breastcancer_loaded_model = pickle.load(open('C:/Users/Dell/OneDrive/Documents/ML webapp/trained_model_BC.sav','rb'))

parkinsons_loaded_model = pickle.load(open('C:/Users/Dell/OneDrive/Documents/ML webapp/trained_model_PD.sav','rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('DISEASE PREDICTION SYSTEM ',
                           ['Home','Diabetes Prediction','Parkinson Disease Prediction','Breast Cancer Prediction'],
                           icons=['house','thermometer-low', 'person','heart-pulse'],
                           default_index=0)
#home page
if (selected == 'Home'):
    st.title("Welcome to the Disease Prediction App")
    st.subheader("This application allows you to determine the likelihood of illness by making predictions.")
    st.markdown("<h1 style='text-align: center; color: red;'>Please select a disease prediction category from the sidebar.</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: 16F0A1;'>STAY HEALTHY</h1>", unsafe_allow_html=True)
    
    image=Image.open("C:/Users/Dell/OneDrive/Documents/ML webapp/img.jpg")
    st.image(image,caption='',output_format="auto")
    
     
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    st.subheader('Fill in the appropriate diagnosed values and press the predict button.')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_loaded_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)   
    
#Parkinson prediction page    
if (selected=='Parkinson Disease Prediction'):
    st.title('Parkinson Disease Prediction using ML')
    st.subheader('Fill in the appropriate diagnosed values and press the predict button.')
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        PD_prediction = parkinsons_loaded_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                  Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR,
                                                  RPDE, DFA, spread1, spread2, D2, PPE]])

        if PD_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
#breast cancer prediction page

if (selected == 'Breast Cancer Prediction'):
    # page title
    st.title('Breast Cancer Prediction using ML')
    st.subheader('Fill in the appropriate diagnosed values and press the predict button.')
    col1, col2, col3, col4, col5, col6= st.columns(6)

    with col1:
        radius_mean = st.text_input('Mean radius of tumor')
        concavity_mean = st.text_input('Mean concavity of tumor')
        perimeter_se = st.text_input('Standard error of perimeter')
        symmetry_se = st.text_input('Standard symmetry')
        smoothness_worst = st.text_input('worseness of smoothnes')
        
    with col2:
        texture_mean = st.text_input('Mean value of texture')
        concave_points_mean = st.text_input('Mean concave points of tumor')
        area_se = st.text_input('Standard error of area')
        fractal_dimension_se = st.text_input('Standard fractional dimension')
        compactness_worst = st.text_input('worseness of compactness')

    with col3:
        perimeter_mean = st.text_input('Mean perimeter of tumor')
        symmetry_mean = st.text_input('Mean symmetry of tumor')
        smoothness_se = st.text_input('Standard error of smoothness')
        radius_worst = st.text_input('worseness of radius')
        concavity_worst = st.text_input('worseness of concavity')
          
    with  col4:
        area_mean = st.text_input('Mean area of tumor')
        fractal_dimension_mean = st.text_input('Mean fractal dimension of tumor')
        compactness_se = st.text_input('Standard error of compactness')
        texture_worst = st.text_input('worseness of texture')
        concave_points_worst = st.text_input('worseness of concave points')
          
    with col5:
        smoothness_mean = st.text_input('Mean smoothness of tumor')
        radius_se = st.text_input('Standard error of radius')
        concavity_se = st.text_input('Standard error of concavity')
        perimeter_worst = st.text_input('worseness of perimeter')
        symmetry_worst = st.text_input('worseness of symmetry')
        
    with col6:
        compactness_mean = st.text_input('Mean compactness of tumor')
        texture_se = st.text_input('Standard error of texture')
        concave_points_se = st.text_input('Standard error of concave points')
        area_worst = st.text_input('worseness of area')
        fractional_worst = st.text_input('worseness of fractional')
        
        
        #code for prediction
        breast_cancer_diagnosis = ''

        # creating a button for Prediction
        if st.button('Breast Cancer Test Result'):
            BS_prediction = breastcancer_loaded_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean,
                                                      smoothness_mean, compactness_mean, concavity_mean,
                                                      concave_points_mean, symmetry_mean,
                                                      fractal_dimension_mean, radius_se, texture_se,
                                                      perimeter_se, area_se, smoothness_se, compactness_se,
                                                      concavity_se, concave_points_se]])

            if BS_prediction[0] == 1:
                breast_cancer_diagnosis = 'The Breast cancer is Malignant'
            else:
                breast_cancer_diagnosis = 'The Breast Cancer is Benign'

        st.success(breast_cancer_diagnosis)