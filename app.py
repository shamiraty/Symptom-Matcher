from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel

app = Flask(__name__)

# Sample Patient Data /use this when in localhost
df = pd.read_csv("patient_conditions.csv")

# un-comment this  when online  otherwise use MYSQL
#df = pd.DataFrame(data)

# Function to Recommend Similar Patients
def recommend_patients(selected_id, top_n=10):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["disease"] + " " + df["symptoms"])
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    patient_idx = df[df["id"] == selected_id].index[0]
    scores = list(enumerate(similarity_matrix[patient_idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
    recommended_patients = [df.iloc[i[0]].to_dict() for i in scores]
    return recommended_patients

# Function to Categorize Patients Based on Doctor Comments
def categorize_patients():
    texts = [comment.split() for comment in df["doctor_comment"]]
    dictionary = Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    lda_model = LdaModel(corpus, num_topics=10, id2word=dictionary, passes=10)
    topic_assignments = [max(lda_model.get_document_topics(corpus[i]), key=lambda x: x[1])[0] for i in range(len(corpus))]
    
    df["category"] = topic_assignments
    return df[["id", "doctor_comment", "category"]]

@app.route('/')
def index():
    categorized_df = categorize_patients()
    return render_template('index.html', patients=df.to_dict(orient='records'), categorized_patients=categorized_df.to_dict(orient='records'))

@app.route('/recommend/<int:patient_id>')
def recommend(patient_id):
    recommendations = recommend_patients(patient_id)
    selected_patient_category = df[df["id"] == patient_id]["category"].values[0]
    same_category_patients = df[df["category"] == selected_patient_category].to_dict(orient='records')

    return jsonify({"recommendations": recommendations, "same_category": same_category_patients})

if __name__ == '__main__':
    app.run(debug=True)
