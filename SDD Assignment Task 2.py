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

class ScoringFrame(ctk.CTkFrame): #This is the frame that displays the team information and allows user to update game statistics for a team
    def __init__(self, master, teamName, players):
        super().__init__(master, width=900, height = 700)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        teamName = teamName
        players= players

        self.TeamLabel = ctk.CTkLabel(self, text= teamName, 
                                      fg_color= 'grey', 
                                      font = ("Bahnschrift SemiBold",30), 
                                      width= 400, height = 50, 
                                      corner_radius= 10, 
                                      anchor = 'w')
        
        self.TeamLabel.grid(column = 0, row = 0)

        self.batterLabel = ctk.CTkLabel(self, text= 'Batting team', 
                                      fg_color = 'transparent', 
                                      bg_color = 'transparent',
                                      font = ("Bahnschrift SemiBold",18),
                                      anchor = 'w',
                                      justify = 'left'
                                    )
        
        self.batterLabel.grid(column = 0, row = 1)

        self.emptyLabel = ctk.CTkLabel(self, text= '',width = 500, fg_color = 'transparent', bg_color = 'transparent')
        self.emptyLabel.grid(column = 1, row = 0, columnspan = 2)

        self.emptyLabel2 = ctk.CTkLabel(self, text= '',width = 500, fg_color = 'transparent', bg_color = 'transparent')
        self.emptyLabel2.grid(column = 1, row = 1, columnspan = 2)
                    
                                

        #for player in players:
        #    self.playerLabel = ctk.CTkLabel(self, text = player.name)
        #    self.playerLabel.pack()

            

def switchToNewScreen(oldFrame,newFrame): #general switch screen function
    oldFrame.forget()
    newFrame.pack()
    return

def startGame(oldFrame, newFrame, t1Name, t2Name, t1Entries, t2Entries):

    t1_name = t1Name.get()
    t2_name = t2Name.get()
    t1Players = []
    t2Players = []
    for textbox in t1Entries:
        name = textbox.get()
        t1Players.append(player(name))

    for textbox in t2Entries:
        name = textbox.get()
        t2Players.append(player(name))

    global t1ScoreFrame 
    global t2ScoreFrame

    t1ScoreFrame = ScoringFrame(newFrame,t1_name,t1Players)
    t2ScoreFrame = ScoringFrame(newFrame,t2_name,t2Players)

    oldFrame.forget()
    newFrame.pack()
    t1ScoreFrame.pack()
    return


def closeProgram():  #exits program
    root.quit()
    return


team1Players = []
team2Players = []

"""
Starting menu screen
"""
menuScreen = ctk.CTkFrame(master=root, width = 900, height = 700) #screen that the user sees when they first open the program

beginButton = ctk.CTkButton(menuScreen, text = "New Game", anchor =  'center',
                             width = 300, height = 100,  
                            command=lambda: switchToNewScreen(menuScreen,entryScreen), 
                            font = ("Bahnschrift SemiBold",30))

exitButton = ctk.CTkButton(menuScreen,text = "EXIT",anchor =  'center', 
                           width = 300, height = 100,  
                           hover = True, 
                           command=closeProgram, 
                           font = ("Bahnschrift SemiBold",18))

titleLabel = ctk.CTkLabel(menuScreen, text = 'Cricket Score Tracker', 
                          fg_color= 'transparent', 
                          anchor= 'center', 
                          font = ("Bahnschrift SemiBold",30),
                          padx = 10, pady=50)
titleLabel.pack()
beginButton.pack(pady = 10)
exitButton.pack(pady = 10)
menuScreen.pack(fill = 'both', expand = 1)


"""
Team information entry screen
"""
entryScreen = ctk.CTkFrame(master=root, width=900, height=700) #This frame is the screen that the user opens the app into


teamOneFrame = ctk.CTkScrollableFrame(entryScreen, width = 435, height=600) #frame containing name entry for team one
teamOneFrame.grid(row=0, column = 0)
teamOneHeader = ctk.CTkLabel(teamOneFrame,text="TEAM 1", fg_color="transparent", font = ("Bahnschrift SemiBold",30))
teamOneHeader.grid(row = 0, column = 0, pady = 10, padx = 5)
teamOneName = ctk.CTkEntry(teamOneFrame,placeholder_text= "Team name",width=250, height = 50, font = ('Bahnschrift SemiBold', 18))
teamOneName.grid(row=0,column=1, pady = 10)

