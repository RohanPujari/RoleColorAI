# RoleColorAI – AI Engineer Take-Home Assignment

## Introduction

This repository contains my solution to the **RoleColorAI – AI Engineer Take-Home Assignment**.

RoleColorAI approaches resumes through a **team-role lens**, focusing on *how* someone contributes to a team rather than only *what* their job title is. This is a wonderful idea for the companies to execute and cutdown time while hiring.
This prototype demonstrates a simple and interpretable way to:

1. Analyze raw resume text
2. Identify which **RoleColor traits** are most represented
3. Generate a **role-aligned resume summary**

The solution is intentionally lightweight and reasoning-driven, prioritizing clarity over model complexity.

---

## RoleColor Framework (Part 1)

The system uses a basic keyword framework to represent each RoleColor:

- **Builder** – Strategy, vision, system design, innovation, ownership
- **Enabler** – Collaboration, communication, stakeholder alignment, coordination
- **Thriver** – Fast execution, adaptability, delivery under pressure
- **Supportee** – Reliability, documentation, testing, maintenance, stability

The keywords can be chosen based on common resume language and typical team responsibilities that the company or the hiring team wants.  
All keywords are **lemmatized** to align with NLP token processing and avoid mismatches between word forms (e.g., *collaborated → collaborate*).

This approach keeps the framework transparent and easy to reason about.

---

## Resume RoleColor Scoring (Part 2)

The resume is processed using a library **spaCy** for lightweight NLP preprocessing:

- Tokenization
- Lemmatization
- Stopword removal

Each meaningful token is compared against the RoleColor keyword sets.  
When a match is found, the corresponding RoleColor score is incremented by 1.

To make scores comparable across resumes of different lengths (basically to normalize), raw counts are **normalized into a score distribution**.

Example output:
Builder: 0.29
Enabler: 0.29
Thriver: 0.21
Supportee: 0.21

This is the assessment that is been asked to perform, but I have few questions and ideas to increase the quality or approach.
First of all, thank you for giving me this opportunity to work or build towards this idea. I was genuinely enjoying building this project and I see a god scope of this in the future hopefully replacing ATS systems :D

Secondly, there are gaps which I noticed in this area. A person cannot be a builder only and Im guessing the company dont weant to hire only a builder or Enabler or Supportee, they want  a blend of these with different proportions like for a HR you need to have a Dominant Enabler, Great Supportee, Best Thriver and Good Builder. This might be different for different positions like AI engineer, or Marketing Analyst or Product Manager and also depends on Seniority. So displaying all the values with different positions will be more helpful...!!

Thirdly, the summary is not the aligned to the resume context rather than RoleColor scores. In order for this to be implimented, we would require a RAG based LLM model(Summarizer models like BART/Pegasus) which would take the uploaded resume and the scores and generate a summary of this system that could be more reliable than the answer we produce.

And Finally, I felt this was a very good idea to be implimented in the hiring domain. All the best to the team and hope to see you on the other side.