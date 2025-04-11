import streamlit as st
from streamlit_chat import message
from datetime import datetime
from dotenv import load_dotenv
import os
from agent import call_agent
from sub_agents.forecast.model import predict_price, generate_forecast_plots, generate_forecast_data

# Loading environment variables
load_dotenv()

# Setting up the Streamlit app
st.set_page_config(
    page_title="OpenSight Home Sales Assistant",
    page_icon="🏠",
    layout="wide"
)

# Side bar for instructions
st.sidebar.title("How to Use OpenSight")
st.sidebar.markdown(
    """
    **OpenSight: AI-Powered Home Sales Assistant**

    **Overview:**
    - OpenSight provides strategic insights to help you optimize home sales.
    - It fuses macroeconomic forecasts with latest market trends.

    **Features:**
    - Forecasts the House Price Index (HPI) based on current & historical data which is a proxy for housebuyer demand.
    - Displays dynamic visualizations for HPI, interest rates, and GDP trends in the UI.
    - Offers actionable recommendations based on market conditions.

    **Instructions:**
    - Simply type your question in the chat box below.
    - Your queries can be about market trends, pricing strategies, or sales tactics.
    - The assistant uses today's data to generate predictions and insights.
    """
)

# Title
st.title("OpenSight Home Sales Assistant")
st.markdown("**Hey builder! I am here to assist you with strategies based on current conditions. What do you want?**")


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat history
for i, msg in enumerate(st.session_state.messages):
    if msg.get("speaker") == "user":
        message(msg.get("text"), is_user=True, key=f"user_{i}")
    else:
        message(msg.get("text"), is_user=False, key=f"bot_{i}")

# User input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here...", key="chat_input")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip():

    target_date = datetime.today().strftime('%Y-%m-%d')
    st.session_state.messages.append({"speaker": "user", "text": user_input})
    with st.spinner("Thinking..."):
        bot_response = call_agent(user_input)
    st.session_state.messages.append({"speaker": "bot", "text": bot_response})
    st.session_state.show_plots = True
    st.rerun()

# Display plots
if st.session_state.get("show_plots", False):
    st.markdown("### Market Visualizations")
    try:
        hpi_data, ir_data, gdp_data = generate_forecast_data()

        st.markdown("#### 📈 House Price Index (HPI)")
        st.line_chart(hpi_data)

        st.markdown("#### 💰 Interest Rates")
        st.line_chart(ir_data, color="#cf0c09")

        st.markdown("#### 🧾 Gross Domestic Product (GDP)")
        st.line_chart(gdp_data, color="#09cf4e") 
        st.session_state.show_plots = False
    except Exception as e:
        st.warning(f"Could not generate visualizations: {e}")
