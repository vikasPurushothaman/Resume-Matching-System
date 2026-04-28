from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import re

from config import *
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def load_vector_db():
    return Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embedding_model
    )

def extract_required_experience(jd):
    match = re.search(r"(\d+)\+?\s+years", jd.lower())
    return int(match.group(1)) if match else 0

def keyword_match_score(jd, text):
    keywords = ["Python", "Machine Learning", "SQL", "React"]



    score = 0
    matched = []

    for k in keywords:
        if k.lower() in jd.lower() and k.lower() in text.lower():
            score += 1
            matched.append(k)

    return score, matched

def compute_score(similarity, keyword_score):
    return int((similarity * 85) + (keyword_score * 5))


def match_job(job_description):
    vectordb = load_vector_db()

    docs_with_scores = vectordb.similarity_search_with_score(
        job_description, k=TOP_K
    )

    required_exp = extract_required_experience(job_description)

    results = []

    for doc, distance in docs_with_scores:
        similarity = 1 - distance 

        candidate_exp = doc.metadata.get("experience_years", 0)

        if candidate_exp < required_exp:
            continue  

        keyword_score, matched_skills = keyword_match_score(
            job_description, doc.page_content
        )

        score = compute_score(similarity, keyword_score)

        results.append({
            "candidate_name": doc.metadata.get("name", "Unknown"),
            "resume_path": doc.metadata.get("source"),
            "match_score": score,
            "matched_skills": matched_skills,
            "relevant_excerpts": doc.page_content[:200],
            "reasoning": (
                f"Matched {matched_skills}, "
                f"Experience: {candidate_exp} yrs, "
                f"Similarity: {similarity:.2f}"
            )
        })

    results = sorted(results, key=lambda x: x["match_score"], reverse=True)

    return {
        "job_description": job_description,
        "top_matches": results[:TOP_K]
    }


if __name__ == "__main__":
    jd = """
    Looking for a Python developer with 5+ years experience in Machine Learning and SQL.
    """

    output = match_job(jd)

    import json
    print(json.dumps(output, indent=2))