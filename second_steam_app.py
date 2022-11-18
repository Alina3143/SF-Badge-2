import streamlit
#import pandas
import requests
import snowflake.connector
import urllib.error import URLError

streamlit.title("SF Badge Ass 1")
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗  Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


fruityjuice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityjuice_response)
fruityjuice_normalized = pandas.json_normalize(fruityjuice_response.json())
streamlit.dataframe(fruityjuice_normalized)

# SnowFlake

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text(my_data_row)
#my_cur = my_cnx.cursor()

my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("Fruits to choose from:")
streamlit.dataframe(my_data_row)
#streamlit.write('The user entered ', fruit_choice)

#fruityjuice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
add_my_fruit =  streamlit.text_input('What fruit would you like information to ADD ?','Melon')
streamlit.text(add_my_fruit)
#my_cur.execute("INSERT INTO  fruit_load_list (FRUIT_NAME) VALUES(" +add_my_fruit+ ')')
