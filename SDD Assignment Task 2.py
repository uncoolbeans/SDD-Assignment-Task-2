from tkinter import *
import customtkinter as ctk

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
root.geometry("900x700")

class player: #creating a class for player that will be used to store the statistics of each player later on
    def __init__(self,name):
        self.name = name
    runs = 0
    balls = 0

def switchToNewScreen(oldFrame,newFrame):
    oldFrame.forget()
    newFrame.pack()
    return

def closeProgram():  #what does this do?????????????
    root.quit()
    return

team1Players = []
team2Players = []

"""
Starting menu screen
"""

menuScreen = ctk.CTkFrame(master=root, width = 900, height = 700) #screen that the user sees when they first open the program

beginButton = ctk.CTkButton(menuScreen, text = "New Game", anchor =  'center', width = 300, height = 100,  command=lambda: switchToNewScreen(menuScreen,startingScreen))
exitButton = ctk.CTkButton(menuScreen,text = "EXIT",anchor =  'center', width = 300, height = 100,  hover = True, command=closeProgram)
titleLabel = ctk.CTkLabel(menuScreen, text = 'Cricket Score Tracker', fg_color= 'transparent', anchor= 'center', font = ("Montserrat",30),padx = 10, pady=50)
titleLabel.pack()
beginButton.pack(pady = 10)
exitButton.pack(pady = 10)
menuScreen.pack(fill = 'both', expand = 1)


"""
Team information entry screen
"""
startingScreen = ctk.CTkFrame(master=root, width=900, height=700) #This frame is the screen that the user opens the app into


teamOneFrame = ctk.CTkScrollableFrame(startingScreen, width = 450, height=600) #frame containing name entry for team one
teamOneFrame.grid(row=0, column = 0)
teamOneHeader = ctk.CTkLabel(teamOneFrame,text="TEAM 1", fg_color="transparent", font = ("Montserrat",24),padx = 10, pady = 3)
teamOneHeader.grid(row = 0, column = 0)
teamOneName = ctk.CTkEntry(teamOneFrame,placeholder_text="Enter team 1 name",width=300)
teamOneName.grid(row=0,column=1)

teamTwoFrame = ctk.CTkScrollableFrame(startingScreen, width = 450, height=600) #frame containing name entry for team two
teamTwoFrame.grid(row=0, column = 1)
teamOneHeader = ctk.CTkLabel(teamTwoFrame,text="TEAM 2", fg_color="transparent", font = ("Montserrat",24),padx = 10, pady = 3)
teamOneHeader.grid(row = 0, column = 0)
teamTwoName = ctk.CTkEntry(teamTwoFrame,placeholder_text="Enter team 2 name",width=300)
teamTwoName.grid(row=0,column=1)

nextButton = ctk.CTkButton(startingScreen,text='Next', width=900, height = 100, command = switchToNewScreen)
nextButton.grid(row=1,column=0,columnspan = 2)

"""
Game score screen
"""

gameFrame = ctk.CTkFrame(master=root, width= 900, height = 700)





root.mainloop()
