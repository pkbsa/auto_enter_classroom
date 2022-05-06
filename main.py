import time
from datetime import datetime
from pynput.keyboard import Controller,Key
from data import lst
import webbrowser

keyboard = Controller()

Status = False

print("### Starting the program ###")
print(f"-- date {datetime.now().day} time [{datetime.now().hour}:{datetime.now().minute}]")
print(" ")

for i in lst :
    itime = (int(i[2].split(':')[0]))*60 + int(i[2].split(':')[1])
    #print(" ")
    print(f"Next Subject : {i[4]}")
    print(f"Class time [{i[1]}]")
    #print(" ")
    while True :
        currenttime = (datetime.now().hour*60) + datetime.now().minute
        #print("currtime :",currenttime)
        if Status == False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]) and datetime.now().day == i[3] :
                print("======= In =======")
                print("Class time :", int(i[1].split(':')[0]),":",int(i[1].split(':')[1]))
                print("Subject :", i[4])
                print(i[0])
                webbrowser.open(i[0])
                time.sleep(5)
                keyboard.press(Key.enter)
                time.sleep(2)
                keyboard.press(Key.enter)
                Status = True
        elif Status == True :
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]) :
                print("ออกห้องได้แล้วจ้า")
                print("===== Out =====")
                print(" ")
                time.sleep(1)
                Status = False
                break
        if Status == False and currenttime > itime and datetime.now().day >= i[3] :
            break