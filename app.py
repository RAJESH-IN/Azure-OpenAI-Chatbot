import os
from flask import Flask, request, jsonify
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Azure OpenAI
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Azure Search
search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name="support-index",
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json["question"]

    # Search documents
    results = search_client.search(user_question)
    context = " ".join([doc["content"] for doc in results])

    # Generate response
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful support assistant."},
            {"role": "user", "content": f"Context: {context}\nQuestion: {user_question}"}
        ]
    )

    return jsonify({"answer": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True)
