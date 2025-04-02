
import os
import joblib
from django.shortcuts import render
from .forms import ResumeForm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the model
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'resume_model.pkl')
model = joblib.load(model_path)

# Dummy training data for vectorizer (in real project, load from training)
sample_data = [
    "Looking for a Python developer with ML and NLP knowledge.",
    "Need an experienced Data Scientist with Python and AI background.",
    "Seeking a Machine Learning engineer with cloud deployment experience."
]
vectorizer = TfidfVectorizer()
vectorizer.fit(sample_data)

def index(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume_text = form.cleaned_data['resume_text']
            jd_text = sample_data[0]  # Use first JD as default match
            resume_vec = vectorizer.transform([resume_text])
            jd_vec = vectorizer.transform([jd_text])
            score = cosine_similarity(resume_vec, jd_vec)[0][0]
            return render(request, 'resumeranker/result.html', {'result': f'Match Score: {score:.2f}'})
    else:
        form = ResumeForm()
    return render(request, 'resumeranker/index.html', {'form': form})
