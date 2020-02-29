import re,os,sys
from selenium import webdriver
from pathlib import Path
from random import choice

FILE_EXTENSIONS = ".avi$|.mov$|.mp4$|.flv$|.wmv$"

def instanceWriter(name,window):
    with open(f'.cache/MULTIPLAYER_{window}', 'w') as f:
        f.write(name)

def videoSelector2(directory=None,filter=""):
    if directory == None:
        directory = (os.path.dirname(os.path.realpath(__file__)))
    file_list = os.listdir(directory)
    pattern = ".avi$|.mov$|.mp4$|.flv$|.wmv$"

    final_list = [x for x in file_list if \
        ((re.search(pattern, x)) and (filter.lower() in x.lower()))]
    choice_file = choice(final_list)
    return choice_file

def videoSelector(directory="./",substring=""):
    file_list = os.listdir(directory)
    final_list = [i for i in file_list if((re.search(FILE_EXTENSIONS, i)) and (substring.lower() in i.lower()))]
    choice_file = choice(final_list)
    return choice_file

if __name__ == "__main__":
    directory, substring = "./", ""
    for i in sys.argv[1:]:
        if "-d=" in i[:3]:
            directory = i[3:]

    
    print(videoSelector(directory, substring))