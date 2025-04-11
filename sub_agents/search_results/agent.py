from google.adk.agents import Agent
from google.adk.tools import google_search
from sub_agents.search_results import prompt


search_results_agent = Agent(
    model="gemini-2.0-flash-exp",
    name="search_results_agent",
    description="A helpful agent that searches latest housing market news and macroeconomic trends in Canada.",
    instruction=prompt.SEARCH_RESULTS_PROMPT,
    tools=[google_search]
)