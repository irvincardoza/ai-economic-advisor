#!/bin/bash

# Create base folder
mkdir ai_financial_assistant
cd ai_financial_assistant

# Create directories
mkdir -p agents
mkdir -p utils
mkdir -p reports/generated_reports

# Create main files
touch app.py requirements.txt README.md

# Create agent files
touch agents/market_analyst_agent.py
touch agents/investment_strategy_agent.py
touch agents/risk_management_agent.py
touch agents/report_agent.py

# Create utils files
touch utils/finGPT_wrapper.py
touch utils/api_fetcher.py
touch utils/recommendation_engine.py
touch utils/report_generator.py

# Confirm directory structure
echo "Project structure created successfully:"
tree .
