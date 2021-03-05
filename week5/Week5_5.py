from urllib.request import urlretrieve

src = "https://movie-phinf.pstatic.net/20200506_168/1588731103437Jz8kl_JPEG/movie_image.jpg?type=m203_290_2"
urlretrieve(src, "poster.png")