from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", password="password")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Team A", members=["User1", "User2"])
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", password="password")
        activity = Activity.objects.create(user=user, type="Running", duration=30)
        self.assertEqual(activity.type, "Running")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", password="password")
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Workout A", description="Description of Workout A")
        self.assertEqual(workout.name, "Workout A")
