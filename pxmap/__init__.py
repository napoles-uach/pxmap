import os
import streamlit.components.v1 as components
def px_static(fig, width=700, height=500):
    return components.html(
        fig.to_html(),height=height + 10, width=width
       )
