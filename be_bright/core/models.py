from django.db import models
from django.utils import timezone


# Create your models here.

class Themes(models.Model):
    id = models.IntegerField(primary_key=True)
    theme_name = models.CharField(max_length=256)


class CoursesMaterials(models.Model):
    id = models.IntegerField(primary_key=True)
    material_text = models.TextField(null=True, blank=True)
    material_links = models.TextField(null=True, blank=True)
    theme = models.ForeignKey(Themes, on_delete=models.SET_NULL, null=True, blank=True, related_name='course_theme')
    course_id = models.ForeignKey('Courses', on_delete=models.CASCADE)


class CoursesMaterialsFiles(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    material = models.ForeignKey(CoursesMaterials, on_delete=models.CASCADE, related_name='courses_files')


class Teachers(models.Model):
    id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    date_of_creation = models.DateField(auto_now=False, auto_now_add=True)
    address = models.CharField(max_length=200)
    is_chief = models.BooleanField(default=False)


class TeachersLogin(models.Model):
    teacher_id = models.OneToOneField(Teachers, primary_key=True, on_delete=models.CASCADE)
    password_salt = models.CharField(max_length=256)
    password_hash = models.CharField(max_length=256)
    hash_algorithm = models.IntegerField()


class TeachersAchievement(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='achievement')
    curse_id = models.ForeignKey('Courses', on_delete=models.CASCADE)


class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    date_of_creation = models.DateField(auto_now=False, auto_now_add=True)
    address = models.CharField(max_length=200)


class StudentsLogin(models.Model):
    student_id = models.OneToOneField(Students, primary_key=True, on_delete=models.CASCADE)
    password_salt = models.CharField(max_length=256)
    password_hash = models.CharField(max_length=256)
    hash_algorithm = models.IntegerField()


class StudentsAchievement(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='achievement')
    curse_id = models.ForeignKey('Courses', on_delete=models.CASCADE)


class Courses(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    teachers = models.ManyToManyField(Teachers, blank=True)
    students = models.ManyToManyField(Students, blank=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    course_code = models.CharField(max_length=8, unique=True)


class Tasks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    task = models.TextField()
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    task_theme = models.ForeignKey(Themes, on_delete=models.SET_NULL, related_name='task_theme')


class TasksMaterials(models.Model):
    id = models.IntegerField(primary_key=True)
    material_text = models.TextField(null=True, blank=True)
    material_links = models.TextField(null=True, blank=True)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)


class MaterialsFiles(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    material = models.ForeignKey(TasksMaterials, on_delete=models.CASCADE, related_name='materials_files')


class Results(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.TextField(null=True, blank=True)
    grade = models.PositiveSmallIntegerField()
    answer_id = models.OneToOneField('Answers', on_delete=models.CASCADE)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)


class Answers(models.Model):
    id = models.IntegerField(primary_key=True)
    answer_text = models.TextField(blank=True, null=True)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)


class AnswersFiles(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='answers_files')
