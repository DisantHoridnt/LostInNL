from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
STATUS_CHOICES = [('missing', 'Missing'), ('found', 'Found')]
ACTION_CHOICES = [('insert', 'Insert'), ('update', 'Update'), ('delete', 'Delete')]


# user's pk - kwargs={'pk' : self_id}

class MissingPerson(models.Model):
    full_name = models.CharField(max_length=255)
    last_seen_date = models.DateField()
    last_seen_location = models.CharField(max_length=255)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    picture_url = models.TextField()
    contact_info = models.TextField()
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    eye_color = models.CharField(max_length=50)
    case_number = models.CharField(max_length=255)
    #user FK
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name} ({self.id})"


class AuditTrail(models.Model):
    #user FK
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=255)
    action = models.CharField(max_length=6, choices=ACTION_CHOICES)
    record_id = models.IntegerField()
    #user FK
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now_add=True)

class Forum(models.Model):
    #missing person FK
    missing_person = models.ForeignKey(MissingPerson, on_delete=models.CASCADE)
    title = models.TextField()
    #user FK
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    #forum FK
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    content = models.TextField()
    #user FK
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.content}"

class Media(models.Model):
    #missing person FK
    missing_person = models.ForeignKey(MissingPerson, on_delete=models.CASCADE)
    media_url = models.TextField()
    #user FK
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.missing_person_id} @{self.media_url}"
