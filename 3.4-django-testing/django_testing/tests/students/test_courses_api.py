import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_retrieve_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=1)
    course = courses[0]

    # Act
    response = client.get(f'/api/v1/courses/{course.id}/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course.id
    assert data['name'] == course.name


@pytest.mark.django_db
def test_list_courses(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, item in enumerate(data):
        assert item['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_courses_by_id(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)
    target_course = courses[3]

    # Act
    response = client.get('/api/v1/courses/', data={'id': target_course.id})

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['id'] == target_course.id
    assert data[0]['name'] == target_course.name


@pytest.mark.django_db
def test_filter_courses_by_name(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)
    target_course = courses[5]

    # Act
    response = client.get('/api/v1/courses/', data={'name': target_course.name})

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['id'] == target_course.id
    assert data[0]['name'] == target_course.name


@pytest.mark.django_db
def test_create_course(client):
    # Arrange
    count = Course.objects.count()
    payload = {'name': 'Python-разработчик с нуля'}

    # Act
    response = client.post('/api/v1/courses/', data=payload)

    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    data = response.json()
    assert data['name'] == payload['name']


@pytest.mark.django_db
def test_update_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=1)[0]
    payload = {'name': 'Обновлённый курс по Django'}

    # Act
    response = client.patch(f'/api/v1/courses/{course.id}/', data=payload)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == payload['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=1)[0]
    count = Course.objects.count()

    # Act
    response = client.delete(f'/api/v1/courses/{course.id}/')

    # Assert
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
