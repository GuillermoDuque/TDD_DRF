import pytest

from movies.models import Dog


@pytest.mark.django_db
def test_add_dog(client):
    dog = Dog.objects.all()
    assert len(dog) == 0

    resp = client.post(
        "/api/dog/",
        {
            "name": "puppy",
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["name"] == "puppy"

    dog = Dog.objects.all()
    assert len(dog) == 1
