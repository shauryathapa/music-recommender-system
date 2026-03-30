import pandas as pd
import random

#THIS LOADS THE CLEANED DATASET FROM THE CSV FILE INTO A PANDAS DATAFRAME.
df = pd.read_csv("src/spotify_data_clean.csv")

# Normalize column names
df.columns = [col.strip().lower() for col in df.columns]

# Column names to use in the code
TRACK = "track_name"
ARTIST = "artist_name"
ALBUM = "album_name"
DURATION = "track_duration_min"
POPULARITY = "track_popularity"


#search for songs or artists that match the query

def search_song_or_artist(query):
    query = query.lower()

    results = df[
        df[TRACK].astype(str).str.lower().str.contains(query, na=False) |
        df[ARTIST].astype(str).str.lower().str.contains(query, na=False)
    ]

    if results.empty:
        print("❌ No results found")
    else:
        print("\n🔍 Results:")
        print(results[[TRACK, ARTIST]].head(10))

#get detailed info about a specific song by its exact name

def get_song_info(song):
    song = song.lower()

    result = df[df[TRACK].astype(str).str.lower() == song]

    if result.empty:
        print("❌ Song not found")
    else:
        row = result.iloc[0]
        print("\n🎵 Song Info:")
        print(f"Name     : {row[TRACK]}")
        print(f"Artist   : {row[ARTIST]}")
        print(f"Album    : {row[ALBUM]}")
        print(f"Duration : {row[DURATION]} mins")
        print(f"Popularity: {row[POPULARITY]}")

#based on a given song, recommend similar songs using simple heuristics like same artist, same album, or similar popularity.
def recommend_similar(song):
    song = song.lower()

    base = df[df[TRACK].astype(str).str.lower() == song]

    if base.empty:
        print("❌ Song not found")
        return

    base = base.iloc[0]


    # Same artist OR same album OR similar popularity
    same_artist = df[df[ARTIST] == base[ARTIST]]
    same_album = df[df[ALBUM] == base[ALBUM]]

    df["pop_diff"] = abs(df[POPULARITY] - base[POPULARITY])
    similar_pop = df.sort_values("pop_diff").head(10)

    combined = pd.concat([same_artist, same_album, similar_pop]).drop_duplicates()

    print("\n🔥 Similar Songs:")
    for _, row in combined.head(10).iterrows():
        print(f"{row[TRACK]} - {row[ARTIST]}")


def recommend_by_mood(mood):
    mood = mood.lower()

    #this works base on the popularity of the songs.
    if mood == "sad":
        filtered = df[df[POPULARITY] < 40]
    elif mood == "happy":
        filtered = df[df[POPULARITY] > 70]
    elif mood == "party":
        filtered = df[df[POPULARITY] > 80]
    elif mood == "chill":
        filtered = df[(df[POPULARITY] >= 40) & (df[POPULARITY] <= 70)]
    else:
        print("❌ Invalid mood")
        return

    if filtered.empty:
        print("❌ No songs found")
        return

    sample = filtered.sample(min(10, len(filtered)))

    print(f"\n🎧 {mood.upper()} Songs:")
    for _, row in sample.iterrows():
        print(f"{row[TRACK]} - {row[ARTIST]}")

# uses random to give random set of songs from the dataset.
def random_songs():
    sample = df.sample(min(10, len(df)))

    print("\n Random Songs:")
    for _, row in sample.iterrows():
        print(f"{row[TRACK]} - {row[ARTIST]}")


#main function to run the command line interface for the music recommender system.

def main():
    while True:
        print("\n====== MUSIC RECOMMENDER ======")
        print("1. Search song/artist")
        print("2. Get song info")
        print("3. Recommend similar songs")
        print("4. Mood-based songs")
        print("5. Random songs")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            q = input("Enter song or artist: ")
            search_song_or_artist(q)

        elif choice == "2":
            s = input("Enter exact song name: ")
            get_song_info(s)

        elif choice == "3":
            s = input("Enter song name: ")
            recommend_similar(s)

        elif choice == "4":
            m = input("Mood (sad/happy/chill/party): ")
            recommend_by_mood(m)

        elif choice == "5":
            random_songs()

        elif choice == "6":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
