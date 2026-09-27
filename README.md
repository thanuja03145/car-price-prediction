
# 🚗 Automotive Intelligence & Used Car Price Prediction Platform

An end-to-end, multi-modal AI platform designed for used car price valuation, 5-year financial forecasting, vehicle visual condition diagnostics, and traffic intelligence via an integrated AI voice assistant.

---

## 👤 Developer Profile
* **Developer:** Thanuja K
* **Domain:** Artificial Intelligence & Data Science Engineering (3rd Year Project)

---

## 🌟 Key Features

* **🎯 Price Prediction (DNN Regression):** Estimates accurate used car resale prices based on 12 vehicle attributes using Deep Learning models.
* **📉 Financial Forecast:** Computes 5-year vehicle depreciation and projects annual maintenance costs.
* **🔍 Model Explainability (XAI):** Visualizes feature importance and impact percentage on predicted prices.
* **📷 AI Vision Assessment:** Analyzes uploaded vehicle photos to evaluate overall vehicle condition and highlight potential defects.
* **🎙️ Automotive AI Voice Assistant:** Supports interactive text and voice queries for district/state-wise traffic density and valuation insights.

---

## 📁 Project Architecture & Folder Structure

```text
├── ml/
│   ├── predictor.py          # DNN Model loading & inference logic
├── financial/
│   ├── depreciation.py       # Depreciation calculation algorithms
│   ├── maintenance.py        # Maintenance cost estimation
│   └── deal_classifier.py    # Fair market deal categorization
├── explainability/
│   └── feature_importance.py # XAI logic for model interpretation
├── vision/
│   └── condition_analyzer.py # Computer Vision diagnostic scripts
├── voice/
│   └── voice_assistant.py    # Voice assistant NLP & query handling
├── app.py                    # Main Streamlit Dashboard Application
├── requirements.txt          # Python dependency requirements
└── README.md                 # Project documentation

----

🛠️ Technology Stack
 * Frontend / UI: Streamlit (Custom Dark UI Architecture)
 * Backend Framework: Python 3.10+
 * Machine Learning / AI: TensorFlow / Keras (DNN), Scikit-Learn
 * Computer Vision: OpenCV / Pillow
 * Data Handling: Pandas, NumPy
 * Voice Integration: JavaScript Web Speech API Integration

---

🚀 How to Install, Run, and Access the App Link
Step 1: How to Install Locally
 * Clone the GitHub repository:
   git clone [https://github.com/thanuja03145/car-price-prediction.git](https://github.com/thanuja03145/car-price-prediction.git)

---

 * Navigate into the project folder:
   cd car-price-prediction
---

 * Create and activate a virtual environment (optional but recommended):
   python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
---

 * Install all required dependencies:
   pip install -r requirements.txt
---

Step 2: How to Run Locally
 * Start the Streamlit server:
   streamlit run app.py
---

 * Open your web browser and navigate to:
   http://localhost:8501
---

Step 3: How to Deploy & Open the Live App Link
 * Go to share.streamlit.io and log in with your GitHub account (thanuja03145).
 * Click Create app -> I already have an app.
 * Select your repository: thanuja03145/car-price-prediction and branch main.
 * Set Main file path to app.py and click Deploy!.
 * Once deployed, open your live project URL in any web browser:
   [https://car-price-prediction.streamlit.app](https://car-price-prediction.streamlit.app)

---

🔗 Project & Live Deployment Links
 * GitHub Repository: https://github.com/thanuja03145/car-price-prediction
 * Live App Link: https://car-price-prediction.streamlit.app
Developed by Thanuja K as a 3rd Year AI & Data Science Engineering Project.

---

### Single Terminal Command to Commit & Push to GitHub:

Paste this single line into your VS Code Terminal and press Enter:

```bash
git add README.md && git commit -m "Complete README with install, run, and app link steps by Thanuja K" && git push origin main
