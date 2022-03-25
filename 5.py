# send unlimited messages
import pyautogui as mess
import time as ti

limit = input("Enter number = ")
msg = input("Message you want to send = ")
print("Wait 5 second")

i = 0
ti.sleep(5)
while i < int(limit):
    mess.typewrite(msg)
    mess.press('Enter')
i += 1