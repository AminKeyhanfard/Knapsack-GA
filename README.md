# Genetic Algorithm for the Knapsack Problem 🧬🎒

This project implements a simple **Genetic Algorithm (GA)** to solve the **0/1 Knapsack Problem**

## 🧠 Problem Overview

You are given:
- A list of items, each with a **weight** and **value**
- A backpack (knapsack) with a **maximum weight capacity**

The goal is to select a subset of the items such that:
- The **total weight** does not exceed the capacity
- The **total value** is as high as possible

---

## 📌 How It Works

This project uses a basic GA setup:
- **DNA Representation**: A binary list where 1 means "include the item"
- **Fitness Function**: Total value of selected items (0 if overweight)
- **Selection**: Top N individuals kept each generation
- **Crossover**: Random combination of parent genes
- **Mutation**: Small chance to flip each bit

The script also **plots fitness over generations** using `matplotlib`.

---

## 📈 Example Output

```bash
Generation 01 | Best fitness: 20
Generation 02 | Best fitness: 27
...
🏆 Best solution found:
DNA: [1, 1, 0, 1, 0, 1, 0, 0, 1]
Total value: 41
Total weight: 10
```

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.7+
- `numpy`
- `matplotlib`

### ▶️ Run the script

```bash
python main.py
```

---

## 🗂️ Project Structure

```
knapsack-ga/
├── main.py
└── README.md
```

---

## 📚 References

- [Knapsack Problem – Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem)
- [Genetic Algorithms – Wikipedia](https://en.wikipedia.org/wiki/Genetic_algorithm)

---

## 📄 License

This project is licensed under the MIT License.

---
