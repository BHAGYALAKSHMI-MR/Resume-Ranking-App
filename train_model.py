
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample data (dummy resumes and job descriptions)
X = [
    "Experienced Python developer with ML skills.",
    "Data scientist with strong background in NLP.",
    "Machine learning engineer with cloud deployment experience."
]
y = [1, 1, 0]  # Labels: 1 for match, 0 for not match

# Vectorization and model training
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

# Save model and vectorizer
joblib.dump(model, "model/resume_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")
