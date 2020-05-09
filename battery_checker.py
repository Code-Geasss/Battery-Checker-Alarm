import psutil
import tkinter
import winsound
import time
import math




def secs2hours(secs):
    #divmod(a, b) means:-
    # a and b : b divides a
    mm, ss = divmod(secs, 60) #The divmod() is part of python’s standard library which takes two numbers as parameters and gives the quotient and remainder of their division as a tuple.
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)



def countdown(count): 
    flag = 0

    battery = psutil.sensors_battery()
    if battery.percent > count:

        while battery.percent > count:
            battery = psutil.sensors_battery()
            print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))

            if battery == count:
                flag = 1
                alarm()
            time.sleep(40)
        
        if flag == 0:
            alarm()
    else:
        hoursT=tkinter.Label(top, text='''Enter the battery percentage at which you
           want to get a alarm:''',fg="black",font='Helvetica 9 bold')
        label['fg']="black"
        label['relief']="ridge"
        label['font'] = "self.bold_font"
        label['bg']="red"
        label['text'] = "Your battery percentage is lesser than the limit set by u"
        
        
def updateButton():            
    hour = hoursE.get()
    if hour.isdigit():
        time = int(hour)
        if time >= 0 and time <= 100:
            countdown(time)
        else:
            hoursT=tkinter.Label(top, text='''Enter the battery percentage at which you
            want to get a alarm:''',fg="black",font='Helvetica 9 bold')
            label['fg']="black"
            label['relief']="ridge"
            label['font'] = "self.bold_font"
            label['bg']="red"
            label['text'] = "Please enter the battery limit less than 100 % and greater than 0 % "

    

def alarm():
    for x in range(7):
        winsound.Beep(1000,1000) #1000, 1000 sound ka frequency h,I tried diff. ones but others were quite bad :(
    label['fg']="black"
    label['relief']="ridge"
    label['font'] = "self.bold_font"
    label['bg']="light blue"
    label['text'] ="Please charge your device the battery has reached your set limit"
    
        

top = tkinter.Tk()
top.geometry("800x600")
hoursT=tkinter.Label(top, text='''Enter the battery percentage at which 
          you want to get a alarm:''',fg="black",font='Helvetica 16 bold')
hoursE=tkinter.Entry(top)
minuteT=tkinter.Label(top, text="(Please input integer values only)",fg="black")


hoursT.grid(row=3,column=1)
hoursE.grid(row=3,column=3,padx=10,pady=10,ipady=3)
minuteT.grid(row=4,column=1)


label = tkinter.Label(top) #pata nhi "top" dalne se and nhi dalne se kuchh farak nhi padta h...
label.grid(row=10,column=1) #this is to show the final alarm output



button=tkinter.Button(top,text="Start Countdown",command=updateButton) #try to pass msg in this updateButton function() .................................................................
button.grid(row=8,column=3)



top.mainloop()