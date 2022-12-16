import streamlit as st
import pandas as pd
import dataframe

st.title('My parents New Health Diner')
st.header('Breakfast Favourites')

st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avacado Toast - For Muthu')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = st.multiselect("Pick some Fruits",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

st.text(fruits_to_show)
st.dataframe[data=None]

#st.text(fruits_to_show)
#df_my_fruit_list = pd.DataFrame(fruits_to_show)

#st.dataframe(df_my_fruit_list)
#st.text(df_my_fruit_list)
#streamlit.text(fruits_to_show)

#streamlit.dataframe[my_fruit_list]
