# import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# from prophet import Prophet

data = pd.read_csv("Leave_tracker1.py.csv")
# st.write(data)

data.info()
st.write(data)

data['date'] = pd.to_datetime(data['date'])

plt.figure(figsize=(15,6))
plt.plot(data['date'],data['status'])
plt.xticks(rotation='vertical')
plt.show()
# import matplotlib.pyplot as plt
# %matplotlib inline

# df=pd.read_csv("Leave_tracker1.py.csv")  
# st.write(df)
# df.head() 
# df.info()
# st.write(df)

# import matplotlib.pyplot as plt
# plt.figure(figsize=(15,6))
# plt.plot(df=)
