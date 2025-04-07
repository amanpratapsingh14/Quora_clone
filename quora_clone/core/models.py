from django.db import models
from django.contrib.auth.models import User


"""
Question: Stores the question title, description, creator, and timestamp.
Answer: Links to a question and user, includes text, timestamp, and a ManyToMany field for likes.
"""

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_answers')

    def __str__(self):
        return f"Answer to {self.question.title} by {self.created_by.username}"