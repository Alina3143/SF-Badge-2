import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
#create the repeatable code block - function
def get_fruityvice_data(this_fruit_choice):
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        return fruityvice_normalized

streamlit.title("SF Badge Ass 1")
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗  Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
  else:   
        back_from_function = get_fruityvice_data(fruit_choice)  
        streamlit.dataframe(back_from_function)        
except URLError as e:
      streamlit.error() 

# SnowFlake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

def get_fruit_load_list():
        with my_cnx.cursor() as my_cur:
                my_cur.execute("select * from fruit_load_list")
                return my_cur.fetchall()
        
# Add a button to load the fruit 
if streamlit.button('Get Fruit Load List'):
        my_cnx.snowflake.connector.connect(**streamlit.secrets["snowflake"])
        my_data_rows = get_fruit_load_list()
        streamlit.dataframe(my_data_rows)
    
# write your own comment -what does the next line do? 
#my_cur.execute("INSERT INTO fruit_load_list VALUES('from streamlit')")
# write your own comment - what does this do?
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)
#my_cur.execute("INSERT INTO fruit_load_list VALUES('from streamlit')")
#fruityjuice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityjuice_response)
#fruityjuice_normalized = pandas.json_normalize(fruityjuice_response.json())
#streamlit.dataframe(fruityjuice_normalized)
#streamlit.stop()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text(my_data_row)
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchall()
#streamlit.text("Fruits to choose from:")
#streamlit.dataframe(my_data_row)
#add_my_fruit =  streamlit.text_input('What fruit would you like information to ADD ?','Melon')
#streamlit.text(add_my_fruit)
#my_cur.execute("INSERT INTO  fruit_load_list (FRUIT_NAME) VALUES(" +add_my_fruit+ ')')
