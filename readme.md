# Revuly 🚀

AI-Powered Review Collection & Semantic Filtering Service (FastAPI + PostgreSQL)

Revuly is a backend service that collects user reviews and uses **AI embeddings** to enable **topic-based filtering**, making review search smarter than keyword matching. It supports storing reviews, generating embeddings during ingestion, and retrieving the most relevant reviews using semantic similarity.

---

## ✨ Features

✅ Collect and store user reviews
✅ Automatic preprocessing (clean text generation)
✅ Generate **AI embeddings** for each review (Sentence Transformers)
✅ Store embeddings inside PostgreSQL (JSONB column)
✅ AI-powered semantic filtering (meaning-based search)
✅ Exclusion filtering (remove irrelevant topics like delivery/shipping)
✅ Clean architecture (Routes → Services → AI layer)

---

## 🧠 How it Works

### ✅ Review Ingestion (POST review)

When a user posts a review:

1. Review text is received via API
2. Text is cleaned/preprocessed
3. AI embedding is generated (`all-MiniLM-L6-v2`)
4. Review + embedding is stored in PostgreSQL

### ✅ Semantic Filtering (POST filter)

When a user searches:

1. Query text is converted to an embedding
2. Similarity is calculated with stored review embeddings
3. Reviews are ranked by relevance score
4. Top relevant reviews are returned

This enables semantic search like:

> Search: **“battery performance”**
> Returns: **“power backup is excellent”** ✅

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python)
* **Database:** PostgreSQL
* **ORM:** SQLModel
* **AI Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)
* **Embedding Storage:** PostgreSQL `JSONB`
* **Similarity Search:** Cosine similarity (NumPy)

---

## 📁 Project Structure

```bash
review-ai-service/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       ├── review_routes.py
│   │       └── filter_routes.py
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   ├── models/
│   │   └── review.py
│   ├── schemas/
│   │   └── review.py
│   ├── services/
│   │   ├── review_service.py
│   │   ├── filter_service.py
│   │   └── ai_service.py
│   ├── ai/
│   │   ├── embeddings.py
│   │   └── similarity.py
│   └── db/
│       ├── session.py
│       └── init_db.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Revuly.git
cd Revuly
```

### ✅ 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

### ✅ 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### ✅ 4. Setup PostgreSQL Database

Create a database in PostgreSQL:

```sql
CREATE DATABASE revuly;
```

Set your DB URL in `.env`:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/revuly
```

### ✅ 5. Run the Server

```bash
uvicorn app.main:app --reload
```

Server will start at:
📍 `http://127.0.0.1:8000`

Swagger Docs:
📍 `http://127.0.0.1:8000/docs`

---

## 📌 API Endpoints

### ✅ Health Check

`GET /health`

---

### ✅ Create Review

`POST /api/v1/review/`

**Request**

```json
{
  "text": "Battery lasts all day but packaging was bad",
  "rating": 4
}
```

---

### ✅ Get All Reviews

`GET /api/v1/review/get-all`

---

### ✅ Get Review by ID

`GET /api/v1/review/{review_id}`

---

### ✅ Semantic Filter Reviews

`POST /api/v1/review/filter`

**Request**

```json
{
  "query": "battery performance",
  "exclude": ["delivery"],
  "threshold": 0.55,
  "top_k": 5
}
```

---

## 🚀 Future Improvements

* ✅ Spam detection using ML model (SVM / Logistic Regression)
* ✅ Sentiment analysis (positive/negative/neutral)
* ✅ Topic classification (battery, camera, delivery, etc.)
* ✅ Use FAISS or a vector DB for faster similarity search at scale
* ✅ Authentication + Rate limiting
* ✅ Docker + Cloud deployment

---

## 👨‍💻 Author

**Yogiraj Ahirrao**

If you like this project, ⭐ the repo!
