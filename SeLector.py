import re,os,sys
from pathlib import Path
from random import choice

FILE_EXTENSIONS = ".avi$|.mov$|.mp4$|.flv$|.wmv$"

def instanceWriter(name,window=None):
    if os.path.isdir(".cache") == False:
        os.mkdir(".cache")

    with open(f".cache/SEPLAYER_{window}", "w") as f:
        f.write(f"file://{name}")

def videoSelector(directory,substring):
    file_list = os.listdir(directory)
    final_list = [i for i in file_list if ((re.search(FILE_EXTENSIONS, i)) \
        and (substring.lower() in i.lower()))]
    choice_file = choice(final_list)
    return f"{directory}{choice_file}"

if __name__ == "__main__":
    directory, substring, window = "./", "", 0
    for i in sys.argv[1:]:
        if "-d=" in i[:3]:
            directory = i[3:]
        elif "-n=" in i[:3]:
            name_arg = i[3:]
        elif "-w=" in i[:3]:
            window = int(i[3])
        elif ("-h" in i[:2]):
            with open('help.txt', 'r') as f:
                file_contents = f.read()
                print (file_contents)
            exit(1)
        else:
            print('Unrecognized Command: Enter -h as an arg to see help text' )
            exit(0)

    video = videoSelector(directory,substring)
    print(video)
    instanceWriter(video,window)