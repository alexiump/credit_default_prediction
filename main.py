# -*- coding: utf-8 -*-
"""
Created on Mon May  1 10:52:57 2023

@author: USER
"""

import pandas as pd
import joblib
import sklearn.linear_model as lr
import streamlit as st





def main():
    st.title("Credit Defaulter")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Right Fuel Card Credit Default Authenticator ML App </h2>
    </div>
    """
    
    model = lr.LogisticRegression()
    model = joblib.load('model_joblib_defaulters')
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
         
    s1 = st.selectbox("What is the Legal Status of the Company?", ('Limited', 'Partnership', 'Sole trader') )
    
    if s1 == "Limited":
        p1=0
    elif s1 == "Partnership":
        p1=1
    elif s1 == "Sole trader":
        p1=2
    
    p2 = st.number_input("What is the Amount of the Customer Debt?")
    
    p3 = st.number_input("What is the Credit of the Customer?")
    
    p4 = st.number_input("What is the Balance of the Customer?")
    
    p5 = st.number_input("What is the Credit Score of the Customer?")
    
    p6 = st.number_input("How long has the custimer own this card (in years)?",0,15,step=1)
    
    p7 = st.number_input("What is the frequency of this customer Transaction?")
    
    p8 = st.number_input("What is the Address Frequency of this customer?",1,5,step=1)
    
    p9 = st.number_input("What is the Age of this customer business?")
    
    s2 = st.selectbox("What is the Transaction Behaviour of this customer?", ('Stable', 'Low Risk', 'Very High Risk', 'High Risk') )
    
    if s2 == "Stable":
        p10=0
    elif s2 == "Low Risk":
        p10=1
    elif s2 == "High Risk":
        p10=2
    elif s2 == "Very High Risk":
        p10=3
        
    p11 = st.number_input("What is the customer credit utilisation?")
    
    p12 = st.number_input("What is the total of the customer Transaction?")
    
    
    new_data = pd.DataFrame({
    'Status':p1,
    'Debt':p2,
    'Limit':p3,
    'Balance':p4,
    'Score':p5,
    'Card_Length':p6,
    'Number_Transaction':p7,
    'Address_Frequency':p8,
    'Company_Age':p9,
    'Transaction_Behaviour':p10,
    'Credit_Utilisation':p11,
    'Amount':p12,
},index=[0])
    
    
    if st.button('Predict'):
        pred = model.predict(new_data)
        #st.success('This customer has high likelyhood of defaulting {}'.format(pred))
        if pred[0]==0:
                st.success('This customer is a non defaulter')
        else:
            st.success("This is a defaulter")
       
    

if __name__=='__main__':
    main()