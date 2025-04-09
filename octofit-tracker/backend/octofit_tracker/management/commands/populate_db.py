from django.core.management.base import BaseCommand
from pymongo import MongoClient
from octofit_tracker.test_data import test_data

class Command(BaseCommand):
    help = 'Populate the MongoDB database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient("mongodb://127.0.0.1:27018")
        db = client["octofit_db"]

        # Insert test data into collections
        db.users.insert_many(test_data["users"])
        db.teams.insert_many(test_data["teams"])
        db.activities.insert_many(test_data["activities"])
        db.leaderboard.insert_many(test_data["leaderboard"])
        db.workouts.insert_many(test_data["workouts"])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
