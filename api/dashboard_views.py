from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from students.models import Student, Department, Course


class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_students = Student.objects.count()
        total_departments = Department.objects.count()
        total_courses = Course.objects.count()

        # Gender breakdown
        male_count = Student.objects.filter(gender="Male").count()
        female_count = Student.objects.filter(gender="Female").count()
        other_count = Student.objects.filter(gender="Other").count()

        # Students per department
        departments = Department.objects.all()
        dept_data = [
            {
                "name": dept.name,
                "student_count": dept.students.count(),
            }
            for dept in departments
        ]

        return Response({
            "total_students": total_students,
            "total_departments": total_departments,
            "total_courses": total_courses,
            "gender_breakdown": {
                "male": male_count,
                "female": female_count,
                "other": other_count,
            },
            "departments": dept_data,
        })
