from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados de teste'

    def handle(self, *args, **kwargs):
        # Criar usuários de teste
        user1 = User.objects.create(email='user1@example.com', name='User One', age=20)
        user2 = User.objects.create(email='user2@example.com', name='User Two', age=25)

        # Criar equipes de teste
        team = Team.objects.create(name='Team A')
        team.members.add(user1, user2)

        # Criar atividades de teste
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-01')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-04-02')

        # Criar leaderboard de teste
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Criar treinos de teste
        Workout.objects.create(name='Workout A', description='Description for Workout A')
        Workout.objects.create(name='Workout B', description='Description for Workout B')

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
