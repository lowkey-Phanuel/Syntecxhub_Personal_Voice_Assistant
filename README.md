# Syntecxhub_Personal_Voice_Assistant

A rule-based Personal Voice Assistant built in Python for **Syntecxhub Artificial Intelligence Internship — Task 4 (Project 1)**.

## Features
- **Speech-to-Text (STT):** Captures voice input with SpeechRecognition and includes a text input fallback when no microphone or PyAudio is available.
- **Rule-Based Command Mapping:** Routes commands in commands.py for time, date, opening websites, launching apps, web searches, and Wikipedia summaries.
- **Text-to-Speech (TTS):** Speaks responses aloud using pyttsx3.
- **Error Handling:** Handles timeouts, unrecognized input, network issues, and missing applications gracefully.

## Sample Commands
- What time is it?
- What is today's date?
- Open YouTube / Open GitHub
- Open calculator / Open notepad
- Search for Python
- Who is Alan Turing?
- Exit
