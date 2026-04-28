# 📌 Resume Matching System using RAG

## 🚀 Overview

This project implements a **Resume Matching System** using **Retrieval-Augmented Generation (RAG)**.

It helps match job descriptions with the most relevant resumes by combining:

* Semantic search (embeddings)
* Vector database retrieval
* Keyword-based filtering
* Metadata-based scoring

---

## 🎯 Problem Statement

Recruiters often manually review large numbers of resumes, which is time-consuming and inefficient.

This system automates resume screening by:

* Understanding job requirements
* Searching resumes semantically
* Ranking candidates based on relevance

---

## 🧠 Key Features

* 📄 Document chunking (resume processing)
* 🔎 Semantic search using embeddings
* 🧩 Vector database using ChromaDB
* ⚡ Hybrid search (semantic + keyword matching)
* 📊 Scoring system (0–100 scale)
* 🧾 Metadata extraction:

  * Name
  * Skills
  * Experience
  * Education
* 🎯 Experience-based filtering
* 📦 Structured JSON output

---

## 🏗️ Project Structure

```bash
resume-rag-system/
├── data/
│   ├── resumes/
│   └── job_descriptions/
│
├── notebooks/
│   └── experiments.ipynb
│
├── vector_db/
├── resume_rag.py
├── job_matcher.py
├── utils.py
├── config.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone / Download Project

```bash
git clone <your-repo-url>
cd resume-rag-system
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Dataset

Place resumes inside:

```bash
data/resumes/
```

Place job descriptions inside:

```bash
data/job_descriptions/
```

---

### 5️⃣ Build Vector Database

```bash
python resume_rag.py
```

---

### 6️⃣ Run Job Matcher

```bash
python job_matcher.py
```

---

## 📥 Sample Input

```text
Looking for a Python developer with 5+ years experience in Machine Learning and SQL.
```

---

## 📤 Sample Output

```json
{
  "job_description": "...",
  "top_matches": [
    {
      "candidate_name": "Rahul Sharma",
      "resume_path": "resume_1.txt",
      "match_score": 92,
      "matched_skills": ["Python", "Machine Learning"],
      "relevant_excerpts": "...",
      "reasoning": "High semantic similarity and matching experience"
    }
  ]
}
```

---

## 📊 Performance Metrics

| Metric             | Value    |
| ------------------ | -------- |
| Retrieval Accuracy | ~0.7     |
| Precision@10       | ~0.6     |
| Latency            | ~0.4 sec |

---

## 🧪 Experiments (Notebook)

Notebook: `notebooks/experiments.ipynb`

Includes:

* Chunk size comparison
* Retrieval evaluation
* Latency measurement
* Matching performance analysis

---

## 🛠️ Technologies Used

* Python
* LangChain
* HuggingFace Embeddings
* ChromaDB
* Scikit-learn
* NumPy

---

## ⚠️ Challenges Faced

* Handling empty metadata in vector DB
* Managing embedding consistency
* Balancing semantic vs keyword matching
* Parsing real-world resume data

---

## 🔮 Future Improvements

* Web UI (React dashboard)
* FastAPI backend
* Advanced NLP (NER for better parsing)
* Real-time recruiter search interface
* Better ranking algorithms

---

## 🎥 Demo

A 3–4 minute demo video is included showing:

* System architecture
* Execution
* Output results
* Performance metrics

---

## 👨‍💻 Author

**Vikas P**

---

## ⭐ Conclusion

This project demonstrates how RAG can be applied to real-world hiring systems by combining semantic search with structured filtering and ranking.

---
