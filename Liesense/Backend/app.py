from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer import analyze_text
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "YOUR_API_KEY"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")

    text_score = analyze_text(text)

    return jsonify({
        "truth_score": text_score,
        "confidence": "Medium" if text_score > 50 else "Low",
        "stress": "High" if text_score < 40 else "Normal"
    })

@app.route("/question")
def get_question():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Ask a technical interview question for a CSE student"}
            ]
        )

        question = response["choices"][0]["message"]["content"]

        return jsonify({"question": question})

    except:
        return jsonify({"question": "Tell me about yourself."})

if __name__ == "__main__":
    app.run(debug=True)