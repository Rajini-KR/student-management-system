from django.contrib.auth import get_user_model
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from students.models import Department, Student


class ApiAuthenticationTests(TestCase):
    @override_settings(ALLOWED_HOSTS=["testserver", "127.0.0.1"])
    def test_session_authenticated_user_can_access_student_api(self):
        user = get_user_model().objects.create_user(
            username="apiuser",
            email="api@example.com",
            password="StrongPass123!",
            first_name="Api",
            last_name="User",
            phone="1234567890",
            role="ADMIN",
        )
        department = Department.objects.create(name="Computer Science", building="A-101")
        Student.objects.create(
            user=user,
            dob="2000-01-01",
            gender="Male",
            cgpa="8.50",
            department=department,
        )

        client = Client()
        client.force_login(user)

        response = client.get(reverse("student_api"))

        self.assertEqual(response.status_code, 200)
