from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("best_model.pkl","rb"))
symptom_columns = pickle.load(open("symptom_columns.pkl","rb"))

# normalize human text → dataset format
def normalize(symptoms):
    cleaned=[]
    for s in symptoms:
        s=s.strip().lower()
        s=s.replace(" ","_")
        s=s.replace("-","_")
        cleaned.append(s)
    return cleaned

# prediction logic
def predict_disease(user_symptoms):
    input_data=[0]*len(symptom_columns)

    for symptom in user_symptoms:
        if symptom in symptom_columns:
            index=symptom_columns.index(symptom)
            input_data[index]=1

    return model.predict([input_data])[0]

@app.route('/')
def home():
    return render_template("index.html")

# API endpoint
@app.route('/predict',methods=['POST'])
def predict():
    data=request.get_json()
    symptoms=data["symptoms"].split(',')
    symptoms=normalize(symptoms)

    result=predict_disease(symptoms)
    return jsonify({"prediction":result})

if __name__=="__main__":
    app.run(debug=True)
