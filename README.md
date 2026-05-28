# 🎬 Movie Recommendation System  

A **content-based movie recommender system** built with **Streamlit**.  
It suggests similar movies based on your selection and fetches posters via the **IMDb API**.  

🚀 **[Live Demo](https://movierecommendationsystem-dvxtobdoayoe3xtfhf8appq.streamlit.app/)**  

---

## ✨ Features  
- Interactive web app built with [Streamlit](https://streamlit.io).  
- Recommends **top 5 similar movies** based on a given title.  
- Fetches movie posters dynamically from the **IMDb API**.  
- Model artifacts (`movie_list.pkl` and `similarity.pkl`) are stored on **Google Drive** and loaded at runtime.  

---

## 🛠️ Tech Stack  
- **Python 3**  
- **Streamlit** (UI framework)  
- **pandas** (data handling)  
- **pickle** (loading trained data)  
- **gdown** (Google Drive integration)  
- **IMDb API** (poster fetching)  

---

## 📂 Project Structure  
├── app.py # Streamlit app
├── requirements.txt # Python dependencies
├── movie_recom.ipynb # Jupyter Notebook (model building)
└── README.md # Project documentation


---

## ⚡ How It Works  
1. User selects a movie from the dropdown.  
2. The app finds the most similar movies using a **cosine similarity matrix**.  
3. For each recommended movie, a poster is fetched via IMDb API.  
4. Results are displayed in a clean grid layout.  

---

## ▶️ Run Locally  

Clone the repo:
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app.py

📸 Demo Screenshot

<img width="1916" height="1050" alt="image" src="https://github.com/user-attachments/assets/3b7edb66-09ab-43d1-b6bc-955dead30469" />


🙌 Acknowledgments

IMDb API
 for poster data.

Streamlit
 for the UI framework.

Google Drive
 for model hosting.


