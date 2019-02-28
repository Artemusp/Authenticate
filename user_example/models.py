from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True, height_field="height", width_field="width")
    file = models.FileField(null=True, blank=True)

    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    video_url = models.CharField(max_length=200,default="link")
    #rating = models.CharField(max_length=2, default=0)
    rating = models.IntegerField(max_length=2, default=0)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()

        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #title = models.CharField(max_length=200)
    text = models.TextField(default="")
    direction = models.CharField(max_length=300)
    course = models.CharField(max_length=300)
    group = models.CharField(max_length=300)

    image = models.ImageField(null=True, blank=True, height_field="height", width_field="width")
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #title = models.CharField(max_length=200)
    text = models.TextField(default="")

    image = models.ImageField(null=True, blank=True, height_field="height", width_field="width")

    file = models.FileField(null=True, blank=True)
    file2 = models.FileField(null=True, blank=True)
    file3 = models.FileField(null=True, blank=True)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    video_url = models.CharField(max_length=200, default="link")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title