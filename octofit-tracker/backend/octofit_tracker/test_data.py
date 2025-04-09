# Test data for the octofit_db database

test_data = {
    "users": [
        {"username": "john_doe", "email": "john@example.com", "password": "password123"},
        {"username": "jane_smith", "email": "jane@example.com", "password": "password123"}
    ],
    "teams": [
        {"name": "Team Alpha", "members": ["john_doe", "jane_smith"]},
        {"name": "Team Beta", "members": []}
    ],
    "activities": [
        {"name": "Running", "calories_burned_per_minute": 10},
        {"name": "Cycling", "calories_burned_per_minute": 8}
    ],
    "leaderboard": [
        {"username": "john_doe", "points": 150},
        {"username": "jane_smith", "points": 200}
    ],
    "workouts": [
        {"username": "john_doe", "activity": "Running", "duration_minutes": 30},
        {"username": "jane_smith", "activity": "Cycling", "duration_minutes": 45}
    ]
}
