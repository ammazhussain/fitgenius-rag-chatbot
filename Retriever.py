from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
import numpy as np
import subprocess
from flask_cors import CORS  # Allow requests from your frontend

# Flask setup
app = Flask(__name__)
CORS(app)

# Load dataset
df = pd.read_csv("modified_megaGymDataset_v6.csv")

# Combine important text fields into one searchable string
df['search_text'] = df[['Exercise', 'Category', 'Type', 'Goal']].astype(str).agg(' '.join, axis=1)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df['search_text']).toarray()

# FAISS Indexing
dimension = vectors.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(vectors))

# Retrieval Function
def retrieve_relevant_exercises(query, k=5):
    query_vector = vectorizer.transform([query]).toarray()
    distances, indices = index.search(query_vector, k)
    return df.iloc[indices[0]][['Exercise', 'Category', 'Type', 'Goal', 'Sets/Duration', 'Reps']]

# Mistral LLM function
def ask_mistral(question, context):
    prompt = f"""
You are a fitness expert. Answer the following user question based on the exercise data provided.

Context:\n{context}\n
Question: {question}
    """.strip()

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    return result.stdout

# Flask API endpoint
@app.route("/query", methods=["POST"])
def query():
    user_input = request.json.get("question")
    if not user_input:
        return jsonify({"answer": "Please provide a valid question."})

    results = retrieve_relevant_exercises(user_input)
    context = results.to_string(index=False)
    response = ask_mistral(user_input, context)
    return jsonify({"answer": response.strip()})

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
