# 🚀 Azure OpenAI + Azure AI Search Chatbot (GPT-4o)

A production-ready Flask chatbot application integrated with:

- ✅ Azure OpenAI (gpt-4o deployment)
- ✅ Azure AI Search
- ✅ Semantic search
- ✅ Environment-based secure configuration

---

# 📌 Architecture Overview

User → Flask API → Azure AI Search → Azure OpenAI (GPT-4o) → Response

---

# 🏗️ Tech Stack

- Python 3.10+
- Flask
- Azure OpenAI
- Azure AI Search
- python-dotenv
- Git & GitHub

---

# 🧱 Step 1 — Create Azure OpenAI Resource

1. Go to Azure Portal
2. Click "Create Resource"
3. Search for **Azure OpenAI**
4. Select:
   - Region: East US (or your region)
5. Click Create

📷 Screenshot:
![Azure OpenAI Resource](screenshots/1-create-resource.png)

---

# 🧠 Step 2 — Create Model Deployment

1. Open your Azure OpenAI resource
2. Go to "Model Deployments"
3. Click "Create"
4. Select:
   - Model: gpt-4o
   - Deployment name: gpt-4o
5. Click Deploy

📷 Screenshot:
![Model Deployment](screenshots/2-deployment.png)

---

# 🔑 Step 3 — Copy Keys and Endpoint

1. Go to "Keys and Endpoint"
2. Copy:
   - Endpoint URL
   - Key 1

📷 Screenshot:
![Keys and Endpoint](screenshots/3-keys.png)

---

# 🔎 Step 4 — Create Azure AI Search

1. Create Azure AI Search resource
2. Create index
3. Upload documents
4. Enable Semantic Search

📷 Screenshot:
![Azure AI Search](screenshots/4-search.png)

---

# 💻 Step 5 — Setup Project Locally

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/azure-openai-chatbot.git
cd azure-openai-chatbot
