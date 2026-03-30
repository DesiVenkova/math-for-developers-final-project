# Mathematical Analysis of Candidate–Job Similarity

This project explores how candidate profiles and job descriptions can be represented as vectors and compared using mathematical similarity measures.

## Project Overview

The goal of this project is to model recruitment decision-making using linear algebra.

Each candidate and job description is represented as a vector of skills, and different similarity metrics are used to evaluate how well they match.

## Key Concepts

- Vector Space Representation
- Euclidean Distance (L2)
- Manhattan Distance (L1)
- Dot Product
- Cosine Similarity
- Scale Sensitivity vs Scale Invariance
- Weighted Similarity

## Example Scenario

The project compares:

- A job description requiring balanced skills
- A junior candidate with correct skill proportions
- A specialist with high but unbalanced experience

It demonstrates how:

- L2 distance favors magnitude
- Cosine similarity favors direction (skill alignment)

## Project Structure

- `Final Exam Project.ipynb` – main analysis and visualizations  
- `similarity_metrics.py` – core mathematical functions  

## How to Run

1. Install dependencies:
```bash
pip install numpy matplotlib
