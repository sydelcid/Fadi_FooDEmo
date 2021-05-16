import streamlit as st
import pandas as pd
import numpy as np

st.title("fooDEmo App")

st.header("An app to suggest food to upbeat your mood!")
st.subheader("by Syed Fadi")
st.subheader("Emotions need care!")

moodlist = ['Angry','Sad','Anxious','Stressed','Lethargic']
fooddict = {}

fooddict['Angry'] = ['Brazil Nuts', 'Omega-3 Fish (Salmon)', 'Eggs', 'Yoghurt']
fooddict['Sad'] = ['Dark Chocolate', 'Walnuts', 'Beans', 'Flax Seeds', 'Poultry']
fooddict['Anxious'] = ['Brazil Nuts', 'Omega-3 Fish (Salmon)', 'Eggs', 'Yoghurt']
fooddict['Stressed'] = ['Dark Chocolate', 'Walnuts', 'Beans', 'Flax Seeds', 'Poultry']
fooddict['Lethargic'] = ['Green Tea','Banana','Water','Apricots','Dates']

allergylist = ['None','Nuts','Dairy and Eggs','Meats','Seafood']

allergydict = {}
allergydict['Nuts'] = ['Brazil Nuts', 'Walnuts']
allergydict['Dairy and Eggs'] = ['Eggs']
allergydict['Meats'] = ['Poultry']
allergydict['Seafood'] = ['Omega-3 Fish (Salmon)']
allergydict['None'] = []

imgdict = {}
imgdict['Brazil Nuts'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/brazil_nuts.jpg"
imgdict['Omega-3 Fish (Salmon)'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/salmon.jpg"
imgdict['Eggs'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/eggs.jpg"
imgdict['Yoghurt'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/yoghurt.jpeg"
imgdict['Dark Chocolate'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/chocobrownie.jpeg"
imgdict['Walnuts'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/walnuts.jpg"
imgdict['Beans'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/beans.jpg"
imgdict['Flax Seeds'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/flaxseed.jpg"
imgdict['Poultry'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/poultry.jpg"
imgdict['Green Tea'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/green_tea.jpg"
imgdict['Banana'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/bananas.jpg"
imgdict['Water'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/water.jpg"
imgdict['Apricots'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/apricots.jpg"
imgdict['Dates'] = "/home/sydelcid/NixDev/stlitlrn/foodemo1/images/dates.jpg"


# st.write("""

# ## What is your current mood? Please select from dropdown.
# """)
moodchc = "blank"
allergychc = "blank"
foodchc = "blank"

moodchc = st.selectbox("What is your current mood? Please select from dropdown.",moodlist)
allergychc = st.selectbox("Select allergy food groups",allergylist)

if allergychc == "blank":
    st.image("/home/sydelcid/NixDev/stlitlrn/foodemo1/images/fadiappfront.jpg")
else:
    foodsel = list(filter(lambda x: x not in allergydict[allergychc], fooddict[moodchc]))

if st.checkbox("Show Available Food Choices"):
    foodchc = st.radio("Based on your mood, your food choices are as below. Please choose one item.", foodsel) #fooddict[moodchc]

if foodchc == "blank":
    st.image("/home/sydelcid/NixDev/stlitlrn/foodemo1/images/fadiappfront.jpg")
else:
    imgpath = imgdict[foodchc]
    st.image(imgpath)