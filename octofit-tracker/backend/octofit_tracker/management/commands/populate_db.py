from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB directly using pymongo
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert users
        users = [
            {'_id': '1', 'username': 'thundergod', 'email': 'thundergod@mhigh.edu', 'password': 'thundergodpassword'},
            {'_id': '2', 'username': 'metalgeek', 'email': 'metalgeek@mhigh.edu', 'password': 'metalgeekpassword'},
            {'_id': '3', 'username': 'zerocool', 'email': 'zerocool@mhigh.edu', 'password': 'zerocoolpassword'},
            {'_id': '4', 'username': 'crashoverride', 'email': 'crashoverride@mhigh.edu', 'password': 'crashoverridepassword'},
            {'_id': '5', 'username': 'sleeptoken', 'email': 'sleeptoken@mhigh.edu', 'password': 'sleeptokenpassword'},
        ]
        db.users.insert_many(users)

        # Insert teams
        teams = [
            {'_id': '1', 'name': 'Blue Team', 'members': ['1', '2', '3']},
            {'_id': '2', 'name': 'Gold Team', 'members': ['4', '5']},
        ]
        db.teams.insert_many(teams)

        # Insert activities
        activities = [
            {'user_id': '1', 'activity_type': 'Cycling', 'duration': 60},
            {'user_id': '2', 'activity_type': 'Crossfit', 'duration': 120},
            {'user_id': '3', 'activity_type': 'Running', 'duration': 90},
            {'user_id': '4', 'activity_type': 'Strength', 'duration': 30},
            {'user_id': '5', 'activity_type': 'Swimming', 'duration': 75},
        ]
        db.activities.insert_many(activities)

        # Insert leaderboard entries
        leaderboard = [
            {'user_id': '1', 'score': 100},
            {'user_id': '2', 'score': 90},
            {'user_id': '3', 'score': 95},
            {'user_id': '4', 'score': 85},
            {'user_id': '5', 'score': 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Insert workouts
        workouts = [
            {'name': 'Cycling Training', 'description': 'Training for a road cycling event'},
            {'name': 'Crossfit', 'description': 'Training for a crossfit competition'},
            {'name': 'Running Training', 'description': 'Training for a marathon'},
            {'name': 'Strength Training', 'description': 'Training for strength'},
            {'name': 'Swimming Training', 'description': 'Training for a swimming competition'},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data using pymongo.'))