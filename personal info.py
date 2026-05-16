# Name: Sayan Dutta
# Project: Personal Information Manager

# Static information
name = "Sayan Dutta"
age = 20
city = "Durgapur"
hobby = "Coding"

# Welcome header
print("=" * 45)
print("     PERSONAL INFORMATION MANAGER")
print("=" * 45)

print("\nPlease tell me about yourself:")
print("-" * 20)

# User input
favorite_food = input("What's your favorite food? ")
favorite_color = input("What's your favorite color? ")

# Input validation
if favorite_food.strip() == "":
    favorite_food = "Not provided"

if favorite_color.strip() == "":
    favorite_color = "Not provided"

# Calculate age in months
age_in_months = age * 12

# Display output
print("\n" + "=" * 45)
print("           YOUR INFORMATION")
print("=" * 45)

print(f"\nName: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")

print(f"\nFavorite Food: {favorite_food.title()}")
print(f"Favorite Color: {favorite_color.title()}")

print("\n" + "=" * 45)
print("Thanks for using this program!")
print("=" * 45)