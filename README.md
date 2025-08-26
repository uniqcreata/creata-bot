# Creata-Bot 🤖

Creata-Bot is a Flask-based Bybit trading assistant that connects to the Bybit API and automates certain trading tasks.  
It is deployed using Render for easy scalability and availability.

## 🚀 Features
- Connects to Bybit API securely
- Handles real-time trading signals
- Uses Flask backend for webhooks & dashboard
- Deployed automatically with Render
- Easy to extend and customize

## 📂 Project Structure
app.py              # Main Flask application
requirements.txt    # Python dependencies
render.yaml         # Render deployment config
runtime.txt         # Python version for Render
Procfile            # Process manager for Render
templates/          # HTML templates (Flask)
README.md           # Project documentation
venv/               # Virtual environment (ignored)

## ⚙️ Setup & Installation

1. Clone the repository
   git clone https://github.com/uniqcreata/creata-bot.git
   cd creata-bot

2. Create and activate virtual environment
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

3. Install dependencies
   pip install -r requirements.txt

4. Run locally
   python app.py
   Open in browser: http://127.0.0.1:5000

## 🚀 Deployment
Creata-Bot is deployed on Render.  
Deployment is handled by the render.yaml file, so updates are automatic when pushing to the main branch.

## 🔒 Environment Variables
Create a .env file with the following:
BYBIT_API_KEY=your_api_key_here
BYBIT_API_SECRET=your_api_secret_here

## 🛠️ Requirements
- Python 3.9+
- Flask
- Requests
- WebSockets
- Bybit
- Python-dotenv

## 📜 License
This project is licensed under the MIT License – feel free to use and modify.

## 👨‍💻 Author
Built with ❤️ by uniqcreata
