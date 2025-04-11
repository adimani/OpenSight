from google.adk.agents import Agent
from sub_agents.forecast import prompt
# import model script from parent directory
from sub_agents.forecast  import model

def forecast_tool():
    # Call the model's prediction function
    predicted_hpi = round(model.predict_price(), 2)

    # Generate dynamic plots (this is a placeholder; actual plotting code would go here)
    plot_reference = "Dynamic visualizations for historical HPI (blue) and predicted HPI (red) are available in the UI."

    return {
        "predicted_hpi": predicted_hpi,
        "plot_reference": plot_reference
    }

forecast_agent = Agent(
    model="gemini-2.0-flash-exp",
    name="forecast_agent",
    description="A helpful agent that obtains the predicted HPI and plots for a given date.",
    instruction=prompt.FORECAST_PROMPT,
    tools=[
        forecast_tool
    ]
)