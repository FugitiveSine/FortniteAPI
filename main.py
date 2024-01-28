import fortnite_api
from fortnite_api import Account
from fortnite_api import BrPlayerStats #import class
import tkinter as tk
import PIL
from tkinter import *
from PIL import ImageTk, Image
import os

root = tk.Tk()
root.title("Fortnite Item Shop")
root.geometry('800x500')
api = fortnite_api.FortniteAPI("57f41e4a-cb97-4471-a4fa-a09d41695146")
userID = "08fce4917cf343e99868269d35489098"
userName = "sine on zaza"
def getFortniteDate():
    aShop = api.shop.fetch()
    aShop.date.date()#gets todays fortnite shop date (+1 day)

usrStats = api.stats.fetch_by_name(userName)
player_data = {}
#thing = BrPlayerStats(userID, player_data)
print(usrStats.battle_pass.level)
#print()


root.mainloop()
