# 🚀 FastVLM-Agent Benchmark

## 🧠 Overview

FastVLM-Agent is a prototype benchmark framework designed to evaluate **multimodal AI agents** that process both images and text. The goal of this project is to study the **trade-off between latency (speed) and reasoning quality** in vision-language systems.

Modern multimodal models such as GPT-4 Vision and Claude demonstrate strong reasoning capabilities but often suffer from **high inference latency**, making them less suitable for real-time applications.

This project provides a **lightweight, experimental benchmark** to measure how fast and how accurately such systems respond to visual queries.

---

## 🎯 Objectives

- Evaluate **latency vs reasoning trade-offs**
- Measure **end-to-end performance of multimodal agents**
- Provide a **simple benchmarking framework**
- Simulate **real-world decision-making scenarios**

---

## 🏗️ System Architecture
        ┌────────────────────┐
        │    Input Image     │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │ Vision Module      │
        │ (Image Captioning) │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │ Caption Output     │
        └─────────┬──────────┘
                  │
    ┌─────────────▼─────────────┐
    │ Combine with User Query   │
    └─────────────┬─────────────┘
                  │
        ┌─────────▼──────────┐
        │ Language Model     │
        │ (Reasoning Engine) │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │ Generated Answer   │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │ Evaluation Module  │
        │ Latency + Accuracy │
        └────────────────────┘
        
---

## ⚙️ How It Works

1. An image is passed into a vision model (BLIP) to generate a caption  
2. The caption is combined with a user question  
3. A language model generates a response  
4. The system measures:
   - ⏱️ Latency (processing time)
   - 🎯 Accuracy (basic match with ground truth)

---

## 📊 Evaluation Metrics

| Metric | Description |
|------|-------------|
| ⏱️ Latency | Time taken from input → response |
| 🎯 Accuracy | Whether answer matches expected output |
| 🧠 Reasoning | Based on contextual correctness |
| ❌ Hallucination | Incorrect or unsupported outputs |

---

## 📂 Project Structure
fastvlm-agent-benchmark/
│── main.py
│── evaluator.py
│── dataset.json
│── utils.py
│── requirements.txt
│── README.md


---

## 📦 Installation

```bash
pip install -r requirements.txt

Running the Project:
python main.py

Dataset

The dataset consists of simple image-question pairs:
{
  "image": "image1.jpg",
  "question": "What is in the image?",
  "answer": "car"
}

🧪 Example Output:
Question: What is in the image?
Predicted: A car is parked on the street.
Latency: 0.82 seconds

🚀 Key Contributions
✅ Prototype multimodal agent pipeline
✅ Latency-aware evaluation system
✅ Simple benchmark for vision-language tasks
✅ Foundation for real-world agent evaluation
🔬 Future Work
Add advanced multimodal models (LLaVA, BLIP-2)
Improve reasoning evaluation metrics
Introduce adaptive model routing
Expand dataset with real-world scenarios
Add visualization dashboards
🧠 Research Motivation

This project is part of a broader effort to build evaluation infrastructure for next-generation multimodal AI agents, focusing on:

Real-time performance
Reliability
Decision-making under constraints
👩‍💻 Author

Rashmi Thimmaraju

⭐ Acknowledgment

This project is developed as part of a research exploration into multimodal AI systems and evaluation frameworks.


