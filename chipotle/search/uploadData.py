import os, csv
from search.models import courseInfo
os.chdir("C:\\Users\\abhij\\Desktop\\Taco\\chipotle\\chipotle\\search")

with open('courseInfoData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        
        p = courseInfo(class_id=row['class_id'], course_code=row['course_code'], professor=row['professor'], day=row['day'], time=row['time'])
        p.save()