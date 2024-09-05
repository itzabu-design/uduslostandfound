from django.db import models

class FoundReport(models.Model):
    finder_name = models.CharField(max_length=100)
    gsm = models.CharField(max_length=15, default='0000000000')
    address = models.CharField(max_length=255, default='Unknown')
    item = models.CharField(max_length=255, default='Unknown Item')
    description = models.TextField()
    item_name = models.CharField(max_length=100)
    date_found = models.DateField()

    def __str__(self):
        return f"{self.item} found by {self.name}"

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    gsm = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class LostReport(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    date_lost = models.DateField()

    def __str__(self):
        return self.item_name