# 🩺 AIcura - Your AI Health Assistant

AIcura is a simple, locally running AI health assistant that lets you input your symptoms (with optional image upload) and receive a natural-sounding diagnosis response from a powerful AI model, along with spoken audio.

> ⚠️ Disclaimer: This is a learning/experimental tool and not a replacement for real medical advice.

---

## 💡 Features

- Text-based symptom input
- Optional image upload 
- AI-generated doctor-style diagnosis
- Audio response via text-to-speech
- Clean and simple web UI using Gradio

---

## 🚀 Setup Instructions

### 1. Clone the repo

git clone https://github.com/Satya19112003/AIcure.git
cd AIcura

### 2. Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Set up your environment variables

Create a `.env` file in the root directory:

GROQ_API_KEY=your_groq_api_key_here

> 🔐 You can get your GROQ API key from https://console.groq.com

---

## ▶️ Run the App

python app.py

The Gradio UI will launch at http://127.0.0.1:7860 in your browser.

---

## 🧪 Example Usage

1. Enter your symptoms in the text box.  
2. Optionally upload an image (e.g., rash, skin mark).  
3. Get a short, natural response mimicking a doctor.  
4. Play the audio version of the response.

---

## 📌 Technologies Used

- Python 3.10+
- Gradio – UI
- Groq – LLM API
- gTTS – Text to Speech
- Pillow – Image handling

--

## 🤝 Contributing

Pull requests are welcome! If you'd like to improve the UI or add new features, feel free to fork this project.

---

## 📄 License

This project is for educational purposes only and is not intended for clinical use.
