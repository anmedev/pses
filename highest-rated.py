# Implement Highest Rated

# Create a function named get_highest_rated that is responsible for finding the highest-rated restaurant.

# This function should take in a list of dictionaries named restaurants as a parameter. Each dictionary represents the data associated with a restaurant, including its rating. This function should have a return value of the restaurant with the highest rating.

# Ask Clarifying Questions - id: d10ece96-af0b-4f22-a55d-b630ea9b582f
# 1. How should the function handle multiple restaurants with the highest rating?
# 2. How should the function handle a list without any restaurants?

# Wrte Unit Tests - id: 890d7045-28cb-4832-812b-d65803ce2618
# 1. Use the comments provided to write at least two example input/outputs:
  # Consider at least one nominal and one edge case.
  # What is the expected output for the given input?
  # You can use the examples provided in the prompt, or other examples.
# 2. Write unit tests for get_highest_rated for the nominal and edge cases you identified in the first step.

# Nominal Test Case
def test_select_highest_rating_from_list():
    # arrange
    restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]

    # act
    result = get_highest_rated(restaurants)

    # assert
    assert result == {"name": "Crow's Nest", "rating": 5}

# Edge Case
def test_returns_none_from_empty_list():
      # arrange
    restaurants = []

    # act
    result = get_highest_rated(restaurants)

    # assert
    assert result is None

# Create Logical Steps - id: 085ad8a1-7dbd-49ad-aa7a-2213dd0d3c76
# Without writing code, describe how you would implement get_highest_rating in enough detail that someone else could write the code.

# - It may be helpful to break up the problem/algorithm into smaller subproblems/algorithms. For example, 1. Handle invalid input, 2. Given valid input, perform the computation/solve the problem/etc.
# - Your logical steps could take the form of a numbered list, pseudo code, or anywhere in between. What's important at this stage is to think through and outline the implementation before writing code.

# Sub Problems
# Sub Problem 1: Define a function called get_highest_rating, which takes in a list of dictionaries called restaurants as its parameter
# def get_highest_rating(restaurants):

# Sub Problem 2: Determine if the restaurants list is empty
# use a conditional statement and the not operator to see if restaurants is an empty list
#   if the restaurants list is empty
#       then return None
# end

# Sub Problem 3: Create a variable to store the highest rating
# create a variable called highest_rating and set it to the value of the first rating in the restaurants list

# Sub Problem 4: Determine which restaurant has the highest rating
# use a for loop to iterate through each dictionary in the list of dictionaries, where each dictionary represents a restaurant
# use a conditional statement to compare if the rating of the current restaurant is higher than the value stored in the highest_rating variable
#   if the current restaurant's rating is higher, reassign the highest_rating value to the value of the current restaurant's rating
#     then return the restaurant with the highest rating
# end

# Sub Problem 5: Determine the restaurant with the highest rating
# invoke the get_highest_rating function and print the return value to the console

# Solution:
restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]
# restaurants = [{"name": "Crow's Nest", "rating": 1}]
# restaurants = []

def get_highest_rated(restaurants):
  if not restaurants:
    return None

  highest_rating = restaurants[0]["rating"]
  for restaurant in restaurants:
    if restaurant["rating"] > highest_rating:
      highest_rating = restaurant["rating"]
  return restaurant

print(get_highest_rated(restaurants))

# Time Complexity: Linear - O(n)
# Space Complexity: Constant - O(1)