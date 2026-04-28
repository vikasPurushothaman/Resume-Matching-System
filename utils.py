import re
from typing import Dict

def extract_metadata(text: str) -> Dict:
    metadata = {}
    lines = text.split("\n")
    metadata["name"] = lines[0].strip() if lines and lines[0].strip() else "Unknown"
    skills = re.findall(r"(Python|Java|SQL|Machine Learning|React|Node\.js)", text, re.I)
    metadata["skills"] = list(set(skills)) if skills else ["Unknown"]
    exp = re.findall(r"(\d+)\+?\s+years", text.lower())
    metadata["experience_years"] = int(max(map(int, exp))) if exp else 0
    education = re.findall(r"(B\.?Tech|M\.?Tech|Bachelor|Master|PhD)", text, re.I)
    metadata["education"] = list(set(education)) if education else ["Unknown"]
    return metadata