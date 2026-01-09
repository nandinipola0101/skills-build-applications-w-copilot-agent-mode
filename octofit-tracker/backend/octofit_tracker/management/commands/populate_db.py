from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        # User.objects.all().delete()  # Avoid due to Djongo/MongoDB bug
        # Team.objects.all().delete()  # Avoid due to Djongo/MongoDB bug

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='Team DC', description='DC superheroes')

        # Create Users (team is a CharField, not FK)
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        from datetime import date
        # Create Activities (no distance, requires date)
        Activity.objects.create(user=tony, type='Run', duration=30, date=date.today())
        Activity.objects.create(user=steve, type='Swim', duration=45, date=date.today())
        Activity.objects.create(user=bruce, type='Cycle', duration=60, date=date.today())
        Activity.objects.create(user=clark, type='Run', duration=25, date=date.today())

        # Create Workouts (requires difficulty)
        Workout.objects.create(name='Avengers HIIT', description='High intensity interval training for Marvel heroes', difficulty='Hard')
        Workout.objects.create(name='Justice League Strength', description='Strength training for DC heroes', difficulty='Medium')

        # Create Leaderboard (score and rank)
        Leaderboard.objects.create(user=tony, score=100, rank=1)
        Leaderboard.objects.create(user=steve, score=90, rank=3)
        Leaderboard.objects.create(user=bruce, score=95, rank=4)
        Leaderboard.objects.create(user=clark, score=98, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
