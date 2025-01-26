from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated labels for multi-label classification
SIMULATED_LABELS = {
    "AI": ["Artificial Intelligence", "Machine Learning"],
    "Agriculture": ["Crop Management", "Fertilizers"],
    "Technology": ["Programming", "Web Development"]
}

# Simulated NER entities
SIMULATED_ENTITIES = {
    "AI": ["Neural Networks", "GPT-3"],
    "Agriculture": ["Wheat", "Soil Health"],
    "Technology": ["Python", "Docker"]
}

@app.route('/process', methods=['POST'])
def process_text():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Static simulated results
    predicted_labels = ["AI", "Technology"]  # Pretend this is the result of a model
    extracted_entities = ["Neural Networks", "Python"]  # Pretend NER extraction
    summary = "This text discusses AI and technology."  # Pretend summary

    return jsonify({
        "predicted_labels": predicted_labels,
        "extracted_entities": extracted_entities,
        "summary": summary
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 
