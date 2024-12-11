from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Context to store user's details
user_context = {"season": None, "type": None, "gender": None}

# Read CSV database into DataFrame
outfits_df = pd.read_csv('data/outfits.csv')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_outfit', methods=['POST'])
def get_outfit():
    global user_context
    data = request.json
    query = data.get('query', '').lower()

    # Extract gender, type, and season from the query
    genders = ["men", "women"]
    types = ["casual", "formal", "wedding"]
    seasons = ["summer", "winter", "spring", "fall"]

    detected_gender = None
    detected_type = None
    detected_season = None

    # Detect keywords from user input
    for gender in genders:
        if gender in query:
            detected_gender = gender
    for outfit_type in types:
        if outfit_type in query:
            detected_type = outfit_type
    for season in seasons:
        if season in query:
            detected_season = season

    # Update the context with only what is detected
    if detected_gender:
        user_context["gender"] = detected_gender
    if detected_type:
        user_context["type"] = detected_type
    if detected_season:
        user_context["season"] = detected_season

    # Prompt for missing context
    if not user_context["type"]:
        return jsonify({"suggestion": "Please specify the outfit type (casual, formal, or wedding)."})
    if not user_context["season"]:
        return jsonify({"suggestion": "Please specify the season (summer, winter, spring, or fall)."})
    if not user_context["gender"]:
        return jsonify({"suggestion": "Please specify the gender (men or women)."})
    
    # Query database (CSV) for response
    match_query = outfits_df[
        (outfits_df['gender'] == user_context["gender"]) &
        (outfits_df['season'] == user_context["season"]) &
        (outfits_df['type'] == user_context["type"])
    ]
    
    if not match_query.empty:
        suggestion = match_query.iloc[0]['suggestion']
        return jsonify({"suggestion": f"For {user_context['gender']}: {suggestion}."})
    else:
        return jsonify({"suggestion": "Sorry, no suggestion found in the database."})


if __name__ == '__main__':
    app.run(debug=True)
