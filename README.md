# 🎵 Music Recommender System

A terminal-based music recommender system that suggests songs based on user search, similarity, and mood using a real Spotify dataset.

# 📌 Problem Statement

With the vast number of songs available today, users often struggle to find music that matches their mood or preferences efficiently. Most platforms require manual searching or rely heavily on algorithms that are not transparent to the user.
This project aims to solve that problem by providing a simple, interactive command-line tool that helps users discover songs quickly based on their input.

#💡 Project Overview

This system allows users to:

- Search songs or artists  
- Get detailed song information  
- Receive similar song recommendations  
- Discover songs based on mood  
- Explore random songs from the dataset  

The project is built using Python and works entirely in the terminal, making it lightweight and easy to run.

Features

-  Search songs by name or artist  
-  View detailed song information  
-  Get similar song recommendations  
-  Mood-based song suggestions (happy, sad, chill, party)  
-  Random song generator  
-  Fast and lightweight terminal interface

  tech Stack

- Python  
- Pandas  
- CSV Dataset (Spotify songs data)  



#Requirements

Make sure you have the following installed:

- Python 3.x  
- pip  

Install required libraries:

```bash
pip install pandas


## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/shauryathapa/music-recommender-system.git

Navigate to project folder
cd music-recommender-system/src

RUN THE PROGRAM

USAGE
OUTPUT AFTER RUNNING THe CODE
====== MUSIC RECOMMENDER ======
1. Search song/artist
2. Get song info
3. Recommend similar songs
4. Mood-based songs
5. Random songs
6. Exit

Example output
Enter choice: 1
Enter song name: Shape of You

Found 3 songs:
1. Shape of You - Ed Sheeran
2. Shape of My Heart - Sting
3. Thinking Out Loud - Ed Sheeran

<img width="940" height="629" alt="image_2026-03-30_234352545" src="https://github.com/user-attachments/assets/e73612bb-231d-47bb-ae15-6b1272f722ae" />
<img width="940" height="629" alt="image_2026-03-30_234352545" src="https://github.com/user-attachments/assets/e73612bb-231d-47bb-ae15-6b1272f722ae" />
<img width="940" height="629" alt="image" src="https://github.com/user-attachments/assets/629e1ec1-aac5-4109-8a29-78a5a70a212c" />
<img width="940" height="629" alt="image" src="https://github.com/user-attachments/assets/629e1ec1-aac5-4109-8a29-78a5a70a212c" />


Project Structure
music-recommender-system/
│
├── src/
│   ├── main.py
│   └── spotify_data_clean.csv
│
├── README.md
├── .gitignore
└── LICENSE


Future Improvements
Add support for Hindi and multilingual songs
Integrate Spotify API for real-time recommendations
Build a web interface using Flask or Streamlit
Improve recommendation accuracy using ML models
