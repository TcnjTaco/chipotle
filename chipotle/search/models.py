from django.db import models
import datetime as dt
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator


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