t1p1_entry = ctk.CTkEntry(teamOneFrame, placeholder_text="Player 1",width=300)
t1p2_entry = ctk.CTkEntry(teamOneFrame, placeholder_text="Player 2",width=300)
t1p3_entry = ctk.CTkEntry(teamOneFrame, placeholder_text="Player 3",width=300)
t1p4_entry = ctk.CTkEntry(teamOneFrame, placeholder_text="Player 4",width=300)
t1p5_entry = ctk.CTkEntry(teamOneFrame, placeholder_text="Player 5",width=300)
t1p6_entry = ctk.CTkEntry(teamOneFrame, placeholder_text="Player 6",width=300)
t1p7_entry = ctk.CTkEntry(teamOneFrame, placeholder_text="Player 7",width=300)
t1p8_entry = ctk.CTkEntry(teamOneFrame, placeholder_text="Player 8",width=300)
t1p9_entry = ctk.CTkEntry(teamOneFrame, placeholder_text="Player 9",width=300)
t1p10_entry = ctk.CTkEntry(teamOneFrame, placeholder_text="Player 10",width=300)
team1Entries = [t1p1_entry,t1p2_entry,t1p3_entry,t1p4_entry,t1p5_entry,t1p6_entry,t1p7_entry,t1p8_entry,t1p9_entry,t1p10_entry]

for count,entry in enumerate(team1Entries):
    entry.grid(row = count+1, pady = 10, columnspan = 2, column = 0)
    pass

teamTwoFrame = ctk.CTkScrollableFrame(entryScreen, width = 435, height=600) #frame containing name entry for team two
teamTwoFrame.grid(row=0, column = 1)
teamOneHeader = ctk.CTkLabel(teamTwoFrame,text="TEAM 2", 
                             fg_color="transparent", 
                             font = ("Bahnschrift SemiBold",30),
                             padx = 10, pady = 3)

teamOneHeader.grid(row = 0, column = 0, pady = 10, padx = 5)
teamTwoName = ctk.CTkEntry(teamTwoFrame,placeholder_text= "Team name",
                           width=250, height = 50, 
                           font = ('Bahnschrift SemiBold', 18))
teamTwoName.grid(row=0,column=1, pady = 10)

t2p1_entry = ctk.CTkEntry(teamTwoFrame, placeholder_text="Player 1",width=300)
t2p2_entry = ctk.CTkEntry(teamTwoFrame, placeholder_text="Player 2",width=300)
t2p3_entry = ctk.CTkEntry(teamTwoFrame, placeholder_text="Player 3",width=300)
t2p4_entry = ctk.CTkEntry(teamTwoFrame, placeholder_text="Player 4",width=300)
t2p5_entry = ctk.CTkEntry(teamTwoFrame, placeholder_text="Player 5",width=300)
t2p6_entry = ctk.CTkEntry(teamTwoFrame, placeholder_text="Player 6",width=300)
t2p7_entry = ctk.CTkEntry(teamTwoFrame, placeholder_text="Player 7",width=300)
t2p8_entry = ctk.CTkEntry(teamTwoFrame, placeholder_text="Player 8",width=300)
t2p9_entry = ctk.CTkEntry(teamTwoFrame, placeholder_text="Player 9",width=300)
t2p10_entry = ctk.CTkEntry(teamTwoFrame, placeholder_text="Player 10",width=300)
team2Entries = [t2p1_entry,t2p2_entry,t2p3_entry,t2p4_entry,t2p5_entry,t2p6_entry,t2p7_entry,t2p8_entry,t2p9_entry,t2p10_entry]

for count,entry in enumerate(team2Entries):
    entry.grid(row = count+1, pady = 10, columnspan = 2, column = 0)
    pass

nextButton = ctk.CTkButton(entryScreen,text='Next', 
                           font = ("Bahnschrift SemiBold",18),
                           width=900, height = 100, 
                           command = lambda: startGame(entryScreen,gameFrame,teamOneName,teamTwoName,team1Entries,team2Entries))

nextButton.grid(row=1,column=0,columnspan = 2)


"""
Game Frame (contains the frames for team 1 and 2)
"""
gameFrame = ctk.CTkFrame(root,width = 900, height = 700)


root.mainloop()
