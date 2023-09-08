import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title("My Parents New Healthy Diner")

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruits they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#create a repetative code block
def get_fruity_vice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
   # write your own comment -what does the next line do? 
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
streamlit.dataframe(fruits_to_show)
streamlit.write("---")

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please Select a fruit to get information")
  else:
    back_from_function=get_fruity_vice_data(fruit_choice)
    # write your own comment - what does this do?
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

streamlit.header("The friuit load list contains")
#Snowflake related-function
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return my_cur.fetchall()
#Add a button to load the fruit
if streamlit.button('Get fruit load List'):
  my_cnx= snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
