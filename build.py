"""
This file is the class for generating multiple Streamlit applications
or create multiple page through an object oriented framework. Definitely
not written by me but I found it useful to learn how to do this and
modified some of its code.
"""

import pandas as pd

class GeneratePage:

    def __init__(self, st) -> None:
        """Passing streamlit instance to the class. And creating empty page list."""
        self.pages = []
        self.st = st

    def add_page(self, title, func) -> None: 
        self.pages.append({
            "title": title, 
            "function": func
        })

    def run(self):
        page = self.st.sidebar.selectbox(
            'App Navigation',
            self.pages, 
            format_func=lambda page: page['title']
        )

        page['function']()


class GeneratePageYoo:

    def __init__(self, st) -> None:
        """Passing streamlit instance to the class. And creating empty page list."""
        self.pages = []
        self.st = st

    def add_page(self, title, func) -> None: 
        self.pages.append({
            "title": title, 
            "function": func
        })

    def run(self):
        page = self.st.sidebar.selectbox(
            'App Navigation',
            self.pages, 
            format_func=lambda page: page['title']
        )

        page['function']()