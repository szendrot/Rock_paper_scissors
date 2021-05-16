# Write your code here
import random
random.seed()

name = input('Enter your name:')
print('Hello, ' + name)

my_option_str = input()
if my_option_str == '':
    my_option_list = ['paper', 'rock', 'scissors']
else:
    my_option_list = my_option_str.split(',')

all_options_list =['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']

print("Okay, let's start")

file = open('rating.txt', 'r')
score_list = file.readlines()
file.close()
score_list_m = []
for words in score_list:
    score_list_m.append(words.replace('\n', ''))
score_list_new = ' '.join(score_list_m).split()
score_dict = {score_list_new[n] : score_list_new[n + 1] for n in range(0, len(score_list_new), 2)}
if name in score_dict:
    score = int(score_dict[name])
else:
    score = 0

while True:
    my_option = random.choice(my_option_list)
    your_option = input()
    if your_option in all_options_list:
        your_index = all_options_list.index(your_option, 15, 30)
        you_win_list = all_options_list[your_index-1:your_index-8:-1]   
    else:
         None
   
    if your_option == '!exit':
        break

    elif your_option == '!rating':
        print('Your rating: ' + score_dict[name] if score == 0 and name in score_dict else 'Your rating: ' + str(score))

    elif your_option not in my_option_list:
        print('Invalid input')

    elif my_option == your_option:
        score += 50
        print('There is a draw (' + my_option + ')')

    elif my_option in you_win_list: 
        score += 100
        print('Well done. The computer chose ' + my_option + ' and failed')
        
    
    else:
        print('Sorry, but the computer chose ' + my_option)

