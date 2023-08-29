# Who Wants To Be A Millionaire 💰
print('\n'
"#### WELCOME TO 'WHO WANTS TO BE A MILLIONARE' ####"
'\n'
)

import random
import questions

score = 0
n = 0
alpha_lower = ['a', 'b', 'c', 'd']
alpha_upper = ['A', 'B', 'C', 'D']

while n != 15:
  Q = questions.get_question(n,random.randint(0,9))
  print('\n')
  print(Q[0])
  print("A.", Q[1])
  print("B.", Q[2])
  print("C.", Q[3])
  print("D.", Q[4])

  ans_index = None
  correct_format = False

  while not correct_format:
    answer = input("\nWhat is your answer?")
    if answer in alpha_lower or answer in alpha_upper:
      correct_format = True
    else:
      print('Incorrect format!')

  # Convert letter given to index of Question's choices provided

  if answer.islower():
    ans_index = alpha_lower.index(answer) + 1
  elif answer.isupper():
    ans_index = alpha_upper.index(answer) + 1

  # Check if aus_index set, if not dont run, if so check if correct and add points if so

  if Q[ans_index] == Q[5]: 
    score += 100
    print("\nCorrect!")
    print("\nYour score is {score}!".format(score=score))
    n += 1
  else:
    print("\nIncorrect! You are bad!")
    print("\nThe correct answer was {answer}.\n".format(answer=Q[5]))
    n += 1

print("\nFinal score was {score} out of 1500!".format(score=score))

if score == 1500:
  print('\n You are officially a millionare!!!\n')
else:
  print('\nShut up and stop crying! You are a failure and your parents hate you!\n')