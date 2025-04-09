from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(email="test@example.com", name="Test User", age=25)

    def test_user_creation(self):
        user = User.objects.get(email="test@example.com")
        self.assertEqual(user.name, "Test User")

class TeamModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(email="team@example.com", name="Team User", age=30)
        team = Team.objects.create(name="Test Team")
        team.members.add(user)

    def test_team_creation(self):
        team = Team.objects.get(name="Test Team")
        self.assertEqual(team.members.count(), 1)

# Similar tests can be added for Activity, Leaderboard, and Workout models
