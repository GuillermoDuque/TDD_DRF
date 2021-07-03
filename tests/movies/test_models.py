import pytest

from movies.models import Movie, Dog


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="Raising Arizona", genre="comedy", year="1987")
    movie.save()
    assert movie.title == "Raising Arizona"
    assert movie.genre == "comedy"
    assert movie.year == "1987"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title


@pytest.mark.django_db
def test_dog_name():
    dog = Dog(name="emma")
    dog.save()
    assert dog.name == "emma"


@pytest.mark.django_db
def test_dog_is_happy():
    dog = Dog(name="emma")
    dog.save()
    assert dog.is_happy
