# Podcast Studio Project

# Overview
The Podcast Studio Project is an automated AI pipeline designed to generate podcast-style audio content. This application scrapes relevant data, processes it using Large Language Models (LLMs) to generate scripts, and utilizes Text-to-Speech (TTS) technology to output high-quality audio files. 

# Key Features
Data Scraping:- Automatically extracts relevant text and data from targeted web sources using (`scraper.py`).
AI Script Generation:- Uses LLMs to clean, format, and transform raw text into engaging podcast scripts using (`llm_utils.py`).
Text-to-Speech (TTS) Integration:- Converts the final script into natural-sounding audio, producing MP3 outputs using (`tts_utils.py`)
Streamlined Pipeline:- Using a unified architecture (`pipeline.py`) that handles the end-to-end process from text acquisition to audio generation.

# Project Structure
* `app.py` - The main application entry point.
* `pipeline.py` - Manages the end-to-end flow of data between scraping, text generation, and audio generation.
* `scraper.py` - Handles web scraping and data gathering.
* `llm_utils.py` - Contains the logic for interacting with Large Language Models.
* `tts_utils.py` - Manages the text-to-speech audio generation.
* `utils.py` - Helper functions used across the project.
* `.env` - Environment variables (API keys) needed to run the LLMs and TTS services *(Note: This file is ignored by Git for security)*.

#  Getting Started

# Prerequisites
1. Ensure you have Python installed. It is highly recommended to use a virtual environment to avoid package conflicts.

2. Ensure u clone the repository:
   ```bash
   git clone https://github.com/JeweAbiodun-sketch/Podcas_Studio_Project_1.git
   cd Podcas_Studio_Project_1

   To test run the app you can use any of the url saved in the file named (url link) in the project folder