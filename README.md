# RoleColorAI – AI Engineer Take-Home Assignment

## Introduction

This repository contains my solution to the **RoleColorAI – AI Engineer Take-Home Assignment**.

RoleColorAI approaches resumes through a **team-role lens**, focusing on *how* someone contributes to a team rather than only *what* their job title is.  
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

The keywords were chosen based on common resume language and typical team responsibilities.  
All keywords are **lemmatized** to align with NLP token processing and avoid mismatches between word forms (e.g., *collaborated → collaborate*).

This approach keeps the framework transparent and easy to reason about.

---

## Resume RoleColor Scoring (Part 2)

The resume is processed using **spaCy** for lightweight NLP:

- Tokenization
- Lemmatization
- Stopword removal

Each meaningful token is compared against the RoleColor keyword sets.  
When a match is found, the corresponding RoleColor score is incremented.

To make scores comparable across resumes of different lengths, raw counts are **normalized into a score distribution**.

Example output:
