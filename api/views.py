from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from students.models import Student, Department, Course

from .serializers import (
    StudentSerializer,
    StudentWriteSerializer,
    DepartmentSerializer,
    CourseSerializer,
)


# ---------------------------------
# Student List + Create
# ---------------------------------

class StudentListCreateAPI(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]

    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    queryset = Student.objects.select_related(
        "user",
        "department",
    ).prefetch_related("courses")

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_fields = (
        "gender",
        "department",
    )

    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__email",
        "department__name",
    )

    ordering_fields = (
        "cgpa",
        "dob",
        "user__first_name",
    )

    ordering = (
        "user__first_name",
    )

    def get_serializer_class(self):

        if self.request.method == "POST":
            return StudentWriteSerializer

        return StudentSerializer


# ---------------------------------
# Student Retrieve Update Delete
# ---------------------------------

class StudentRetrieveUpdateDestroyAPI(
    generics.RetrieveUpdateDestroyAPIView
):

    permission_classes = [IsAuthenticated]

    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    queryset = Student.objects.select_related(
        "user",
        "department",
    ).prefetch_related("courses")

    def get_serializer_class(self):

        if self.request.method in ["PUT", "PATCH"]:
            return StudentWriteSerializer

        return StudentSerializer


# ---------------------------------
# Department List
# ---------------------------------

class DepartmentListAPI(generics.ListAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Department.objects.all()

    serializer_class = DepartmentSerializer


# ---------------------------------
# Course List
# ---------------------------------

class CourseListAPI(generics.ListAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Course.objects.all()

    serializer_class = CourseSerializer