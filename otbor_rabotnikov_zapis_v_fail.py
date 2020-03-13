import string
import keyboard
import sys
import os
d={
    'question_1':
    {'question':'Do you have experience at least 5 years?',
      'answer':'yes'},
    'question_2':
    {'question':'Would you like to have salary 1000eur?',
      'answer':'yes'},
    'question_3':
    {'question':'would you like to work from office?',
    'answer':'yes'}
   }
chosed={}
unchosed={}


answer=''
def get_iput_from_user():
    return input("Enter response... ")


def ifchosed(chosed):
    chosed.get(name)
    fail=open('vastuvõetud.txt','a')#zapisali
    fail.write(name+'\n')
    fail.close()
    return name

def ifunchosed(unchosed):
    unchosed.get(name)
    fail=open('eisobi.txt','a')#zapisali
    fail.write(name+'\n')
    fail.close()
    return name
def yes_no():
    answer=input("yes/no")
    if answer=="yes":
        get_iput_from_user()
    elif answer=="no":
        print("Sorry, your background is does not suit us!")
        ifunchosed(unchosed)
        sys.exit()


print("What is your name? ")
name=get_iput_from_user()
print(f"{name}, do you know python?")
python=yes_no()
try:
    print(f"{name},", d['question_1']['question'],'yes/no')
    if get_iput_from_user()==d['question_1']['answer']:
        print("One more question")
        print(f"{name},", d["question_2"]['question'],'yes/no')
        if get_iput_from_user()==d['question_2']['answer']:
            print("One more question")
            print(f"{name},", d['question_3']['question'],'yes/no')
            if get_iput_from_user()==d['question_3']['answer']:
                print("Okey, we will give you feedback as soos as possible!")
                ifchosed(chosed)
            else:
                print("We work only in the office")
                ifunchosed(unchosed)
        else:
            print("Okey")
            ifunchosed(unchosed)
    else:
        print("Thank you!")
        ifunchosed(unchosed)
except:
    ValueError




f=open("vastuvõetud.txt", "r")
if f.mode == 'r':
    contents =f.read()
    print(contents)

f2=open("eisobi.txt", "r")
if f2.mode == 'r':
    contents =f2.read()
    print(contents)
