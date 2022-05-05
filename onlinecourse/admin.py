from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission, Enrollment

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


#    pass

class ChoiceInline  (admin.StackedInline):
    model = Choice
    extra = 2
#    pass
class QuestionInline (admin.StackedInline):
    model = Question
    extra = 5
    
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ChoiceInline]
    

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['title']
# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin) #, QuestionInline)
admin.site.register(Choice, ChoiceAdmin) #, ChoiceInline)
admin.site.register(Submission)
admin.site.register(Enrollment)