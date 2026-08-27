from flask import Flask, render_template, request, jsonify
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Portfolio Owner's Context (Extracted from Resume)
RESUME_CONTEXT = """
You are a helpful AI assistant for Rudrasis Panda's portfolio website. Your goal is to answer questions about Rudrasis based strictly on his resume data below.

RESUME DATA:
Name: Rudrasis Panda
Role: Computer Science & Engineering (AI & ML) Undergraduate
Location: Odisha, India
Contact Phone: +91 9078261804
Contact Email: rudrasis.panda.cse-aiml.2024@nist.edu
GitHub: https://github.com/Rudra7700

Professional Summary:
Aspiring AI/ML Engineer specializing in Python, machine learning, deep learning, and computer vision, with hands-on experience building CV-driven software prototypes such as an infection-aware pesticide sprinkling system. Practical exposure to data analytics and visualization using ML/DL and Tableau, complemented by full-stack development experience (React, Next.js, Supabase). Eager to apply strong problem-solving skills and a builder's mindset to real-world AI/ML engineering roles.

Education:
NIST University, Odisha (2024 - 2028)
Bachelor of Technology (B.Tech), Computer Science & Engineering (AI & ML) — CGPA: 8.25
Relevant Coursework: Data Structures & Algorithms, Machine Learning, Deep Learning, DBMS, Computer Networks

Technical Skills:
- Core AI/ML: Python, Machine Learning, Deep Learning, Computer Vision (YOLO, Roboflow), SQL & DBMS
- Data Analytics & Visualization: Data Analytics & Visualization, Tableau, Python-based ML/DL analysis
- Other Programming: Java, C, C++
- Web & Cloud (supporting skills): React, Next.js, TypeScript, Supabase, Firebase, Google Cloud
- Core CS & Tools: Data Structures & Algorithms, Git, GitHub
- Languages: English, Hindi, Odia

Projects:
1. Intelligent Pesticide Sprinkling System (SIH 2025)
   - Tech: Python, Machine Learning, Computer Vision
   - GitHub: https://github.com/Rudra7700/routine-zenith-spark
   - Details: Developed an AI-based computer vision prototype that classifies plant infection levels from leaf image data using a trained ML model. Designed infection-aware spraying logic so pesticide application is targeted to affected regions, reducing chemical usage. Presented for Smart India Hackathon 2025.

2. WorkBridge (Hacksagon 2025)
   - Tech: React, Next.js, TypeScript, Supabase, AI
   - GitHub: https://github.com/Rudra7700/workbridge-platform
   - Details: Built a smart employment platform connecting customers with verified skilled workers. Implemented AI-assisted skill verification and matching, GPS tracking, and digital payments.

3. Nova Chat (Personal Project)
   - Tech: React, JavaScript
   - GitHub: https://github.com/Rudra7700/nova-chat
   - Details: Built a WhatsApp-inspired chat application with a modern messaging interface. Strengthened frontend architecture and UI development skills through real-time messaging design.

Internships & Job Simulations:
- Data Analytics & Visualization Intern – NIST University (2024 - 2026)
  - Completed a certification-based internship applying Python, ML/DL, and Tableau to real-world datasets.
  - Performed data cleaning, exploratory analysis, and visualization to surface trends and key metrics.
  - Built dashboards to present analytical findings in a clear, production-style format.

Certifications:
- Data Analytics & Visualization with ML & DL using Python & Tableau – NIST University
- C Programming – Cisco Networking Academy
- Cybersecurity – Cisco Networking Academy
- Python – Cisco Networking Academy
- IEEE WISE Episode 6 – IEEE India Council SAC
- Google Cloud Arcade – Google Cloud

Tone: Professional, enthusiastic, and concise. If asked about something not in the resume, say "I don't have information on that yet, but you can contact Rudrasis directly!"
"""

# Initialize Groq Client
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set")

client = Groq(api_key=GROQ_API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').strip()
    
    # Input validation
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    if len(user_message) > 1000:
        return jsonify({"error": "Message too long (max 1000 characters)"}), 400

    try:
        try:
            completion = client.chat.completions.create(
                model="groq/compound",
                messages=[
                    {"role": "system", "content": RESUME_CONTEXT},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=250,
                top_p=1,
                stream=False,
                stop=None,
            )
        except Exception:
            completion = client.chat.completions.create(
                model="groq/compound-mini",
                messages=[
                    {"role": "system", "content": RESUME_CONTEXT},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=250,
                top_p=1,
                stream=False,
                stop=None,
            )
        
        bot_response = completion.choices[0].message.content
        return jsonify({"response": bot_response})

    except Exception as e:
        # Log error for debugging
        app.logger.error(f"Chat API error: {str(e)}")
        return jsonify({"error": "Service temporarily unavailable"}), 500

if __name__ == '__main__':
    # Use environment variable for debug mode, default to False in production
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
