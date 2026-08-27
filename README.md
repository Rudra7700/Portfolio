<<<<<<< HEAD
# Portfolio
This is my first website
=======
# Rudrasis Panda - AI/ML Portfolio

A modern, responsive portfolio website showcasing Rudrasis Panda's skills, projects, and experience in AI & Machine Learning.

## Features

- **Modern Dashboard Design**: Clean, professional interface with dark theme
- **Interactive Chatbot**: AI-powered assistant that answers questions about the resume
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile devices
- **Skill Showcase**: Displays technical skills and project experience
- **Contact Information**: Easy access to contact details and social links

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **AI/ML**: Groq API for chatbot functionality
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)

## Deployment

This portfolio is configured for deployment on Render.com.

### Prerequisites

1. **Groq API Key**: Get your API key from [Groq Console](https://console.groq.com/keys)
2. **Render Account**: Sign up at [Render](https://render.com)

### Deployment Steps

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Ready for Render deployment"
   git push origin main
   ```

2. **Deploy on Render**:
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will automatically detect the `render.yaml` configuration
   - Add your `GROQ_API_KEY` as an environment variable
   - Click "Create Web Service"

3. **Environment Variables**:
   Set these in your Render dashboard:
   - `GROQ_API_KEY`: Your Groq API key
   - `FLASK_ENV`: production (auto-set)
   - `FLASK_DEBUG`: false (auto-set)
   - `PORT`: 10000 (auto-set)

### Local Development

1. **Clone and Setup**:
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Create Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY
   ```

5. **Run Locally**:
   ```bash
   python app.py
   ```

   Visit `http://localhost:5000` to view the portfolio.

## Project Structure

```
portfolio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment configuration
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore file
├── static/
│   ├── style.css        # Main stylesheet
│   └── chat.js          # Chatbot functionality
├── templates/
│   └── index.html       # Main HTML template
└── README.md            # This file
```

## Security Features

- Environment variable management for API keys
- Input validation and sanitization
- Error handling without exposing sensitive information
- Production-ready configuration with debug mode disabled

## Customization

To customize this portfolio for your own use:

1. Update the `RESUME_CONTEXT` in `app.py` with your information
2. Modify the content in `templates/index.html`
3. Adjust styling in `static/style.css`
4. Update contact information and social links
5. Replace the profile image placeholder

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

- **Email**: RUDRASIS.PANDA.CSE-AIML.2024@NIST.EDU
- **GitHub**: https://github.com/Rudra7700
- **Phone**: 9078261804
>>>>>>> f918528 (Configure portfolio web app for Render deployment)
