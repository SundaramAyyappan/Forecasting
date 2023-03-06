# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:45:13 2023

@author: Jeevika
"""

import numpy as np
import pickle
import pandas as pd

import streamlit as st 


from PIL import Image

pickle_in = open("Forecasting.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def forecasting(Date):
    
    prediction=classifier.predict([[Date]])
    print(prediction)
    

def main():
    
    st.title('Forecasting Web App')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Forecasting Prediction App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    Date = st.number_input('How many days forecast do you want?',min_value = 1, max_value = 365)
    
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result

    if st.button("Predict"):
        result = forecasting(Date)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()
