# Agentic Financial-RAG: Production-Grade Modular AI System

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Framework: LangGraph](https://img.shields.io/badge/Framework-LangGraph-orange.svg)](https://github.com/langchain-ai/langgraph)
[![Tooling: UV](https://img.shields.io/badge/Tooling-UV-brightgreen.svg)](https://github.com/astral-sh/uv)

## 🚀 Overview
This repository contains a production-grade **Retrieval-Augmented Generation (RAG)** system designed for high-stakes financial document analysis. 

Moving beyond basic "linear" RAG, this project implements an **Agentic Workflow** using **LangGraph**. The system doesn't just retrieve and answer; it evaluates the quality of retrieved context and uses state-driven logic to ensure accuracy, transparency, and reliability—critical requirements for financial risk analytics.

## ✨ Key Features
- **Agentic Orchestration:** Built with **LangGraph** to manage complex, cyclic AI workflows.
- **Semantic Chunking:** Advanced document processing that splits text based on meaning and context rather than arbitrary character limits.
- **Production-Grade Modular Architecture:** Separates concerns into `ingestion`, `retrieval`, `generation`, and `state` modules for maximum maintainability.
- **Modern Python Tooling:** Uses **UV** for lightning-fast, reproducible dependency management.
- **Source Transparency:** Interactive UI built with **Streamlit** that displays retrieved source segments alongside the generated answer to mitigate hallucinations.

## 🛠️ Tech Stack
- **AI Frameworks:** LangGraph, LangChain
- **LLM Orchestration:** OpenAI (GPT-4o) / Anthropic (Claude 3.5)
- **Vector Database:** ChromaDB / Pinecone
- **Package Management:** [uv](https://github.com/astral-sh/uv)
- **Frontend:** Streamlit
- **Document Processing:** PyMuPDF, Semantic Linker

## 📐 System Architecture
The system follows a modular pipeline designed for scalability:

1. **Ingestion Module:** Extracts data from PDFs, applies Semantic Chunking, and generates high-dimensional embeddings.
2. **Retrieval Node:** Performs a similarity search against the Vector Store.
3. **Evaluation Logic (Agentic):** A dedicated node evaluates if the retrieved context is sufficient to answer the query. If not, it can trigger a refined search.
4. **Generation Node:** Uses a "Chain-of-Thought" prompt to synthesize a final answer with citations.



## 📦 Getting Started

### Prerequisites
Install `uv` (the fastest Python package manager):
```bash
curl -LsSf https://astral-sh/uv/install.sh | sh