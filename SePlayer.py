import os,sys,SeLector
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep

X_SIZEMOD = 1
X_OFFSET = 0
Y_SIZEMOD = 35
Y_OFFSET = -10

'''This method shall an int (window) as args'''
def instanceReader(window):
    print(window)
    if os.path.isfile(f".cache/SEPLAYER_{window}") == False:
        return "file:///fff"
    with open(f'.cache/SEPLAYER_{window}', 'r') as f:
        file_name = f.read()
        return file_name

def resolutionParser(window,resolutions):
    x_size = int(resolutions["width"]) // 2 - X_SIZEMOD
    y_size = int(resolutions["height"]) // 2 - Y_SIZEMOD
    x_pos = x_size - X_OFFSET
    y_pos = y_size - Y_OFFSET
    
    if window == 2:
        return [x_pos,0,x_size,y_size]
    if window == 3:
        return [0,y_pos,x_size,y_size]
    if window == 4:
        return [x_pos,y_pos,x_size,y_size]
    return [0,0,x_size,y_size]

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
    

    file_name = instanceReader(window)
    print(file_name)
    #start webdriver of correct size/position
    opts = Options()
    opts.add_argument("--kiosk")

    first_pass = True

    with Firefox(options=opts) as driver:
        resolutions = driver.get_window_size()
        parsed_resolutions = resolutionParser(window,resolutions)
        driver.get(file_name)
        if first_pass:
            driver.set_window_position(parsed_resolutions[0],parsed_resolutions[1])
            driver.set_window_size(parsed_resolutions[2],parsed_resolutions[3])
            first_pass = False

        while(True):
            temp = instanceReader(window)
            if file_name == temp:
                sleep(1)
                continue
            file_name = temp
            driver.get(file_name)




if __name__ == "__main__":
    window = 1
    for i in sys.argv[1:]:
        if "-w=" in i[:3]:
            window = int(i[3])


    driverLauncher(window)
    