
## Phoebe – Desktop Voice Assistant

Phoebe is a Python-based voice-controlled desktop assistant that helps automate everyday tasks like opening websites, launching apps, playing music, and checking the time using simple voice commands.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)

---

## Overview

Phoebe is designed to make desktop tasks faster and hands-free. Using speech recognition and text-to-speech, it listens to user commands and executes actions like opening websites, running desktop applications, playing music links, and reporting the current time. The assistant is modular, easy to expand, and ideal for personal productivity automation.

---

## Features

- Voice-activated assistant for desktop tasks  
- Opens popular websites: YouTube, Google, Instagram, WhatsApp, ChatGPT, and more  
- Launches desktop applications like VS Code, Telegram, and Spotify  
- Plays specific music tracks via Spotify links  
- Speaks the current time on request  
- Modular design for easy addition of new commands  

---

## Tech Stack

- **Programming Language:** Python  
- **Libraries:** `speech_recognition`, `pyttsx3`, `webbrowser`, `datetime`, `os`  
- **IDE / Tools:** Jupyter Notebook, VS Code  
- **Platform:** Windows (can be adapted for other OS)  

---

## Installation

1. Clone the repository:  
  (https://github.com/NavinchandSahu/Desktop-Assistant)

2. Navigate to the project folder:
   https://github.com/NavinchandSahu/Desktop-Assistant/blob/main/Desktop-Assistant.py

3. Install dependencies:

For speech recognition
pip install SpeechRecognition
For text-to-speech
pip install pyttsx3
For working with date and time (built-in, no install needed)
datetime is part of Python's standard library
For OS operations (built-in, no install needed)
os is part of Python's standard library
For opening web pages
webbrowser is part of Python's standard library

4. Run the application:

   ```bash
   python app.py
   ```

---

## Usage

1. Launch the assistant by running `app.py`
2. Speak commands clearly after the greeting
3. Examples of commands:

   * "Open YouTube"
   * "Open VS Code"
   * "Play specials"
   * "What is the time?"
4. The assistant will respond and execute the requested action


