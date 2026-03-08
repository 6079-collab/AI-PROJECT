TEAM : Team ID : SWTID-2026-1741 Team Size : 5 Team Leader : AKASH S K Team member : TAMILARASAN M Team member : MADHUMITHA M Team member : SAJITHA R Team member : AKSHAYA S
🌿 Leaf Health Check
Turn simple leaf images into actionable plant health insights using AI-powered image analysis. The system detects damaged areas on plant leaves, estimates severity, and provides helpful rescue recommendations to assist farmers, gardeners, and plant enthusiasts.
🚀 Features
Leaf Image Upload: Upload plant leaf images directly through the web interface.
Damage Detection: Uses image processing techniques to detect discoloration and damaged regions on leaves.
Severity Analysis: Calculates the percentage of affected area and classifies plant health status.
AI Diagnosis: Uses Google's Gemini AI to provide possible disease explanations and treatment suggestions.
Plant Care Recommendations: Provides useful tips to recover and maintain plant health.
Downloadable Report: Generate and download a plant health report instantly.
🏗 Architecture
The project follows a modular Python architecture using Streamlit for the web interface.
Frontend / Application Layer
Streamlit UI (app.py)
Backend Processing Modules
image_processing.py – Leaf preprocessing and damaged area detection
severity.py – Severity classification logic
recommendation.py – Plant care suggestions
ai_diagnosis.py – Gemini AI integration
AI Pipeline
OpenCV (Image processing and damage detection)
NumPy (Numerical operations)
Gemini AI (Diagnosis and explanation generation)
💻 Getting Started Prerequisites
Python 3.9+
Streamlit
OpenCV
NumPy
Pillow
A Google Gemini API Key
⚙ Installation
Clone the repository
git clone https://github.com/YOUR_USERNAME/Leaf-Health-Check.git cd Leaf-Health-Check
Install dependencies
pip install -r requirements.txt ▶ Run the Application
Start the Streamlit application
streamlit run app.py
The application will automatically open in your browser.
📊 How It Works
User uploads a leaf image
Image preprocessing is applied using OpenCV
Damaged regions are detected
Percentage of affected area is calculated
Severity level is classified
Gemini AI generates diagnosis and suggestions
Results and recommendations are displayed
🌱 Example Output
The system generates:
Leaf preview
Percentage of affected area
Severity classification
AI diagnosis
Rescue recommendations
Downloadable health report
🎯 Use Cases
Smart agriculture assistance
Plant disease monitoring
Gardening support tools
AI-powered agricultural research
Educational AI projects
🔮 Future Improvements
Deep learning based plant disease detection
Real-time camera scanning
Multiple crop disease dataset integration
Mobile application support
Cloud deployment
🛡 License
This project is developed for educational purposes under the Naan Mudhalvan AI program.

