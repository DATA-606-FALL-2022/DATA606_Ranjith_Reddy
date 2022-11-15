import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from ProductRecommendor import prod_recommender, product

pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def pred(user_id,product_id,lift,recc):
    
    prediction=model(user_id,product_id,lift,recc)
    print(prediction)
    return prediction


def main():
    #st.title("Product Recommendation")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Product Recommender
     </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    user_id = int(st.number_input("User ID"))
    product_id = int(st.number_input("product ID"))
    lift = int(st.number_input("Lift"))
    recc = int(st.number_input("No of Recommendations"))

    result=""
    if st.button("Predict"):
        result=pred(user_id,product_id,lift,recc)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()