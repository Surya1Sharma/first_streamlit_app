import streamlit
import pandas
streamlit.title("My Parents New Healty Diner")
streamlit.header('Breakfast Fevourites')
streamlit.text('🥣 Omega3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 hard Boiled & Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick Some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
import requests
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_row = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
add_my_fruit = streamlit.text_input('What fruit would you like to Add?','Jackfruit')
streamlit.write(fruit_choice)
streamlit.text('Thanks for adding Jackfruit')

