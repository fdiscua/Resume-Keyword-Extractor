# Resume Keyword Extractor

An AI-powered tool that extracts and highlights the most important keywords from a resume by comparing it with a job description. This project showcases skills in **NLP**, **text processing**, **TF-IDF**, and **web development** using **Streamlit**.

![image](https://github.com/user-attachments/assets/dfce3ac9-4031-45db-abab-386182c13649)


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Overview

The Resume Keyword Extractor allows users to upload a PDF resume and enter a job description. The tool then processes the resume, extracts text, and uses **TF-IDF** to determine the top matching keywords relevant to the job description. This can help job seekers tailor their resumes to better fit the requirements of their target positions.

## Features

- **PDF Text Extraction**: Automatically extracts text from PDF resumes.
- **Text Preprocessing**: Cleans and normalizes text by removing stopwords and special characters.
- **Keyword Extraction**: Uses TF-IDF to extract the top matching keywords based on a provided job description.
- **Web Interface**: A simple and interactive web application built with Streamlit.
- **Match Tips**: Provides users with suggestions to optimize their resumes by including the identified keywords.

## Tech Stack

- **Python**: Programming language used for development.
- **NLTK**: For text preprocessing and stopword removal.
- **Scikit-Learn**: Implements TF-IDF for keyword extraction.
- **PyPDF2**: Extracts text from PDF files.
- **Streamlit**: Creates the web interface for the application.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/resume-keyword-extractor.git
   cd resume-keyword-extractor
