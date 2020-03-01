import os,sys,SeLector
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep


'''This method shall an int (window) as args'''
def instanceReader(window):
    if os.path.isfile(f".cache/SEPLAYER_{window}") == False:
        return "file:///fff"
    with open(f'.cache/SEPLAYER_{window}', 'r') as f:
        file_name = f.read()
        return file_name

def resolutionParser(window):
    resolution_list = []
    return resolution_list


'''
This method shall take an int (window) as args.
1.) The correct resolution list shall be gained from the resolutionParser method
2.) A webdriver of the correct size/position shall be launched with the default loading page
3.) A while(true) loop shall be launched
    a.) A value named "temp" shall be read from the corresponding .cache/SP_{window} file
    b.) temp shall be compared to file_name
        IF EQUAL the program shall sleep for 1 second and restart
    c.) file_name shall be set equal to temp
    d.) the webdriver shall load the new file_name
'''
def driverLauncher(window):
    
    resolution_list = resolutionParser(window)
    file_name = instanceReader(window)
    print(file_name)
    #start webdriver of correct size/position
    opts = Options()
    opts.add_argument("--kiosk")

    first_pass = True

    with Firefox(options=opts) as driver:
        driver.get(file_name)
        if first_pass:
            driver.set_window_position(100,100)

            first_pass = False

        while(True):
            temp = instanceReader(window)
            if file_name == temp:
                sleep(1)
                continue
            file_name = temp
            driver.get(file_name)




if __name__ == "__main__":
    window = int(sys.argv[1])

    driverLauncher(window)
    