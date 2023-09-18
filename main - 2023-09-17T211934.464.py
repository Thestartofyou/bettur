import random
import json

# Sample pet data (you can replace this with real data)
pets = [
    {"name": "Buddy", "type": "Dog", "age": 3, "location": "New York"},
    {"name": "Whiskers", "type": "Cat", "age": 2, "location": "Los Angeles"},
    {"name": "Rex", "type": "Dog", "age": 4, "location": "Chicago"},
]

# Database to store user and pet data
users_db = {}
matches_db = {}

# Load existing user and match data from a JSON file
try:
    with open("data.json", "r") as file:
        data = json.load(file)
        users_db = data.get("users", {})
        matches_db = data.get("matches", {})
except FileNotFoundError:
    pass

def save_data():
    data = {"users": users_db, "matches": matches_db}
    with open("data.json", "w") as file:
        json.dump(data, file)

def create_profile():
    username = input("Enter your username: ")
    pet_name = input("Enter your pet's name: ")
    pet_type = input("Enter your pet's type (e.g., Dog, Cat): ")
    pet_age = input("Enter your pet's age: ")
    location = input("Enter your location: ")

    users_db[username] = {
        "pet_name": pet_name,
        "pet_type": pet_type,
        "pet_age": pet_age,
        "location": location,
    }
    save_data()
    print("Profile created successfully!")

def swipe_right(user):
    pet = random.choice([p for p in pets if p["location"] == user["location"]])
    print(f"You swiped right on {pet['name']} ({pet['type']}, {pet['age']} years old)!")
    matches_db[user["pet_name"]] = pet
    save_data()

def swipe_left():
    if not pets:
        print("No more pets to swipe!")
        return
    pet = pets.pop(0)
    print(f"You swiped left on {pet['name']} ({pet['type']}, {pet['age']} years old)!")

def show_matches(user):
    matched_pets = [pet for pet in matches_db.values() if pet["location"] == user["location"]]
    if not matched_pets:
        print("You haven't matched with any pets yet.")
    else:
        print("Your matches:")
        for pet in matched_pets:
            print(f"{pet['name']} ({pet['type']}, {pet['age']} years old)")

while True:
    print("\nOptions:")
    print("1. Create Profile")
    print("2. Swipe right (like)")
    print("3. Swipe left (pass)")
    print("4. Show Matches")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_profile()
    elif choice == "2":
        username = input("Enter your username: ")
        if username in users_db:
            swipe_right(users_db[username])
        else:
            print("User not found. Create a profile first.")
    elif choice == "3":
        swipe_left()
    elif choice == "4":
        username = input("Enter your username: ")
        if username in users_db:
            show_matches(users_db[username])
        else:
            print("User not found. Create a profile first.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

