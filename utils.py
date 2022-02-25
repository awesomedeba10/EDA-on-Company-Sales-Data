import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

def process_data(df):
    df['month_name'] = df['month_number'].apply(lambda x: datetime.datetime(2020, x, 1).strftime('%B'))
    return df

@st.cache
def load_data():
    df = pd.read_csv('data/company_sales_data.csv')
    df = process_data(df)
    return df

df = load_data()

def preview_data():
    st.subheader('All Data')
    st.dataframe(df)
    st.subheader('Data Statistics')
    st.write(df.describe())

def linePlot():
    st.subheader('Monthly Profit Graph : Total Profit vs Month')
    fig = plt.figure(figsize=(13, 4))
    sns.lineplot(x="month_name", y="total_profit", data=df,
        markers=True)
    plt.xlabel('Month')
    plt.ylabel('Total Profit')
    st.pyplot(fig)

def units_sold():
    st.subheader('Monthly Units Sold Graph : Units Sold vs Month')
    product_df = pd.melt(df, id_vars=['month_name'], value_vars=['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer'],
        var_name='product', value_name='units_sold')
    fig = plt.figure(figsize=(13, 4))
    sns.barplot(data=product_df, x='month_name', y='units_sold', hue='product')
    st.pyplot(fig)
    fig2 = plt.figure(figsize=(13, 4))
    sns.kdeplot(data=product_df, x="units_sold", hue="product", multiple='stack')
    st.pyplot(fig2)
