import pyautogui as pt
import time

print("After putting the limit and message, open the chatbox of the user you want to spam to")

limit = input("\nEnter the limit:")

message = input("\nEnter the message:")

i = 0
time.sleep(5)

while i < int(limit):
    pt.typewrite(message)
        
    pt.press("enter")

    i+=1
