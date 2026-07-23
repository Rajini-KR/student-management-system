from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from students.models import Course, Department


class RegisterViewTests(TestCase):
    def test_register_page_is_available(self):
        response = self.client.get(reverse("register"))

        self.assertEqual(response.status_code, 200)

    def test_register_page_creates_user(self):
        department = Department.objects.create(
            name="Computer Science",
            building="A-101",
        )
        course = Course.objects.create(
            name="Python",
            code="CS101",
            credits=3,
        )

        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "first_name": "New",
                "last_name": "User",
                "email": "new@example.com",
                "phone": "1234567890",
                "role": "STUDENT",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
                "dob": "2000-01-01",
                "gender": "Male",
                "cgpa": "8.50",
                "department": department.pk,
                "courses": [course.pk],
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            get_user_model().objects.filter(username="newuser").exists()
        )
