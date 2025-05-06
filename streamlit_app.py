import streamlit as st
import pandas as pd

from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
from snowflake.snowpark import DataFrame
#from snowflake.core import Root

st.set_page_config(layout="wide")

st.markdown(
    """
          <style type="text/css">
          [data-testid=stSidebar] {
                    background-color: #e4f6ff;
                    color: #FFFFFF;
          }
          </style>
""",
    unsafe_allow_html=True,
)

session = get_active_session()

def get_snowflake_session():
    """Create or get cached Snowflake session."""
    return session  # Assuming 'session' is created elsewhere in the app

def toolsapp():
    with st.container():

        # Load your SVG file

        svg_content = read_svg("Snowflake.svg")
        svg_content3 = read_svg("Silgan_Holdings_logo.svg")

        # Display the animated SVG

        st.image(svg_content, width=100)
        st.image(svg_content3, width=300)
        st.header("Welcome to the Tag Search & Gen AI Tools App!")

def tsearch():
    with st.container():
        svg_content3 = read_svg("Silgan_Holdings_logo.svg")
        # Display the animated SVG
        st.image(svg_content3, width=300)
        st.header("Search for Tags")
        entered_text = st.text_input(
            "Enter tag to search",
            label_visibility="hidden",
            placeholder="Enter tag to search",
        )
        entered_text = entered_text.replace("'", "\\'")
        if entered_text:
            cortex_response = session.sql(f"SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.TAG_REFERENCES WHERE TAG_NAME ilike '{entered_text}%' or TAG_VALUE ilike '{entered_text}%'");
            st.caption("Tags:")
            st.write(cortex_response)

def askaq():
    with st.container():
        svg_content3 = read_svg("Silgan_Holdings_logo.svg")
        st.image(svg_content3, width=300)
        st.header("Use a Foundational LLM to Ask a Question")
        model_list = [
            "claude-3-5-sonnet",
            "deepseek-r1",
            "snowflake-arctic",
            "reka-flash",
            "reka-core",
            "llama3.2-1b",
            "llama3.2-3b",
            "mistral-7b"
        ]
        selected_model = st.selectbox("Which Foundational Model:", model_list)
        entered_code = st.text_area(
            "Paste the Data for Your Question",
            label_visibility="hidden",
            height=300,
            placeholder="Paste Data",
        )
        entered_code = entered_code.replace("'", "\\'")
        model_instruct = st.text_area(
            "Please provide Model Instructions",
            label_visibility="hidden",
            placeholder="Enter Prompt",
        )

        if st.button("Ask My Question!"):
            cortex_response = session.sql(
                    f"select snowflake.cortex.complete('{selected_model}',concat('[INST]','{model_instruct}','{entered_code}','[/INST]')) as RESPONSE").to_pandas().iloc[0]["RESPONSE"];
            st.caption("Answer:")
            st.write(cortex_response)

def nextba():
    with st.container():
        svg_content3 = read_svg("Silgan_Holdings_logo.svg")
        st.image(svg_content3, width=300)
        st.header("Use a Foundational LLM to Identify Next Best Action")
        model_list = [
            "claude-3-5-sonnet",
            "deepseek-r1",
            "snowflake-arctic",
            "reka-flash",
            "llama3.2-1b",
            "llama3.2-3b",
            "mistral-7b"
        ]
        selected_model = st.selectbox("Which Foundational Model:", model_list)
        entered_code = st.text_area(
            "Paste the Data for Your Question",
            label_visibility="hidden",
            height=300,
            placeholder="Paste Data",
        )
        entered_code = entered_code.replace("'", "\\'")
        default_model_instruct = """Based on these notes, please provide the next best action"""
        model_instruct = st.text_area(
            "Please provide Model Instructions",
            default_model_instruct,
            label_visibility="hidden",
            placeholder="Enter Prompt",
        )

        if st.button("Next Best Action!"):
            cortex_response = session.sql(
                    f"select snowflake.cortex.complete('{selected_model}',concat('[INST]','{model_instruct}','{entered_code}','[/INST]')) as RESPONSE").to_pandas().iloc[0]["RESPONSE"];
            st.caption("Answer:")
            st.write(cortex_response)

def read_svg(path):

    with open(path, 'r') as f:

        svg_string = f.read()

    return svg_string

page_names_to_funcs = {
    "Tools App": toolsapp,
    "Tag Search": tsearch,
    "Next Best Action": nextba,
    "Ask the LLM a ?": askaq
}

selected_page = st.sidebar.selectbox("Select", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
