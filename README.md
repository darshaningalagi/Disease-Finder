# AI Disease Prediction Chatbot

An AI-based disease prediction system built using Flask and Random Forest.  
Users enter symptoms in a chatbot-style interface and the system predicts a possible disease based on trained machine learning logic.

---

## Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- Tailwind CSS

---

## How It Works

1. User enters symptoms separated by commas.
2. Input is normalized (spaces and hyphens converted to underscores).
3. Symptoms are converted into a feature vector.
4. A trained Random Forest model predicts the disease.
5. The result is displayed in a chatbot interface.

---

## Diseases Supported

The model is trained on 10 diseases:

- Fungal Infection  
- Allergy  
- GERD  
- Chronic Cholestasis  
- Drug Reaction  
- Peptic Ulcer Disease  
- Dengue  
- Typhoid  
- Diabetes  
- Hypertension  

---



## Installation

Clone the repository:
git clone https://github.com/darshaningalagi/Disease-Finder.git

cd Disease-Finder

Install dependencies:
pip install -r requirements.txt


Run the application:
python app.py

Open in browser:
ex: http://127.0.0.1:5000



---

## Model Information

- Algorithm: Random Forest Classifier
- Dataset: Synthetic disease-symptom dataset
- Accuracy: ~98% on generated test split

Note: This project uses synthetic training data for academic purposes.  
It is not intended for real medical diagnosis.

---

## Future Improvements

- Integration with real medical datasets
- Confidence score display
- Symptom auto-suggestions
- Cloud deployment
- Model performance visualization

---

## Disclaimer

This project is for educational and demonstration purposes only.  
Do not use it for real medical decision making.