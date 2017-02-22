import media
import fresh_tomatoes

# Office Space
office_space = media.Movie(
    "Office Space",
    "A hypnotized man learns the true value of modern work",
    "http://bit.ly/2m3Acqc",
    "https://youtu.be/dMIrlP61Z9s"
)

# The Big Lebowski
the_big_lebowski = media.Movie(
    "The Big Lebowski",
    "A lazy L.A. County man investigates a kidnapping.",
    "http://bit.ly/2l37AJp",
    "https://youtu.be/cd-go0oBF4Y")

# Blood Diamond
blood_diamond = media.Movie(
    "Blood Diamond",
    "A crooked arms dealer finds a conscience.",
    "http://bit.ly/2lBRpWU",
    "https://youtu.be/yknIZsvQjG4"
)

# The Professional
the_professional = media.Movie(
    "The Professional",
    "A hitman takes a 9-year-old girl as an apprentice.",
    "http://bit.ly/2lC1naP",
    "https://youtu.be/DcsirofJrlM"
)

# Vanilla Sky
vanilla_sky = media.Movie(
    "Vanilla Sky",
    "Tom Cruise. Rubber Face. Lucid Deams?",
    "http://bit.ly/2l3kcAe",
    "https://youtu.be/k09OX40NLUw")

# Bull Durham
bull_durham = media.Movie(
    "Bull Durham",
    "A career minor leaguer chases the all-time homerun record.",
    "http://bit.ly/2mhvWPY",
    "https://youtu.be/kqqdEwFz4mU"
)

# Movies list -- to provide input to fresh_tomatoes.py
movies = [office_space, the_big_lebowski, blood_diamond, the_professional,
          vanilla_sky, bull_durham]

# Function call
fresh_tomatoes.open_movies_page(movies)
