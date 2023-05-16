from tkinter import *
import customtkinter as ctk

#this is the start of the project
"""
Topic: Doing a software that helps keep score for cricket games

Your program must keep track of the two opposing teams. The user should be able to enter data on a ball-by-ball basis. 
Each ball should result in either a hit (with an amount of runs attached), a wide, a no-ball or a pass ball (with an amount of runs attached). 
The program should keep track of overs, providing indication when it’s time to swap ends. It should also keep track of outs, 
storing the bowler’s name whenever a batter gets out.

"""
root = ctk.CTk()
root.title('Cricket Scorecard')
ctk.set_appearance_mode("dark")

class player: #creating a class for player that will be used to store the statistics of each player later on
    def __init__(self,name):
        self.name = name
    runs = 0
    balls = 0

team1 = []
team2 = []

StartingScreen = ctk.CTkFrame(master=root, width=900, height=700) #This frame is the screen that the user opens the app into
StartingScreen.pack()

teamOneFrame = ctk.CTkScrollableFrame(StartingScreen, width = 450, height=600) #frame containing name entry for team one
teamOneFrame.grid(row=0, column = 0)
teamOneHeader = ctk.CTkLabel(teamOneFrame,text="TEAM 1", fg_color="transparent", font = ("Montserrat",24),padx = 10, pady = 3)
teamOneHeader.grid(row = 0, column = 0)
teamOneName = ctk.CTkEntry(teamOneFrame,placeholder_text="Enter team 1 name",width=300)
teamOneName.grid(row=0,column=1)

teamTwoFrame = ctk.CTkScrollableFrame(StartingScreen, width = 450, height=600) #frame containing name entry for team two
teamTwoFrame.grid(row=0, column = 1)
teamOneHeader = ctk.CTkLabel(teamTwoFrame,text="TEAM 2", fg_color="transparent", font = ("Montserrat",24),padx = 10, pady = 3)
teamOneHeader.grid(row = 0, column = 0)
teamTwoName = ctk.CTkEntry(teamTwoFrame,placeholder_text="Enter team 2 name",width=300)
teamTwoName.grid(row=0,column=1)





root.mainloop()
