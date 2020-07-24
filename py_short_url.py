import pyshortners as ps

#enter your url here
longURL = "........."
shortURL = ps.Shortener().tinyural.short(longURL)

print(shortURL)
