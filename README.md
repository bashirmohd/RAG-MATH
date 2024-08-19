# RAG-MATH

This repository implements a Retrieval-Augmented Generation (RAG) system designed to query a PDF document and answer questions based solely on the content of the document. The system is particularly adept at handling mathematical equations, ensuring that answers are both accurate and contextually relevant.

## Table of Contents- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
  - [vectorstore.py](https://github.com/abdull6771/RAG-MATH/blob/main/vectorstore.py)
  - [retriever.py](https://github.com/abdull6771/RAG-MATH/blob/main/retriever.py)
  - [template.py](https://github.com/abdull6771/RAG-MATH/blob/main/template.py)
  - [llm.py](https://github.com/abdull6771/RAG-MATH/blob/main/llm.py)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project leverages the `langchain` and `Chroma` libraries, along with an OpenAI-based language model, to create a Q/A system that retrieves relevant information from a PDF document. The system is especially useful for documents containing mathematical content, as it can parse and interpret equations.

## Features-**PDF Content Retrieval**: Efficiently retrieves the most relevant sections from a PDF document.
-**Mathematical Equation Handling**: Accurately interprets and includes mathematical equations in responses.
-**Prompt Engineering**: Utilizes a custom template to structure the language model's responses.
-**Modular Design**: Components are modularized for easier customization and maintenance.

## Installation1.**Clone the repository:**```bash
   git clone https://github.com/abdull6771/RAG-MATH.git
   cd RAG-MATH