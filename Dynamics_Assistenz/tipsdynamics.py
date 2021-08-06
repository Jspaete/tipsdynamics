##################################################
'''
This programm allows you to look at tips on different levels. The first tip should help you less than the next one and so on. 
The goal is that you can solve the exercise on your level without looking at the solutions. 
How it works?:
    You have two functions: overview(week) and show_ex(week,exercise)
    IMPORTANT: Each week you have to download on my polybox all new files and store it in the
    same folder as you stored the programm. These files are pickels or images.
    IMPORTANT 2: You have to have installed matplotlib, dill, glob and ipython. 
    Look on my website to find out how to do this. https://n.ethz.ch/~jspaete
    password for the polybox is: Havefun:)
    For each exercise I defined one to three tips. 
    IMPORTANT 3: At first you have to run the file bevor starting. For that you need a integrated terminal. 
    If you can't find it, you will find informations here: https://code.visualstudio.com/docs/editor/integrated-terminal 
    Then type into the terminal:
    - ipython or python3 -i
    - run itpsdynamics.py
    Then you can start.
Functions:
-   overview(week)
    Purpose:    To know how many tips for each week and exercise exist
    Example:    if you want to know it for week 1, you have to press: overview(1)
                w1e2a stands for week 1 exercise 2a
-   show_ex(week,'exercise') 
    The ' around the exercise are IMPORTANT and you need to write them!
    Purpose:    To know a tip for a specific week and exercise
    Example:    You want to know the tip for exercise 3a in week 1, you have to type: show_ex(1,'3a')
                The programm will then ask you, if you want to get another tip. 
                If you type "yes" it will give you the next tip which should help you more than the last one.
                If you don't want to get anouther tip, type "no".

copyright
'''
##################################################
import dill
import glob
from PIL import Image
import PIL
#To define new classes, type 

class Tip():
    def __init__(self,name):
        self.name = name
        self.t = []
        self.p = []
        self.define()


    def define(self):
        definition_stop = 'no'
        tip_nmbr = 1
        while definition_stop != 'yes':
            self.t += [input('give now '+ str(tip_nmbr)+'. tip: ')]
            self.p += [input('picture? give file name: ')]
            tip_nmbr+=1
            definition_stop = input('definitions done? ')
        save_yes = input('save now? ')
        if save_yes == 'yes':
            self.save()

    def get_tip(self,tip_nmbr):
        if self.t[tip_nmbr] != '0':
            print(self.t[tip_nmbr])
        if self.p[tip_nmbr] != '0':
            img = Image.open(self.p[tip_nmbr])
            img.show()
    
    def check_tip(self,tip_nmbr):
        if len(self.t) > tip_nmbr or len(self.p) > tip_nmbr:
            return 1
        else :
            return 0

def overview(week):
    tips_container = load_w(week)
    for i in tips_container.keys():
        print(f'exercise: {i}')
        print(f'Tips: {tips_container[i].length()} \n')

def show_ex(week,exercise):
    tip_nmbr = 0
    next_tip = 'yes'
    while next_tip != 'no':
        tips_container = load_w(week)
        if tips_container[f'w{week}e{exercise}'].check_tip(tip_nmbr) == 1:
            tips_container[f'w{week}e{exercise}'].get_tip(tip_nmbr)
            next_tip = input('Do you want to get another tip? ')
            tip_nmbr += 1
        else:
            print("There is no next tip for this exercise")
            next_tip = "no"


def load_w(week):
    tips_container = {}
    filenames = glob.glob(f"w{week}*.pickle") #am ende dieser definition wird filenames wieder gelöscht
    for filename in filenames: 
        with open(filename,'rb') as f:
            tips_container[filename[:-7]] = dill.load(f)
            tips_container.keys()
    return dict(sorted(tips_container.items()))#das ist der dictionary


