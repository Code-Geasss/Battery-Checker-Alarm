This project was a small idea to save my laptop, my previous laptop lost it's ability bcoz of me not taking care of it's battery.

Thus I thought of writing a script which can save laptops/ computers from losing their power. Help was taken from stack-overflow posts :)

First of all install the requirements.txt file by the command => (pip install requirements.txt)

Execute the battery_checker.py file => (python battery_checker.py) # command for windows


Note:- At the top of the tkinter window, u might see this->(NOT  RESPONDING) written, but don't worry, as the application uses some inbuilt     drivers/softwares it is showing us that...

A tkinter dialog box will appear, write the percentage of battery, so that as soon battery level reaches below your provided battery level,
an alarm will be turned on for 7 seconds. (you can change the time limit of alarm acc. to your desire by going in the battery_checker.py file and 

                            inside ->>>def alarm():
                                          for x in range(7  -> change this number))
                                          
                                        
                                        