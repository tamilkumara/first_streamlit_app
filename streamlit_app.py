import streamlit
import pandas

streamlit.title('My parents New Health Diner')
streamlit.header('Breakfast Favourites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast - For Muthu')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list1 = my_fruit_list.set_index('Fruit')
streamlit.text(my_fruit_list1)

import streamlit
fruits_selected = streamlit.multiselect("Pick some Fruits",list(my_fruit_list1.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list1.loc[fruits_selected]
streamlit.text(fruits_to_show)
#streamlit.dataframe(my_fruit_list1)
#streamlit.dataframe[my_fruit_list]
