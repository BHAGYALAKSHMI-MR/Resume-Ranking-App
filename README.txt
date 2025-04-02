# 🧠 Resume Ranking App

A Django-based web application that ranks resumes by comparing them to a given job description using NLP and machine learning techniques.

## 🚀 Features

- Input job description and multiple resumes
- Use TF-IDF + Cosine Similarity to score resumes
- Ranks resumes based on relevance
- Clean web interface built with Django
- Train and save your own ML model

## 🛠️ Tech Stack

- Python
- Django
- scikit-learn
- NumPy
- joblib

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BHAGYALAKSHMI-MR/Resume-Ranking-App.git
cd Resume-Ranking-App
```

### 2. Create Virtual Environment and Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate         # On Windows
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Train the Model (Optional)

```bash
python train_model.py
```

### 5. Run the App

```bash
python manage.py runserver
```

Go to `http://127.0.0.1:8000/` in your browser.

---

## 💡 How It Works

- Resumes and job description are vectorized using **TF-IDF**
- Cosine similarity is used to measure match
- Results are ranked and displayed on the web UI

---

## 📁 Project Structure

```
Resume-Ranking-App/
├── resumeranker/               # Django app
├── templates/                  # HTML templates
├── static/                     # CSS, JS
├── train_model.py              # Model training script
├── model/                      # Trained ML model
├── requirements.txt
├── manage.py
```

---

## 📌 Future Enhancements

- Support PDF/DOCX resume uploads
- Named Entity Recognition (NER) for advanced parsing
- Admin dashboard to manage job descriptions and scores
- Deploy to Render or Heroku

---

## 📄 License

MIT License

---

> Created with ❤️ using Python & Django
