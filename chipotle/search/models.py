from django.db import models
import datetime as dt
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.
class courseInfo(models.Model):
    class_id = models.IntegerField(primary_key=True, null=False, validators=[MaxValueValidator(99999), MinValueValidator(10000)])
    course_code = models.CharField(max_length=10)
    professor = models.CharField(max_length=50)
    day = models.CharField(max_length=7, validators=[MinLengthValidator(7)], blank=False)
    time = models.TimeField() 

    class Meta():
        verbose_name = 'Course Info'
    
    def __str__(self):
        return self.course_code + ": " + self.professor + ", " + self.day + ", " + self.time.strftime('%I:%M %p')



class studentInfo(models.Model):

    majors = [
        ('Computer Science', 'Computer Science'),
        ('Mathematics', 'Mathematics'),
        ('Military Science', 'Military Science'),
        ('Finance', 'Finance'),
        ('Physics', 'Physics'),
        ('Biology', 'Biology')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")

    student_id = models.IntegerField(primary_key=True, null=False, validators=[MaxValueValidator(999999), MinValueValidator(100000)])

    major = models.CharField(max_length = 50, null = False, blank = False, choices = majors)
    eof = models.BooleanField(blank=False, choices = [(True, 'Yes'), (False, 'No')])
    arc = models.BooleanField(blank=False, choices = [(True, 'Yes'), (False, 'No')])

    class Meta():
        verbose_name = 'Student Info'
    
    def __str__(self):
        return self.user.first_name

