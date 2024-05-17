from colorama import Fore 
import sys 
import random 
import time 
colors=[Fore.RED,Fore.YELLOW,Fore.GREEN,Fore.BLUE,Fore.CYAN,Fore.MAGENTA,Fore.RESET]
def loop_over(sequence,delay_time,text_color):
  for text in sequence:
    sys.stdout.flush()
    time.sleep(delay_time)
    sys.stdout.write(f'{text_color}{text}')
  else:
    print(f'{colors[-1]}')

try:
  number_of_random_integers_user_wants=int(input('How many random integers do you want?'))
  random_numbers_list=[]
  time.sleep(1)
  start=int(input('Start:'))
  time.sleep(1)
  end=int(input('end:'))
  if end<start:
    time.sleep(1)
    loop_over('The end value should be bigger than the start value.\nRestart the program in order to use it again',0.1,colors[0])
    time.sleep(1)
    sys.exit(loop_over('Exitting program...',delay_time=0.1,text_color=colors[0]))
  else:
   for n in range(number_of_random_integers_user_wants):
    random_numbers_list.append(random.randrange(start,end+1,1))
   else:
    time.sleep(1)
    loop_over(sequence=f'{random_numbers_list}',delay_time=0.001,text_color=colors[-3])
    time.sleep(1)
    pick_integer=int(input('integer:'))
    while pick_integer not in random_numbers_list:
      time.sleep(1)
      loop_over(sequence=f'Error,{pick_integer} is not in the list\n',delay_time=0.01,text_color=colors[0])
      pick_integer=int(input('integer:'))
      if pick_integer in random_numbers_list:
        break 
    else:
      time.sleep(1)
      loop_over(sequence=f'{pick_integer} is in the list at the index of {random_numbers_list.index(pick_integer)}.',text_color=colors[2],delay_time=0.1)
except ValueError:
  loop_over(sequence='Error, you need to enter an integer')