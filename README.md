## CI Basics – Continuous Integration with GitHub Actions

This repository is a **hands-on learning project** focused on understanding **Continuous Integration (CI)** using **GitHub Actions**.

It demonstrates how automated testing can be triggered on every push and pull request to ensure code correctness.

---

## What this repository contains

* A simple **Python application** that calculates:

  * Square
  * Cube
  * Fifth power
* **Unit tests** written using `pytest`
* A **GitHub Actions CI workflow** that:

  * Runs on `push` and `pull_request`
  * Sets up Python
  * Installs dependencies
  * Executes automated tests
* A basic **Streamlit UI** for interaction

---

## CI Workflow Overview

The CI pipeline performs the following steps automatically:

1. Checks out the repository
2. Sets up Python (v3.12)
3. Installs required dependencies
4. Runs unit tests using `pytest`

This ensures that every change is tested before being merged into the `main` branch.

---

## Technologies Used

* Python
* Pytest
* GitHub Actions
* Streamlit

---

## Learning Disclaimer & Credits

> This repository is created **for learning purposes**.

The code and CI workflow are **based on a YouTube tutorial** by **Vikash Das**, and have been followed to understand CI fundamentals.

**Source:**
Vikash Das – *MLops:Day 7 - Continous Integration*
[https://www.youtube.com/watch?v=vEUVeCQ63Ew&list=PLupK5DK91flV45dkPXyGViMLtHadRr6sp&index=7](https://www.youtube.com/watch?v=vEUVeCQ63Ew&list=PLupK5DK91flV45dkPXyGViMLtHadRr6sp&index=7)

All credit for the original explanation goes to the creator.
This repository is **not claimed as original work**, but as a learning and practice implementation.

---
