from movies.serializers import MovieSerializer, DogSerializer


def test_valid_movie_serializer():
    valid_serializer_data = {
        "title": "Raising Arizona",
        "genre": "comedy",
        "year": "1987"
    }
    serializer = MovieSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_movie_serializer():
    invalid_serializer_data = {
        "title": "Raising Arizona",
        "genre": "comedy"
    }
    serializer = MovieSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"year": ["This field is required."]}




def test_valid_dog_serializer():
    """" se estan validando con valid_serializer_data en ambas partes"""
    valid_serializer_data = {
        "name": "marianne",
    }
    serializer = DogSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}