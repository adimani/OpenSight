# 🏠 OpenSight: AI-Powered Home Sales Assistant

**OpenSight** is an intelligent assistant that empowers home builders and real estate stakeholders with strategic market insights, demand forecasts, and action-oriented recommendations. By blending macroeconomic forecasting, multi-agent LLM reasoning, and real-time market data, OpenSight provides a powerful, interactive decision-making companion.



## ✨ Inspiration

This project is heavily inspired by the mission of [OpenHouse.ai](https://openhouse.ai/) — a cutting-edge company that leverages AI to help home builders make more informed, data-driven decisions. OpenSight aims to explore and extend that philosophy, demonstrating how open-source AI agents and forecasting tools can be combined to deliver a robust home sales advisory system.

## 🚀 Demo

Click to watch a live walkthrough of OpenSight in action:  

🎥 **Demo**:  

https://github.com/user-attachments/assets/e914b651-be83-46e1-9821-93ed2f6c03bd



## 🔧 What It Does

OpenSight functions as a multi-modal market assistant for home builders. It integrates:
- **LLM agents** for smart strategy generation
- **HPI forecasting** as a proxy for homebuyer demand
- **Google search tools** for real-time economic and housing trends
- **Visual dashboards** that show macroeconomic movements (interest rates, GDP, etc.)



## 🧭 How It Works

The application is built using a **multi-agent architecture** powered by Google’s Agent SDK (ADK), with agents executing tasks like:

#### Agent Flow

1. **`forecast_agent`** – Predicts the House Price Index (HPI) using macroeconomic data. This is treated as a measure of housing demand.
2. **`search_results_agent`** – Pulls the latest housing news and macroeconomic trends using a live search.
3. **`root_agent`** – Orchestrates the sub-agents to ensure a structured response is delivered to the user.

> Forecasts are visually shown alongside historical data using dynamic line charts for HPI, interest rates, and GDP.

## 📈 Forecasting Methodology

The model uses **HPI as a proxy for homebuyer demand**, predicted using:
- **Multiple Linear Regression** (final production model)
- Tried and tested:
  - Dense Neural Networks
  - Lasso Regression
  - Ridge Regression
  - XGBoost Regressor

These models use features like:
- Lagged HPI, GDP, interest rate, S&P 500 volume (proxy for wealth), unemployment, and moving averages.

## ⚠️ Problems Faced & Limitations

- **📊 Data availability & freshness:**  
  Forecasts rely on past monthly macroeconomic data. The prediction for "today" is actually based on the last completed month.

- **🧠 LLM Robustness:**  
  Currently tuned for market strategy prompts only. It needs improvements to handle more flexible, conversational queries.

- **🔁 No context memory:**  
  OpenSight lacks persistent chat memory. Integration with **LangChain** for history/context threading and RAG pipelines is a future priority.

---
