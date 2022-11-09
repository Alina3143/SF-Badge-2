import streamlit
import pandas
streamlit.title("SF Badge Ass 1")
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗  Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected = streamlit.multiselect("Pick some fruits", list(my_fruit_list.index), ['Avocado','Strawberries'], default=['Avocado'])
#streamlit.dataframe(my_fruit_list)
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
