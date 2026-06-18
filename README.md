# 🎬 CineSense – AI Powered Movie Review Analytics

## 📌 Overview

CineSense is a Streamlit-based web application that allows users to search for movies, view detailed information, and analyze movie reviews using Machine Learning. The application integrates with the TMDB (The Movie Database) API to fetch real-time movie information and uses Natural Language Processing (NLP) techniques to classify user reviews as positive or negative.

This project demonstrates the integration of APIs, Machine Learning, Data Analysis, and Interactive Web Development in a single application.

---

## ✨ Features

### 🎥 Movie Search

* Search movies using TMDB API
* Display movie posters
* View movie overview and release date
* Show TMDB ratings and popularity scores

### 🤖 Sentiment Analysis

* Analyze custom movie reviews
* Classify reviews as:

  * Positive 😊
  * Negative 😞
* Display confidence score for predictions

### 🎯 Movie Recommendations

* Fetch recommended movies from TMDB
* Display movie posters and titles
* Improve user movie discovery experience

### 📊 Interactive Dashboard

* Modern Netflix-style user interface
* Sidebar navigation
* Real-time API integration
* Responsive layout

---

## 🛠️ Technologies Used

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Backend Logic             |
| Streamlit         | Web Application Framework |
| TMDB API          | Movie Data Retrieval      |
| Scikit-Learn      | Machine Learning          |
| TF-IDF Vectorizer | Text Feature Extraction   |
| Naive Bayes       | Sentiment Classification  |
| Requests          | API Communication         |

---

## 📂 Project Structure

```text
CineSense/
│
├── app.py
├── requirements.txt
├── README.md
└── assets/
    └── logo.png
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/CineSense.git
cd CineSense
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 TMDB API Setup

1. Create an account on TMDB.
2. Generate an API Key.
3. Open `app.py`.
4. Replace:

```python
API_KEY = "YOUR_TMDB_API_KEY"
```

with your TMDB API key:

```python
API_KEY = "YOUR_API_KEY"
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 🧠 Machine Learning Workflow

### Data Processing

1. User enters a movie review.
2. Review is transformed into numerical vectors using TF-IDF.
3. Features are passed to a Naive Bayes classifier.
4. Model predicts sentiment.
5. Confidence score is displayed.

### Sentiment Classes

| Label    | Meaning     |
| -------- | ----------- |
| Positive | Good Review |
| Negative | Bad Review  |

---

## 🎯 Future Enhancements

* IMDb 50K Dataset Training
* Deep Learning Sentiment Model (LSTM/BERT)
* Review Summarization
* Word Cloud Visualization
* User Authentication
* Watchlist Management
* Genre-Based Recommendations
* Analytics Dashboard with Plotly
* Multi-Language Review Analysis

---

## 📸 Screenshots

Add screenshots of:

* Home Page
* Movie Search Results
* Review Sentiment Analysis
* Recommendation Section

---

## 📈 Learning Outcomes

This project demonstrates:

* API Integration
* Machine Learning Fundamentals
* Natural Language Processing
* Streamlit Development
* Data Visualization
* Software Project Design

---

## 👨‍💻 Author

**Rithik S**

B.Tech – Artificial Intelligence and Data Science

Karpagam Institute of Technology

Email: [rithik4594@gmail.com](mailto:rithik4594@gmail.com)

GitHub: https://github.com/yourusername

---

## 📜 License

This project is developed for educational and learning purposes.
