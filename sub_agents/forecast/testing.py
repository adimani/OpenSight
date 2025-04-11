import model

def forecast_tool():
    # Call the model's prediction function
    predicted_hpi = model.predict_price()

    # Generate dynamic plots (this is a placeholder; actual plotting code would go here)
    plot_reference = "Dynamic visualizations for historical HPI (blue) and predicted HPI (red) are available in the UI."

    return {
        "predicted_hpi": predicted_hpi,
        "plot_reference": plot_reference
    }


# call forecast_tool
if __name__ == "__main__":
    result = forecast_tool()
    print(result)