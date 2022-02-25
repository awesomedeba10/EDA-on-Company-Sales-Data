import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pickle

st.set_page_config(
    page_title="EDA on Company Sales Data",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "https://github.com/awesomedeba10"
    }
)

from build import GeneratePage
from utils import *


app = GeneratePage(st)

st.title('EDA on Company Sales Data')
st.caption('It is my first attempt to create an app using Streamlit. This is a basic data exploration app on a company \
    sales data which was done as a part of AlmaBetter Data Science Bootcamp.')
st.caption('Link to the [Colab Notebook](https://colab.research.google.com/drive/19rbsQf0GcWMo7EHcbhzJ4FYr4rc-QX6u?usp=sharing)')

def main():
    app.add_page('Preview Data', preview_data)
    app.add_page('Total Profit vs Month', linePlot)
    app.add_page('Units Sold vs Month', units_sold)
    app.run()

if __name__ == '__main__':
    main()


