import fresh_tomatoes
import media

# Each of these are instances of media that contain info for each movie
# The information contained in each instance includes in order:
# movie title, description, movie image url, youtube trailer url

dr_strange = media.Movie("Doctor Strange", 
	"A former neurosurgeon embarks on a journey of healing only to be /"
	"drawn into the world of the mystic arts.",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2ODA4MTM/"
	"0M15BMl5BanBnXkFtZTgwNzE5OTYxMDI@._V1_SY317_CR1,0,214,317_AL_.jpg", 
	"https://www.youtube.com/watch?v=HSzx-zryEgM")

rogue_one = media.Movie("Rogue One", 
	"The Rebellion makes a risky move to steal the plans to the Death/"
	" Star, setting up the epic saga to follow.",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwMzMxODI/"
	"zOV5BMl5BanBnXkFtZTgwNzg3OTAzMDI@._V1_SX214_AL_.jpg", 
	"https://www.youtube.com/watch?v=frdj1zb9sMY")

logan = media.Movie("Logan", 
	"Set in the future, Logan and Professor Charles Xavier must cope /"
	"with the loss of the X-Men when a corporation led by Nathaniel /"
	"Essex is destroying the world leaving it to destruction, with /"
	"Logan's healing abilities slowly fading away and Xavier's /"
	"Alzheimer's forcing him to forget. Logan must defeat Nathaniel /"
	"Essex with the help of a young girl named Laura Kinney.", 
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxMDc1OT/"
	"AzM15BMl5BanBnXkFtZTgwOTMwOTMyMDI@._V1_UX182_CR0,0,182,268_AL_.jpg", 
	"https://www.youtube.com/watch?v=Div0iP65aZo")

power_rangers = media.Movie("Power Rangers", 
	"A group of high-school kids, who are infused with unique /"
	"superpowers, harness their abilities in order to save the world.", 
	"https://images-na.ssl-images-amazon.com/images/M/MV5BNDA3MTk3Nz/"
	"E0MF5BMl5BanBnXkFtZTgwOTYxNTQyOTE@._V1_UX182_CR0,0,182,268_AL_.jpg", 
	"https://www.youtube.com/watch?v=j2djAzvV9mw")

guardians_2 = media.Movie("Guardians of the Galaxy Vol. 2", 
	"Set to the backdrop of Awesome Mixtape #2, 'Guardians of the Galaxy /"
	"Vol. 2' continues the team's adventures as they unravel the mystery /"
	"of Peter Quill's true parentage.", 
	"https://images-na.ssl-images-amazon.com/images/M/MV5BNDhmNzE0YzktNG/"
	"UzZC00MjQ5LTgyZGQtNWNhNGE2NjkxZWZmXkEyXkFqcGdeQXVyNDQzODM3Mzc/"
	"@._V1_UX182_CR0,0,182,268_AL_.jpg", 
	"https://www.youtube.com/watch?v=Y3-cZveM34c")

wonder_woman = media.Movie("Wonder Woman", 
	"An Amazonian princess leaves her island home to explore the world /"
	"and, in doing so, becomes one of the world's greatest heroes.", 
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMzUxNjQ5MjA/"
	"yOF5BMl5BanBnXkFtZTgwMjIzOTA1MDI@._V1_UX182_CR0,0,182,268_AL_.jpg", 
	"https://www.youtube.com/watch?v=Tgk_63b-Mrw")

# Instances were organized into a list called movies
movies = [dr_strange, rogue_one, logan, power_rangers, guardians_2, wonder_woman]

# This will input the list of movies into open_movies_page
# which generates the information above into an html page
fresh_tomatoes.open_movies_page(movies)

