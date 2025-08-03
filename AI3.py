# Movie data
movies = [
    {"title": "Titanic", "genre": "Romance Drama"},
    {"title": "The Notebook", "genre": "Romance Drama"},
    {"title": "Avengers", "genre": "Action"},
    {"title": "Matrix", "genre": "Sci-Fi"},
    {"title": "Interstellar", "genre": "Sci-Fi"},
    {"title": "Iron Man", "genre": "Action"},
    {"title": "Inception", "genre": "Sci-Fi"},
    {"title": "The Fault in Our Stars", "genre": "Romance Drama"}
]

# Recommend function
def recommend_movie(movie_name):
    movie_name = movie_name.strip().lower()
    selected_movie = None

    for movie in movies:
        if movie["title"].strip().lower() == movie_name:
            selected_movie = movie
            break

    if not selected_movie:
        print("Movie not found in the database")
        return

    selected_genre = selected_movie["genre"]
    print(f"\nBecause you watched '{selected_movie['title']}', you may also like:")
    for movie in movies:
        if movie["title"] != selected_movie["title"] and movie["genre"] == selected_genre:
            print(f"- {movie['title']} ({movie['genre']})")

# Ask for input and call the function
movie_input = input("Enter a movie you like: ")
recommend_movie(movie_input)
