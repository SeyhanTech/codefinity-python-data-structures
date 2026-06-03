movie_genres = ("Action", "Comedy", "Drama", "Horror", "Sci-Fi")

# Write your code here
temp_list = list(movie_genres)

temp_list[temp_list.index("Drama")] = "Thriller"  
temp_list[temp_list.index("Horror")] = "Adventure"  

movie_genres = tuple(temp_list)

del temp_list

# Testing
print("Updated genres:", movie_genres)