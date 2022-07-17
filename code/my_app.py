import pandas as pd
import streamlit as st
import yfinance as yf
import cufflinks as cf
import datetime

#page config
st.set_page_config(
     page_title="Stock Dashboard",
     page_icon="📈",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )


#initial_sidebar
st.sidebar.title("Stock Dashboard")
with st.container():
    startdate=st.sidebar.date_input("Start date",datetime.date(2021,1,1))
    enddate=st.sidebar.date_input("End date",datetime.date(2022,1,1))

#get info
stock_list=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
stock_symbol=st.sidebar.selectbox("Stock List",stock_list)
stock_data=yf.Ticker(stock_symbol)
stock_df=stock_data.history(period='1d',start=startdate,end=enddate)

logo='<img src={}>'.format(stock_data.info['logo_url'])
st.markdown(logo, unsafe_allow_html=True)

name=stock_data.info['longName']
st.header('{}'.format(name))

long_info=stock_data.info['longBusinessSummary']
st.write(long_info)

#misc
st.sidebar.balloons()
st.sidebar.text("")
st.sidebar.text("")

form = st.sidebar.form("my_form")
form.slider("Did you like this app?",0,5)
#st.slider("Outside the form")
form.form_submit_button("Submit")

#st.sidebar.
st.sidebar.info("About:  This is a share price dashboard which displays the share prices within the specified period.")

#more info
with st.expander("More Info"):
    for data in stock_data.info:
        if data!=('longBusinessSummary' or 'companyOfficers' or 'logo_rl'): 
            if stock_data.info[data]!=None:
                st.write(data.title(),": ",stock_data.info[data])

tab1, tab2 = st.tabs(["🗃 Data","📈 Chart"])

with tab1:
    st.subheader('Stock Data')
    st.write(stock_df)

with tab2:
    st.subheader('Statistical Analysis')
    fig=cf.QuantFig(stock_df,title='Figure',legend='top')
    fig.add_bollinger_bands()
    f=fig.iplot(asFigure=True)
    st.plotly_chart(f)

#st.write("Streamlit version:", st.__version__)
