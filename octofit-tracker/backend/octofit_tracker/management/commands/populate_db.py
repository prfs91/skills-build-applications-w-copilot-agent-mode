from django.core.management.base import BaseCommand
from djongo import models

# Define models for test data
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()

class Activity(models.Model):
    name = models.CharField(max_length=100)
    calories_burned = models.IntegerField()

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()

class Workout(models.Model):
    user = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes

class Command(BaseCommand):
    help = "Populate the database with test data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate Users
        users = [
            {"name": "Alice", "email": "alice@example.com", "team": "Team A"},
            {"name": "Bob", "email": "bob@example.com", "team": "Team B"},
        ]
        for user in users:
            User.objects.create(**user)

        # Populate Teams
        teams = [
            {"name": "Team A", "points": 120},
            {"name": "Team B", "points": 150},
        ]
        for team in teams:
            Team.objects.create(**team)

        # Populate Activities
        activities = [
            {"name": "Running", "calories_burned": 300},
            {"name": "Cycling", "calories_burned": 250},
        ]
        for activity in activities:
            Activity.objects.create(**activity)

        # Populate Leaderboard
        leaderboard = [
            {"user": "Alice", "points": 80},
            {"user": "Bob", "points": 100},
        ]
        for entry in leaderboard:
            Leaderboard.objects.create(**entry)

        # Populate Workouts
        workouts = [
            {"user": "Alice", "activity": "Running", "duration": 30},
            {"user": "Bob", "activity": "Cycling", "duration": 45},
        ]
        for workout in workouts:
            Workout.objects.create(**workout)

        self.stdout.write(self.style.SUCCESS("Database populated with test data."))
