import streamlit
import pandas as pd
import snowflake.connector
from urllib.error import URLError
import time
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

streamlit.markdown("<h1 style='text-align: center; color: white;'>Citibike Station 🚲 </h1>", unsafe_allow_html=True)



# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("""select * from citibike_status""")
my_catalog = my_cur.fetchall()
df = pd.DataFrame(my_catalog)

#streamlit.write(df)
hdrs = pd.DataFrame(my_cur.description)

id_list = df[0].values.tolist()
#streamlit.write(id_list)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_ntvobf3t.json"
lottie_hello = load_lottieurl(lottie_url_hello)



st_lottie(lottie_hello, key="hello", height=500, width=500)


option = streamlit.selectbox('Choose the station id to view the status:', list(id_list))
if streamlit.button('show status'):
          my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
          my_cur = my_cnx.cursor()
          my_cur.execute("""select * from citibike_status where "id" = """ + option + """; """)
          res = my_cur.fetchall()
          df2=pd.DataFrame(res,columns=hdrs['name']).loc[0]
          col1, col2 = streamlit.columns(2)
          for c in hdrs['name']:
                    with col1:
                              streamlit.write(*[x.upper() for x in c.split("_")], ":")
                    with col2:
                              streamlit.write(df2.at[c])
                    
  
          
