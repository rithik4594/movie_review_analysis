import streamlit as st
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# ==========================================
# TMDB API KEY
# ==========================================
API_KEY = "840a421a15c5713b151842"

# ==========================================
# SENTIMENT MODEL
# ==========================================
reviews = [
    "Amazing movie",
    "Excellent acting",
    "Loved this film",
    "Fantastic story",
    "Best movie ever",
    "Wonderful experience",
    "Brilliant screenplay",
    "Outstanding direction",
    "Terrible movie",
    "Worst film",
    "Bad acting",
    "Waste of time",
    "Very boring",
    "Not worth watching",
    "Poor screenplay",
    "Disappointing ending"
]

labels = [
    1,1,1,1,1,1,1,1,
    0,0,0,0,0,0,0,0
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(reviews)

model = MultinomialNB()
model.fit(X, labels)

def predict_sentiment(text):

    text_vec = vectorizer.transform([text])

    prediction = model.predict(text_vec)[0]

    probabilities = model.predict_proba(text_vec)[0]

    confidence = max(probabilities) * 100

    sentiment = "Positive 😊" if prediction == 1 else "Negative 😞"

    return sentiment, confidence

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="CineSense",
    page_icon="🎬",
    layout="wide"
)

# ==========================================
# CSS
# ==========================================
st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#0f172a,
#111827
);
color:white;
}

.main-title{
text-align:center;
font-size:3rem;
font-weight:bold;
color:white;
}

.subtitle{
text-align:center;
color:#d1d5db;
}

.movie-card{
background:#1f2937;
padding:20px;
border-radius:20px;
box-shadow:0px 0px 20px rgba(255,255,255,0.08);
}

.metric-box{
background:#111827;
padding:15px;
border-radius:15px;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:

    st.title("🎥 CineSense")

    st.success("TMDB Connected")

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ Movie Search")
    st.write("✅ Movie Details")
    st.write("✅ Sentiment Analysis")
    st.write("✅ Confidence Score")
    st.write("✅ Recommendations")

    st.markdown("---")

    st.caption("Powered by TMDB + ML")

# ==========================================
# HEADER
# ==========================================
st.markdown(
"""
<h1 class='main-title'>
🎬 CineSense
</h1>
<p class='subtitle'>
AI Powered Movie Review Analytics
</p>
""",
unsafe_allow_html=True
)

st.divider()

# ==========================================
# MOVIE SEARCH
# ==========================================
st.subheader("🔍 Search Movie")

movie_name = st.text_input(
    "Enter Movie Name",
    placeholder="Avatar"
)

if st.button("Search Movie"):

    if movie_name.strip() == "":
        st.warning("Please enter a movie name")

    else:

        search_url = (
            f"https://api.themoviedb.org/3/search/movie"
            f"?api_key={API_KEY}"
            f"&query={movie_name}"
        )

        with st.spinner("Searching movie..."):

            response = requests.get(search_url)

        if response.status_code == 200:

            data = response.json()

            if len(data["results"]) > 0:

                movie = data["results"][0]

                col1, col2 = st.columns([1,2])

                with col1:

                    if movie["poster_path"]:

                        poster_url = (
                            "https://image.tmdb.org/t/p/w500"
                            + movie["poster_path"]
                        )

                        st.image(
                            poster_url,
                            use_container_width=True
                        )

                with col2:

                    st.subheader(movie["title"])

                    st.write(movie["overview"])

                    st.write(
                        f"📅 Release Date: "
                        f"{movie['release_date']}"
                    )

                    c1,c2,c3 = st.columns(3)

                    c1.metric(
                        "⭐ Rating",
                        movie["vote_average"]
                    )

                    c2.metric(
                        "🔥 Popularity",
                        round(movie["popularity"])
                    )

                    c3.metric(
                        "🗳 Votes",
                        movie["vote_count"]
                    )

                # =====================================
                # RECOMMENDATIONS
                # =====================================

                movie_id = movie["id"]

                rec_url = (
                    f"https://api.themoviedb.org/3/movie/"
                    f"{movie_id}/recommendations"
                    f"?api_key={API_KEY}"
                )

                rec_response = requests.get(rec_url)

                if rec_response.status_code == 200:

                    rec_data = rec_response.json()

                    st.divider()

                    st.subheader(
                        "🎯 Recommended Movies"
                    )

                    rec_movies = rec_data["results"][:5]

                    cols = st.columns(5)

                    for i,m in enumerate(rec_movies):

                        with cols[i]:

                            if m["poster_path"]:

                                st.image(
                                    "https://image.tmdb.org/t/p/w500"
                                    + m["poster_path"]
                                )

                            st.caption(m["title"])

            else:
                st.error("Movie not found")

        else:
            st.error("TMDB API Error")

# ==========================================
# REVIEW ANALYSIS
# ==========================================
st.divider()

st.subheader("📝 Review Sentiment Analysis")

review = st.text_area(
    "Write your review",
    height=150,
    placeholder="Type your review here..."
)

if st.button("Analyze Review"):

    if review.strip() == "":
        st.warning("Please enter a review")

    else:

        sentiment, confidence = predict_sentiment(review)

        if "Positive" in sentiment:
            st.success(sentiment)
        else:
            st.error(sentiment)

        st.write("### Confidence Score")

        st.progress(confidence / 100)

        st.info(
            f"{confidence:.2f}% confidence"
        )

# ==========================================
# FOOTER
# ==========================================
st.divider()

st.caption(
    "🎬 CineSense | Powered by TMDB API & Machine Learning"
)