import fresh_tomatoes
import media

dr_strange = media.Movie("Doctor Strange", 
	"A former neurosurgeon embarks on a journey of healing only to be drawn into the world of the mystic arts.",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2ODA4MTM0M15BMl5BanBnXkFtZTgwNzE5OTYxMDI@._V1_SY317_CR1,0,214,317_AL_.jpg", 
	"https://www.youtube.com/watch?v=HSzx-zryEgM")

rogue_one = media.Movie("Rogue One", 
	"The Rebellion makes a risky move to steal the plans to the Death Star, setting up the epic saga to follow.",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwMzMxODIzOV5BMl5BanBnXkFtZTgwNzg3OTAzMDI@._V1_SX214_AL_.jpg", 
	"https://www.youtube.com/watch?v=frdj1zb9sMY")

logan = media.Movie("Logan", 
	"Set in the future, Logan and Professor Charles Xavier must cope with the loss of the X-Men when a corporation led by Nathaniel Essex is destroying the world leaving it to destruction, with Logan's healing abilities slowly fading away and Xavier's Alzheimer's forcing him to forget. Logan must defeat Nathaniel Essex with the help of a young girl named Laura Kinney, a female clone of Wolverine.", 
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxMDc1OTAzM15BMl5BanBnXkFtZTgwOTMwOTMyMDI@._V1_UX182_CR0,0,182,268_AL_.jpg", 
	"https://www.youtube.com/watch?v=Div0iP65aZo")

power_rangers = media.Movie("Power Rangers", 
	"A group of high-school kids, who are infused with unique superpowers, harness their abilities in order to save the world.", 
	"https://images-na.ssl-images-amazon.com/images/M/MV5BNDA3MTk3NzE0MF5BMl5BanBnXkFtZTgwOTYxNTQyOTE@._V1_UX182_CR0,0,182,268_AL_.jpg", 
	"https://www.youtube.com/watch?v=j2djAzvV9mw")

guardians_2 = media.Movie("Guardians of the Galaxy Vol. 2", 
	"Set to the backdrop of Awesome Mixtape #2, 'Guardians of the Galaxy Vol. 2' continues the team's adventures as they unravel the mystery of Peter Quill's true parentage.", 
	"https://images-na.ssl-images-amazon.com/images/M/MV5BNDhmNzE0YzktNGUzZC00MjQ5LTgyZGQtNWNhNGE2NjkxZWZmXkEyXkFqcGdeQXVyNDQzODM3Mzc@._V1_UX182_CR0,0,182,268_AL_.jpg", 
	"https://www.youtube.com/watch?v=Y3-cZveM34c")

wonder_woman = media.Movie("Wonder Woman", 
	"An Amazonian princess leaves her island home to explore the world and, in doing so, becomes one of the world's greatest heroes.", 
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMzUxNjQ5MjAyOF5BMl5BanBnXkFtZTgwMjIzOTA1MDI@._V1_UX182_CR0,0,182,268_AL_.jpg", 
	"https://www.youtube.com/watch?v=Tgk_63b-Mrw")

movies = [dr_strange, rogue_one, logan, power_rangers, guardians_2, wonder_woman]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)