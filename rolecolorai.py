import re
import spacy
from collections import Counter

ROLECOLOR_KEYWORDS = {
    "Builder🔴": [
        "strategy", "vision", "innovation", "architecture",
        "design", "scalable", "roadmap", "ownership", "product", "data"
    ],
    "Enabler🔵": [
        "collaborate", "stakeholder", "communicate", "align",
        "coordinate", "mentor", "cross", "functional", "lead"
    ],
    "Thriver🟡": [
        "fast-paced", "deadline", "pressure", "execution",
        "delivery", "agile", "adapt", "problem-solving", "accuracy"
    ],
    "Supportee🟢": [
        "reliability", "maintenance", "documentation",
        "testing", "monitoring", "support", "stability"
    ]
}


nlp = spacy.load("en_core_web_sm")


def score_resume_nlp(text):
    doc = nlp(text.lower()) # stores input data in lowercase
    scores = Counter() # used to count in the later part of the code

    for token in doc:
        if token.is_stop or not token.is_alpha: # Basic NLP preprocessing
            continue

        lemma = token.lemma_ #Lemmatization to catch the root words

        for role, keywords in ROLECOLOR_KEYWORDS.items():
            if lemma in keywords: # If there is a word match, with the lemma word, you count them and if that repeats, incriment the score.
                scores[role] += 1 

    total = sum(scores.values()) or 1
    return {k: round(v / total, 2) for k, v in scores.items()} # Normalization process


# Pick the role with the highest score
def dominant_role(scores):
    return max(scores, key=scores.get)

# These are Sample Summaries which can be modified according to the role.
SUMMARY_TEMPLATES = {
    "Builder🔴": (
        "Strategic professional with a strong focus on innovation, system design, "
        "and long-term impact. Known for driving scalable solutions, owning outcomes, "
        "and shaping products that support business growth."
    ),
    "Enabler🔵": (
        "Collaborative professional who excels at connecting teams, aligning stakeholders, "
        "and enabling smooth execution. Brings clarity across functions and helps teams "
        "deliver effectively together."
    ),
    "Thriver🟡": (
        "Execution-focused professional who thrives in fast-paced environments. "
        "Proven ability to deliver under pressure, adapt quickly, and solve problems "
        "when timelines are tight."
    ),
    "Supportee🟢": (
        "Reliability-driven professional focused on stability, quality, and long-term support. "
        "Ensures systems run smoothly through documentation, testing, and consistent maintenance."
    )
}


def rewrite_summary(dominant_role):
    return SUMMARY_TEMPLATES[dominant_role]


if __name__ == "__main__":
    with open("sample_resume.txt", "r", encoding="utf-8") as f:
        resume_text = f.read()

    scores = score_resume_nlp(resume_text)
    role = dominant_role(scores)
    summary = rewrite_summary(role)

    print("RoleColor Scores:")
    for k, v in scores.items():
        print(f"{k}: {v}%")

    print("\nDominant RoleColor:", role,"with score", scores[role], "is the highest score")
    print("\nRewritten Summary:")
    print(summary)
