from google.adk.agents import Agent
from sub_agents.summary_writer import prompt

summary_writer_agent = Agent(
    model="gemini-2.0-flash-exp",
    name="summary_writer_agent",
    description="A helpful agent that combines the prediction results and search results and provides final strategy/summary for the builder.",
    instruction=prompt.SUMMARY_WRITER_PROMPT
)


