import media
import fresh_tomatoes

# class instantiating section:
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",   # noqa
    "https://www.youtube.com/watch?v=a0CDJZu4M5I")

captain_phillips = media.Movie(
    "Captain Bill",
    "The true story of Captain Phillips and the 2009 hijacking "
    "by Somali pirates",
    "https://upload.wikimedia.org/wikipedia/en/a/a8/Captain_Phillips_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=D36VztJ8oaQ")

golden_pond = media.Movie(
    "On Golden Pond",
    "The Golden Pond depicts a love story of true romance",
    "https://upload.wikimedia.org/wikipedia/en/3/34/On_golden_pond.jpg",
    "https://www.youtube.com/watch?v=HWjBM48YP0s")

sound_of_music = media.Movie(
    "The Sound Of Music",
    "The most enduringly popular films ever made, yet behind it "
    "lies an even more astonishing family story",
    "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",
    "https://www.youtube.com/watch?v=UY6uw3WpPzY")

lion_king = media.Movie(
    "Lion King",
    "The Lion King tells the story of Simba, a young lion "
    "who is to succeed his father, Mufasa, as king",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",    "https://www.youtube.com/watch?v=4sj1MT05lAA")

# appending movies into a list:
movies = [toy_story, avatar, captain_phillips, golden_pond, sound_of_music, lion_king]    # noqa

# calling the external rendering function:
fresh_tomatoes.open_movies_page(movies)
