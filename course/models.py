from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Category(BaseModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    title = models.CharField(max_length=100)
    video_link = models.URLField()
    viewing_duration = models.IntegerField()
    products = models.ManyToManyField(Category, related_name='lessons')

    def __str__(self):
        return self.title


class LessonAnalysis(BaseModel):

    lesson_v = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watched_time = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.watched_time >= 0.8 * self.lesson_v.viewing_duration:
            self.status = True
        else:
            self.status = False
            super(LessonAnalysis, self).save(*args, **kwargs)

    def __str__(self):
        return self.lesson_v.title
