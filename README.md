Python DSA + GenAI Interview Preparation Repository

This repository contains all essential Python, DSA, Data Preprocessing, and GenAI skills required for clearing Python Developer (GenAI) and AI Engineer internships/jobs.
It covers coding tasks + verbal interview theory exactly the way companies test.

📌 1. Coding Test (60–70%)

Companies mainly test your logic, DSA, and Python fundamentals — without AI help.

✅ A. Python Logic + DSA (Beginner–Intermediate)

You should be able to solve these easily:

Common DSA Coding Tasks

✔ Reverse a list
✔ Find top 3 most frequent words
✔ Count vowels in a string
✔ Two-sum problem
✔ Check palindrome
✔ Remove duplicates from a list
✔ Merge two sorted lists
✔ Basic searching/sorting
✔ Simple string manipulation
✔ Dictionary counting problems

Difficulty: Easy to Medium
Purpose: Check if you can code without AI or frameworks.

📌 2. Python for Data + GenAI

This is where Python + data handling skills are tested.

✅ Likely Coding Tasks
Data Handling

✔ Read CSV
✔ Read JSON
✔ Parse data cleanly (avoid errors)

Text Preprocessing

✔ Clean text
✔ Lowercase, remove special chars
✔ Remove stopwords
✔ Token-level cleaning

GenAI Utility Functions

✔ Write a text chunking function
✔ Implement cosine similarity from scratch
✔ Build your own simple retrieval system
✔ Write a mini prompt template function
✔ Implement vector search without external libraries
✔ Ensure clean & modular output

These tests check your ability to work with embeddings, retrieval, vector logic, and LLM input/output.

🎯 What They Evaluate in Code

✔ Clean + modular functions
✔ No unnecessary libraries
✔ Variable names should be meaningful
✔ Should run without errors on first attempt
✔ Proper return statements
✔ No complex deep-learning models — only logic

📌 3. Verbal Evaluation (30–40%)

Most candidates lose marks here.
They ask simple but conceptual questions.

🐍 A. Python Theory Questions (90% chance)

Expect questions like:

✔ Difference between list and tuple

(List = mutable, Tuple = immutable)

✔ Explain OOP concepts

Classes, objects, inheritance, polymorphism, encapsulation, abstraction.

✔ What is a decorator?

A function that modifies another function without changing its code.

✔ What is a generator?

Function that uses yield to produce values one at a time (memory efficient).

✔ Mutable vs Immutable types

Mutable → list, dict, set
Immutable → tuple, string, int

✔ What is *args and **kwargs?

*args → variable positional arguments
**kwargs → variable keyword arguments

✔ How does memory work in Python?

Reference-based, garbage collector, stack frame, heap objects.

🤖 B. GenAI Theory Questions (90% chance)

You must know these clearly.

✔ What is an embedding?

A numeric vector representation of text for similarity search.

✔ What is cosine similarity?

A measure of angle between vectors (0–1 similarity score).

✔ How does RAG work?

Query → embed → search vector store → retrieve chunks → pass to LLM

✔ Why do we chunk text?

LLMs require smaller input pieces; chunking prevents context loss and improves retrieval.

✔ What is a vector store?

Database optimized for storing + searching embeddings → FAISS, Chroma, Pinecone.

✔ Difference between LangChain & LangGraph

LangChain = high-level tools, pipelines

LangGraph = state-machine workflow for agent reliability and control

📊 C. Pandas / NumPy Questions (Medium Chance)
✔ How to filter rows?

Using boolean masks, df[df['col'] > 5], .query()

✔ What is vectorization?

Performing operations on entire arrays without loops — faster due to C-level optimization.

✔ Difference between .loc and .iloc?

.loc → label-based indexing

.iloc → integer position-based indexing

📁 Repository Structure
01_DSA/
02_Python_Core/
03_Data_Preprocessing/
04_GenAI/
05_Assessments/

🤝 Contributions

This repo will be regularly updated with:

More coding tasks

More GenAI utility functions

More assessment-style questions

Practical examples
