from art import logo,vs
from game_data import data
import random
from replit import clear



score = 0
should_continue = True

#Get randaom acount
account_b = random.choice(data)


def format_data(account):
  account_name = account["name"]
  account_des = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_des}, from {account_country}"


def check_answer(guess,acc_a,acc_b):
  if(user_answer == 'A'):
    return acc_a['follower_count'] > acc_b['follower_count']
  else:
    return acc_b['follower_count'] > acc_a['follower_count']

while should_continue :
  print(logo)
  account_a = account_b
  print(f'Compare A: {format_data(account_a)}')
  print(vs)
  account_b = random.choice(data)
 
  while account_a == account_b:
    account_b = random.choice(data)
  print(f'Against B: {format_data(account_b)}')
  user_answer = input("Who has more followers ? 'A' or 'B': ").upper()
  is_correct  = check_answer(user_answer,account_a,account_b)
  clear()
  if is_correct:
    score += 1
    print(f"You are correct! Current Score: {score}.")
  else:
    should_continue = False
    print(f"Sorry,wrong answer ! Final Score: {score}.")
    
    


