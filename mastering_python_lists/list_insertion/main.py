travel_wishlist = ["Paris", "Oslo", "Kyoto", "Sydney"]

# Adding new elements
travel_wishlist.insert(0, "London")
travel_wishlist.insert(travel_wishlist.index("Paris") +1, "Budapest")

# Testing 
print("Updated travel_wishlist:", travel_wishlist)