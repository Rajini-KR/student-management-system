from django.contrib import admin
from .models import Student,Course,Department

@admin.register(Department)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'building',)
    

    @admin.register(Course)

    class CourseAdmin(admin.ModelAdmin):
        list_display = ('id',
                        'name',
                        'code',
                        'credits')
        
        
    @admin.register(Student)

    class StudentAdmin(admin.ModelAdmin):
        list_display=('id',
                      'user',
                      'department',
                      'cgpa',
        )
        list_filter=('department','gender')
        search_fields=('user__username','user__first_name','user__last_name','user__email')
        filter_horizontal=('courses',)