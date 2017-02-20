import media
import fresh_tomatoes

office_space = media.Movie("Office Space",
                           "A hypnotized man learns the true value of modern work.",
                           "https://www.movieposter.com/posters/archive/main/58/MPW-29049",
                           "https://youtu.be/dMIrlP61Z9s")

the_big_lebowski = media.Movie("The Big Lebowski",
                               "The laziest man in Los Angeles County finds himself involved in a kidnapping scheme.",
                               "https://s-media-cache-ak0.pinimg.com/originals/76/a8/25/76a8252e814a7ae6be56536fbd4e80ec.jpg",
                               "https://youtu.be/cd-go0oBF4Y")

blood_diamond = media.Movie("Blood Diamond",
                            "A crooked arms dealer finds a conscience.",
                            "https://s3.amazonaws.com/piktochartv2-dev/v2/uploads/4ade8003-cca9-45be-878f-fbe8dedb06c2/c5f0db3326c3718c214d04ff0f33377071380de7_original.jpg",
                            "https://youtu.be/yknIZsvQjG4")

the_professional = media.Movie("The Professional",
                               "A hitman takes a 9-year-old girl as an apprentice.",
                               "http://img.moviepostershop.com/the-professional-movie-poster-1994-1020191956.jpg",
                               "https://youtu.be/DcsirofJrlM")

vanilla_sky = media.Movie("Vanilla Sky",
                          "A horrible accident leads the heir of a publishing company into the future.",
                          "http://www.impawards.com/2001/posters/vanilla_sky_xlg.jpg",
                          "https://youtu.be/k09OX40NLUw")

bull_durham = media.Movie("Bull Durham",
                          "A career minor leaguer chases the all-time homerun record.",
                          "http://www.dvdsreleasedates.com/posters/800/B/Bull-Durham-movie-poster.jpg",
                          "https://youtu.be/kqqdEwFz4mU")

movies = [office_space, the_big_lebowski, blood_diamond, the_professional, vanilla_sky, bull_durham]
fresh_tomatoes.open_movies_page(movies)


