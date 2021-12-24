from art import logo
from art import vs
from game_data import data
import random

score = 0
richtig = True

def generate_data():
  generated_data_list = []
  same_number = True
  while same_number == True:
    data_1_number = random.randint(0, len(data)-1)
    data_2_number = random.randint(0, len(data)-1)
    if data_1_number != data_2_number:
      same_number = False
  data_1 = data[data_1_number]
  data_2 = data[data_2_number]
  generated_data_list.append(data_1)
  generated_data_list.append(data_2)
  return generated_data_list

def game():
  print(logo)

  generated_data_list = generate_data()
  name_a = generated_data_list[0]["name"]
  follower_a = generated_data_list[0]["follower_count"]
  description_a = generated_data_list[0]["description"]
  country_a = generated_data_list[0]["country"]

  name_b = generated_data_list[1]["name"]
  follower_b = generated_data_list[1]["follower_count"]
  description_b = generated_data_list[1]["description"]
  country_b = generated_data_list[1]["country"]

  print(f"Compare A: {name_a}, a {description_a}, from {country_a}.\n")
  print(vs + "\n")
  print(f"Against B: {name_b}, a {description_b}, from {country_b}.\n ")

  inp = input("Who has more followers!")

  if inp == "A":
    if follower_a > follower_b:
      return True
    else:
      return False
  if inp == "B":
    if follower_a < follower_b:
      return True
    else:
      return False

while richtig == True:
  decision = game()
  if decision == True:
    score += 1
  else:
    richtig = False
    print(f"Dein Score war: {score}")

