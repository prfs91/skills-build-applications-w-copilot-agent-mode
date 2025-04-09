from djongo import models

# Model for Users
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

# Model for Teams
class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.JSONField()

# Model for Activity
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()

# Model for Leaderboard
class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

# Model for Workouts
class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
