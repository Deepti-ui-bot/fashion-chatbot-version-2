# Fashion Chatbot - Version 2

A chatbot that provides fashion suggestions based on gender, season, and type of event.

## Features
- Suggests outfits for men and women.
- Considers the season (summer, winter, etc.) and event type (casual, formal, wedding).
- Automatically handles incomplete queries by prompting for missing details.
- Dynamic Context Handling: The bot retains context. If you change only one or two keywords (e.g., say "women" after "men summer casual"), it updates the relevant fields and keeps others unchanged.
- Interactive Prompts: The bot now prompts for missing details intelligently (e.g., if you only say "women wedding," it asks for the season to complete the suggestion).
- Robust Query Handling: Handles incomplete or out-of-order queries seamlessly (e.g., "casual men summer").

## What's New in Version 2
This version improves upon the original by introducing the following features:
- No hardcoding of the responses.
- Improved Dataset Structure: Uses a clean and organized `outfits.csv` file for fashion suggestions.
- Simple and efficient when more responses are to be added directly to the CSV file.

## How to Use
1. Clone the repository:
	git clone https://github.com/Deepti-ui-bot/fashion-chatbot-version-2.git

2. Install the dependencies:
	pip install -r requirements.txt

3. Run the chatbot:
	python app.py

## Files and Folders
app.py: Main chatbot script.
data/outfits.csv: Database of fashion suggestions.
requirements.txt: List of Python dependencies.

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is open-source. Feel free to use it for learning purposes.