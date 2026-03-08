👨‍💻 Team :

Team ID : SWTID-2026-1741

Team Size : 5

Team Leader : AKASH S K (6079@velsrscollege.com)

Team member : TAMILARASAN M

Team member : MADHUMITHA M

Team member : SAJITHA R

Team member : AKSHAYA S


________________________________________
🌿 Leaf Health Check
Turn simple leaf images into actionable plant health insights using AI-powered image analysis.
The system detects damaged areas on plant leaves, estimates severity, and provides helpful rescue recommendations to assist farmers, gardeners, and plant enthusiasts.
________________________________________
🚀 Features
Leaf Image Upload: Upload plant leaf images directly through the web interface.
Damage Detection: Uses image processing techniques to detect discoloration and damaged regions on leaves.
Severity Analysis: Calculates the percentage of affected area and classifies plant health status.
AI Diagnosis: Uses Google's Gemini AI to provide possible disease explanations and treatment suggestions.
Plant Care Recommendations: Provides useful tips to recover and maintain plant health.
Downloadable Report: Generate and download a plant health report instantly.
________________________________________
🏗 Architecture
The project follows a modular Python architecture using Streamlit for the web interface.
Frontend / Application Layer
•	Streamlit UI (app.py)
Backend Processing Modules
•	image_processing.py – Leaf preprocessing and damaged area detection
•	severity.py – Severity classification logic
•	recommendation.py – Plant care suggestions
•	ai_diagnosis.py – Gemini AI integration
AI Pipeline
•	OpenCV (Image processing and damage detection)
•	NumPy (Numerical operations)
•	Gemini AI (Diagnosis and explanation generation)
________________________________________
💻 Getting Started
Prerequisites
•	Python 3.9+
•	Streamlit
•	OpenCV
•	NumPy
•	Pillow
•	A Google Gemini API Key
________________________________________
⚙ Installation
Clone the repository
git clone https://github.com/6079-collab/AI-PROJECT.git
cd Leaf-Health-Check
Install dependencies
pip install -r requirements.txt
________________________________________
▶ Run the Application
Start the Streamlit application
streamlit run app.py
The application will automatically open in your browser.
________________________________________
📊 How It Works
1.	User uploads a leaf image
2.	Image preprocessing is applied using OpenCV
3.	Damaged regions are detected
4.	Percentage of affected area is calculated
5.	Severity level is classified
6.	Gemini AI generates diagnosis and suggestions
7.	Results and recommendations are displayed
________________________________________
🌱 Example Output
The system generates:
•	Leaf preview
•	Percentage of affected area
•	Severity classification
•	AI diagnosis
•	Rescue recommendations
•	Downloadable health report
________________________________________
🎯 Use Cases
•	Smart agriculture assistance
•	Plant disease monitoring
•	Gardening support tools
•	AI-powered agricultural research
•	Educational AI projects
________________________________________
🔮 Future Improvements
•	Deep learning based plant disease detection
•	Real-time camera scanning
•	Multiple crop disease dataset integration
•	Mobile application support
•	Cloud deployment
________________________________________
🛡 License
This project is developed for educational purposes under the Naan Mudhalvan AI program.


