import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
"""
### World Health Organization has estimated 12 million deaths occur worldwide, every year due to Heart diseases. Half the deaths in the United States and other developed countries are due to cardio vascular diseases. The early prognosis of cardiovascular diseases can aid in making decisions on lifestyle changes in high risk patients and in turn reduce the complications.
"""
st.write("")
'''
### Let's take a quick information about you and let's find out about your 10 year Coronary Heart Disease risk.
'''
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

inputs = [None]*11
male,age,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,glucos = inputs

status = st.radio("Select Gender: ", ('Male', 'Female'))
if (status == 'Male'):
    male = 1
else:
    male = 0

age = st.slider("Enter your Age", 1, 120)
# st.text('Selected: {}'.format(age))

cigsPerDay = st.number_input("How many Cigs you use per day (put decimal value if you use half a day)?",min_value=0.0,
    max_value=30.0,step=1.0,format="%.2f")
# st.text('Selected: {}'.format(Cigs))

status = st.radio("Are you using blood pressure medication?: ", ('YES', 'NO'))
if (status == 'YES'):
    BPMeds = 1
else:
    BPMeds = 0

status = st.radio("Have you previously had a stroke?: ", ('YES', 'NO'))
if (status == 'YES'):
    prevalentStroke = 1
else:
    prevalentStroke = 0

status = st.radio("Are you a Hypertensive patient?: ", ('YES', 'NO'))
if (status == 'YES'):
    prevalentHyp = 1
else:
    prevalentHyp = 0

status = st.radio("Are you a patient of diabetes?: ", ('YES', 'NO'))
if (status == 'YES'):
    diabetes = 1
else:
    diabetes = 0
totChol = st.number_input(label="cholesterol level in mg/dL",min_value=1.0,
    max_value=1000.0,step=1.0,format="%.2f")
st.write(totChol)
sysBP = st.number_input(label="systolic blood pressure",min_value=1.0,
    max_value=1000.0,step=1.0,format="%.2f")
st.write(sysBP)
diaBP = st.number_input(label="diastolic blood pressure",min_value=1.0,
    max_value=1000.0,step=1.0,format="%.2f")
# st.write(diaBP)
glucos = st.number_input(label="glucos level in mg/dL",min_value=1.0,
    max_value=1000.0,step=1.0,format="%.2f")
# st.write(glucos)

st.write("male:{} age :{}  Cigs :{}  BPMeds  : {}  prevalentStroke  : {}   prevalentHyp :{}  diabetes  : {}   totChol  : {}  sysBP  :{}   diaBP:{}  glucos :{}".format(male,age,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,glucos))
inputs = male,age,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,glucos
InputArray = np.array(inputs)
InputArray = InputArray.reshape(1,-1)
# st.write(inputs)
if st.button('submit'):
    result = loaded_model.predict(InputArray)
    st.write("The predicted output is : {}".format(int(result)))
    if result == 0 :
        st.write("10 year risk of coronary heart disease CHD , Negative.")
    else:
        st.write("10 year risk of coronary heart disease CHD , Positive .You need to consult to the doctor and start taking precautions")
