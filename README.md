# Language Translation Tool

## Overview
A web based tool for translating text between multiple languages and converting the output into speech. It uses AI powered translation tool and text-to-speech services to provide both readable and audible results. The application supports automatic language detection, manual language selection, and real time interaction through a simple browser interface.

---
## Features
- Translate text between multiple languages
- Automatic language detection of input text
- Manual selection of source and target languages
- Text-to-Speech (TTS) for audible outputs
- Interaction through web interface
- Character limit handling for input validation
- Copy translated text to clipboard

---
## Technologies Used
- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Translation: deep-translator (Google Translate)
- Text-to-Speech: gTTS (Google Text-to-Speech)
- Data Handling: Base64 encoding for audio transfer

---
## Project Structure
```
Language_Translation_Tool/
│
├── services/
│   ├── __init__.py
│   ├── translate_service.py  # handles text translation
│   └── tts_service.py        # handles text-to-speech
│
├── templates/
│   └── index.html            # main user interface
│
├── static/
│   ├── script.js             # handles UI logic and API calls
│   └── style.css             # styling for the application
│
├── app.py                    # main Flask application
├── requirements.txt
├── .gitignore
└── README.md
```

---
## Installation

1. Clone the repository
```
git clone https://github.com/Hemal-Patil/CodeAlpha_Language_Translation_Tool
cd Language_Translation_Tool
```

2. Create and activate virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the application:
```
python app.py
```

---
## Usage
1. Open your browser and go to: `https://127.0.0.1:5000/`
2. Enter the text you want to translate.
3. Select source and target languages (or use auto-detect for source language).
4. Click **Translate** to get the translated output.
5. Use the **Speak** option to hear the text.
6. Copy the translated text if needed.

---
## How it works
The project leverages AI services for translation and speech synthesis:
1. Translation
   - Input text is sent to `translate_service.py`
   - Uses deep-translator (Google Translate API wrapper) to convert text between source and target languages.
   - Returns translated text as JSON.
2. Text-to-Speech (TTS)
   - `tts_service.py` receives text and language.
   - Uses gTTS to generate speech audio in memory.
   - Converts audio to Base64 for frontend playback.

---
