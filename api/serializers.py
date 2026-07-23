from rest_framework import serializers
from students.models import Student, Department, Course
from accounts.models import CustomUser


# ----------------------------
# Department Serializer
# ----------------------------

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"


# ----------------------------
# Course Serializer
# ----------------------------

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


# ----------------------------
# User Serializer
# ----------------------------

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "role",
        )


# ----------------------------
# Student Read Serializer
# ----------------------------

class StudentSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = (
            "id",
            "user",
            "dob",
            "gender",
            "cgpa",
            "department",
            "courses",
            "photo",
        )


# ----------------------------
# Student Create / Update Serializer
# ----------------------------

class StudentWriteSerializer(serializers.ModelSerializer):

    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, required=False)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    phone = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "phone",
            "role",
            "dob",
            "gender",
            "cgpa",
            "department",
            "courses",
            "photo",
        )

    def validate_cgpa(self, value):

        if value < 0 or value > 10:
            raise serializers.ValidationError(
                "CGPA must be between 0 and 10."
            )

        return value

    def validate_email(self, value):

        user = self.instance.user if self.instance else None

        if CustomUser.objects.exclude(
            pk=user.pk if user else None
        ).filter(email=value).exists():

            raise serializers.ValidationError(
                "Email already exists."
            )

        return value

    def validate_username(self, value):

        user = self.instance.user if self.instance else None

        if CustomUser.objects.exclude(
            pk=user.pk if user else None
        ).filter(username=value).exists():

            raise serializers.ValidationError(
                "Username already exists."
            )

        return value

    def create(self, validated_data):

        courses = validated_data.pop("courses")

        username = validated_data.pop("username")
        password = validated_data.pop("password")
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")
        email = validated_data.pop("email")
        phone = validated_data.pop("phone")
        role = validated_data.pop("role")

        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            role=role,
        )

        student = Student.objects.create(
            user=user,
            **validated_data
        )

        student.courses.set(courses)

        return student

    def update(self, instance, validated_data):

        user = instance.user

        courses = validated_data.pop("courses", None)

        user.username = validated_data.pop("username", user.username)
        user.first_name = validated_data.pop("first_name", user.first_name)
        user.last_name = validated_data.pop("last_name", user.last_name)
        user.email = validated_data.pop("email", user.email)
        user.phone = validated_data.pop("phone", user.phone)
        user.role = validated_data.pop("role", user.role)

        password = validated_data.pop("password", None)

        if password:
            user.set_password(password)

        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if courses is not None:
            instance.courses.set(courses)

        return instance