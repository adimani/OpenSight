from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.genai import types
from transformers import pipeline
from datetime import datetime
from sub_agents.forecast.agent import forecast_agent
from sub_agents.search_results.agent import search_results_agent
from sub_agents.summary_writer.agent import summary_writer_agent
import prompt


# (DistilGPT-2) using Hugging Face Transformers.
# llm_pipeline = pipeline("text-generation", model="distilgpt2")

APP_NAME = "open_sight_agent"
USER_ID = "adimani1702"       
SESSION_ID = "session_001"     

# Creating agent, agent tools and session service
root_agent = Agent(
    name="open_sight_agent",
    model="gemini-2.0-flash-exp",  
    description=("A helpful agent to summarize information from the forecast and search results agents. "),
    instruction=prompt.ROOT_PROMPT_4,
    tools = [AgentTool(agent=forecast_agent), 
             AgentTool(agent=search_results_agent)]
)

session_service = InMemorySessionService()
session = session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)



# Calling agent
def call_agent(query, target_date=None):
    # If no target date is provided, use today's date.
    # if target_date is None:
    #     target_date = datetime.today().strftime('%Y-%m-%d')

    # prompt = compose_llm_prompt(query, target_date)

    content = types.Content(role='user', parts=[types.Part(text=query)])
    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)
    
    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            # print("Agent Response:", final_response)
            return final_response
    # for event in events:
    #     if event.is_final_response():
    #         print("Final Response Parts:")
    #         for part in event.content.parts:
    #             print(part) 

# Example usage:
# call_agent("What are the latest trends in homebuyer demand I should be aware of to sell houses now?")
