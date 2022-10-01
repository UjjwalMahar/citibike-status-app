import streamlit
import pandas as pd
import snowflake.connector
from urllib.error import URLError

streamlit.title('Citibike station')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select * from station_status")
my_catalog = my_cur.fetchall()


df = pd.DataFrame(my_catalog)
df.reset_index(inplace=True)
#df.columns = map(lambda x: str(x).upper(), df.columns)
streamlit.write(df.columns)
#id_list = df[0].values.tolist()
#df.columns = df.columns.str.upper()
# #streamlit.write(id_list)

# option = streamlit.selectbox('Choose the station id to view the status:', list(id_list))
# if streamlit.button('show status'):
#           my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#           my_cur = my_cnx.cursor()
#           my_cur.execute("select * from station_status id = 72")
#           df2 = my_cur.fetchone()
#           streamlit.write(df2)
          
