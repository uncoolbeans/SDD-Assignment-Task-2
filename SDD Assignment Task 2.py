from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import sys 
import os

"""
Topic: Doing a software that helps keep score for cricket games

Your program must keep track of the two opposing teams. The user should be able to enter data on a ball-by-ball basis. 
Each ball should result in either a hit (with an amount of runs attached), a wide, a
 no-ball or a pass ball (with an amount of runs attached). 
The program should keep track of overs, providing indication when it’s time to swap ends. It should also keep track of outs, 
storing the bowler’s name whenever a batter gets out.

"""
root = ctk.CTk()
root.title('Cricket Scorecard')
ctk.set_appearance_mode("dark")
root.geometry("900x700")


"""
Game Tab View (contains the frames for team 1 and 2)
"""
gameTab = None

class player: #creating a class for player that will be used to store the statistics of each player later on
    def __init__(self,name):
        self.name = name
    runs = 0
    balls = 0

"""
Score frame for each team
"""
t1ScoreFrame = None #global variables to serve as variables for storing the score frames
t2ScoreFrame = None
endFrame = None

class ScoringFrame(ctk.CTkFrame): #This is the frame that displays the team information and allows user to update game statistics for a team
    def __init__(self, master, teamName, playersEntries, opposingEntries, teamNum):
        super().__init__(master, width=900, height = 1000)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.teamName = teamName #displayed team name
        teamNum = teamNum 
        self.players = [] #displayed team players
        self.opposing = [] #opposing team players

        for textbox in playersEntries:
            name = textbox.get()
            self.players.append(name)

        for textbox in opposingEntries:
            name = textbox.get()
            self.opposing.append(name)

        self.teamRuns = 0
        self.teamNoBalls = 0
        self.teamWickets = 0
        self.wideBalls = 0
        self.overs = 0
        self.totalBalls = 0
        self.battersOut = []
        global gameTab
        
        def addWickets(wickets): #function to add wickets
            if self.teamWickets == 10:
                return
            self.teamWickets += wickets
            self.wicketCounter.configure(text = str(self.teamWickets))
            return
        
        def removeWickets(wickets): #function to remove wickets
            if self.teamWickets > 0:
                self.teamWickets -= wickets
            self.wicketCounter.configure(text = str(self.teamWickets))
            return

        def addRuns(runs): #function to be called when runs added
            self.teamRuns += runs
            self.totalBalls += 1
            self.runsLabel.configure(text=str(self.teamRuns))
            self.ballsLabel.configure(text = str(self.totalBalls))
            self.oversIndicator.configure(text = str(round((self.totalBalls/6),2)))
            return
        
        def removeRuns(runs): #function to be called when run removed
            if self.teamRuns > 0 and self.teamRuns >= runs:
                self.teamRuns -= runs
            self.runsLabel.configure(text=str(self.teamRuns))
            return
        
        def removeBatter(): #function to remove batter
            batter = self.batterSelect.get()
            bowler  = self.bowlerSelect.get()
            if batter not in self.players or bowler not in self.opposing:
                messagebox.showerror('Error', 'Error: Please select a valid batter and bowler!')
                print(teamNum)
                print(self.players)
                print(self.opposing)

            else:
                self.battersOut.insert(0,[batter,bowler])
                self.players.remove(batter)
                self.batterSelect.configure(values = self.players)
                self.remainingBattersLabel.configure(text = f'Remaining batters:\n{len(self.players)}')
                if len(self.players) == 0:
                    messagebox.showwarning('Swap batting teams', 'All batters are out, swap batting teams!')

            self.batterSelect.set('Select batter')
            self.bowlerSelect.set('Select bowler')

            for row,out in enumerate(self.battersOut): #refreshing the display of batter outs
                nameFrame = ctk.CTkFrame(self.outsFrame, height = 20, width = 210)
                batterName = ctk.CTkLabel(nameFrame, text = out[0], width = 70)
                middle = ctk.CTkLabel(nameFrame, text = 'out by', width = 70)
                bowlerName = ctk.CTkLabel(nameFrame,text = out[1], width = 70)
                batterName.grid(row = 0, column = 0, padx = 3)
                middle.grid(row = 0, column = 1, padx = 3)
                bowlerName.grid(row = 0, column = 2, padx = 3)
                nameFrame.grid(row = row, column = 0, columnspan = 2, pady = 5)
            return
        
        def addNoBall(n): #function to add/subtract the number of no balls
            self.teamNoBalls += n
            self.teamRuns += n
            if self.teamRuns < 0:
                self.teamRuns = 0
            if self.teamNoBalls < 0:
                self.teamNoBalls = 0
            self.noBallLabel.configure(text = str(self.teamNoBalls))
            self.runsLabel.configure(text = str(self.teamRuns))
            return
        
        def addWideBall(n): #function to add/subtract the number of wide balls
            self.wideBalls += n
            self.teamRuns += n
            if self.teamRuns < 0:
                self.teamRuns = 0
            if self.wideBalls < 0:
                self.wideBalls = 0
            self.wideLabel.configure(text = str(self.wideBalls))
            self.runsLabel.configure(text = str(self.teamRuns))
            return
        
        def addBalls(n): #add/subtract total balls
            self.totalBalls += n
            if self.totalBalls < 0:
                self.totalBalls = 0
            self.ballsLabel.configure(text = str(self.totalBalls))
            self.oversIndicator.configure(text = str(round((self.totalBalls/6),2)))
            return            
        
        self.TeamLabel = ctk.CTkLabel(self, text= self.teamName, 
                                      fg_color= 'grey', 
                                      font = ("Bahnschrift SemiBold",30), 
                                      width= 300, height = 50, 
                                      corner_radius= 10, 
                                      anchor = 'w')
        self.TeamLabel.grid(column = 0, row = 1, padx = 5, pady = 9, sticky = 'nw', columnspan = 2)

        self.batterLabel = ctk.CTkLabel(self, text= 'Batting team', 
                                      fg_color = 'transparent', 
                                      bg_color = 'transparent',
                                      font = ("Bahnschrift SemiBold",18),
                                      anchor = 'w',
                                      justify = 'left'
                                    )
        
        self.batterLabel.grid(column = 0, row = 0, sticky = 'w', padx = 3)
        """
        empty labels for formatting grid system
        """

        self.row0EmptyLabel1 = ctk.CTkLabel(self, text= '', fg_color = 'transparent', bg_color = 'transparent', width = 150)
        self.row0EmptyLabel1.grid(column = 2, row = 0)

        self.row0EmptyLabel2 = ctk.CTkLabel(self, text= '', fg_color = 'transparent', bg_color = 'transparent', width = 150)
        self.row0EmptyLabel2.grid(column = 3, row = 0)

        self.row0EmptyLabel3 = ctk.CTkLabel(self, text= '', fg_color = 'transparent', bg_color = 'transparent', width = 150)
        self.row0EmptyLabel3.grid(column = 4, row = 0)

        self.oversText = ctk.CTkLabel(self, text= 'Overs', 
                                            font = ("Bahnschrift SemiBold",20),
                                            fg_color = 'transparent', 
                                            bg_color = 'transparent', 
                                            width = 150)
        
        self.oversText.grid(column = 5, row = 0)


        self.row1EmptyLabel1 = ctk.CTkLabel(self, text= '', fg_color = 'transparent', bg_color = 'transparent', width = 150)
        self.row1EmptyLabel1.grid(column = 2, row = 1)

        self.row1EmptyLabel2 = ctk.CTkLabel(self, text= '', fg_color = 'transparent', bg_color = 'transparent', width = 150)
        self.row1EmptyLabel2.grid(column = 3, row = 1)

        self.row1EmptyLabel3 = ctk.CTkLabel(self, text= '', fg_color = 'transparent', bg_color = 'transparent', width = 150)
        self.row1EmptyLabel3.grid(column = 4, row = 1)

        self.oversIndicator = ctk.CTkLabel(self, text = str(round((self.totalBalls/6),1)), 
                                            font = ("Bahnschrift SemiBold",30),
                                            fg_color = 'grey',
                                            corner_radius= 5,
                                            bg_color = 'transparent', 
                                            width = 150,
                                            height = 50)
        self.oversIndicator.grid(column = 5, row = 1)

        self.runsLabel = ctk.CTkLabel(self, text = str(self.teamRuns),
                                      font = ("Bahnschrift SemiBold",30), 
                                      fg_color = 'grey', 
                                      width = 120,
                                      height = 60,
                                      corner_radius = 10
                                      )
        
        self.runsText = ctk.CTkLabel(self, text = "Runs",
                                     font = ("Bahnschrift SemiBold",20), 
                                     width = 120,
                                     height = 30
                                     )
        
        self.runsLabel.grid(column = 0, row = 3, padx = 5, pady = 3)
        self.runsText.grid(column = 0, row = 2)

        self.runsLabelSeperator = ctk.CTkLabel(self, text = '',
                                               height = 50
                                               )
        self.runsLabelSeperator.grid(column= 0, row = 4)

        self.runOptions = ctk.CTkOptionMenu(self, values = ['1','2','3','4','6'], #options menu to choose the number of runs to add/subtract
                                            width = 120,
                                            corner_radius= 5,
                                            font = ("Bahnschrift SemiBold",15),
                                            fg_color = 'grey'
                                            )
        self.runOptions.grid(column = 0, row = 5, padx = 3, pady = 5 )

        self.addRunButton = ctk.CTkButton(self, text = 'Add runs',
                                          fg_color = 'green',
                                          corner_radius = 5,
                                          bg_color = 'transparent',
                                          text_color= 'black',
                                          font = ("Bahnschrift SemiBold",18),
                                          width = 110,
                                          command = lambda: addRuns(int(self.runOptions.get()))
                                          )
        self.addRunButton.grid(column = 0, row = 6, padx = 3, pady = 5)

        #remove run button 
        self.removeRunsButton = ctk.CTkButton(self, text = "Remove runs", 
                                              fg_color = 'red', 
                                              bg_color = 'transparent',
                                              font = ("Bahnschrift SemiBold",18),
                                              text_color = 'black',
                                              width = 110,
                                              command = lambda: removeRuns(int(self.runOptions.get())),
                                              corner_radius=5
                                              )
        self.removeRunsButton.grid(column = 0, row = 7, pady = 3, padx = 5, sticky = 'n')

        self.wicketCounter = ctk.CTkLabel(self, text = f'{self.teamWickets}',
                                          font = ("Bahnschrift SemiBold",30), 
                                          fg_color = 'grey', 
                                          width = 120,
                                          height = 60,
                                          corner_radius = 10
                                          )
        
        self.wicketText = ctk.CTkLabel(self, text = 'Wickets',
                                       font = ("Bahnschrift SemiBold",20), 
                                       width = 100,
                                       height = 30,
                                       )

        self.wicketCounter.grid(column = 1, row = 3, padx = 5, pady = 3)
        self.wicketText.grid(column = 1, row = 2)

        self.addWicketButton = ctk.CTkButton(self, text = 'Add wicket',
                                             fg_color = 'green', 
                                             bg_color = 'transparent',
                                             text_color= 'black',
                                             font = ("Bahnschrift SemiBold",18),
                                             width = 120,
                                             corner_radius= 5,
                                             command = lambda: addWickets(1)
                                             )
        self.addWicketButton.grid(column = 1, row = 5)

        self.removeWicketButton = ctk.CTkButton(self, text = 'Remove wicket',
                                             fg_color = 'Red', 
                                             bg_color = 'transparent',
                                             text_color= 'black',
                                             font = ("Bahnschrift SemiBold",15),
                                             width = 120,
                                             corner_radius= 5,
                                             command = lambda: removeWickets(1),
                                             anchor = 'c'
                                             )
        self.removeWicketButton.grid(column = 1, row = 6)

        self.ballsLabel = ctk.CTkLabel(self, text = f'{self.totalBalls}',
                                       font = ("Bahnschrift SemiBold",30), 
                                        fg_color = 'grey', 
                                        width = 120,
                                        height = 70,
                                        corner_radius = 10
                                        )
        
        self.ballsText = ctk.CTkLabel(self, text = 'Balls',
                                       font = ("Bahnschrift SemiBold",30), 
                                       width = 100,
                                       height = 30,
                                       )
        
        self.ballsLabel.grid(column = 2, row = 3, padx = 5, pady = 3, columnspan = 2)
        self.ballsText.grid(column = 2, row = 2, columnspan = 2)
                                       
        self.widesFrame = ctk.CTkFrame(self)
        wideText = ctk.CTkLabel(self.widesFrame, text = 'Wide balls',
                                font = ("Bahnschrift SemiBold",18) 
                                )
        
        self.wideLabel = ctk.CTkLabel(self.widesFrame, text = str(self.wideBalls),
                                 font = ("Bahnschrift SemiBold",20),
                                 fg_color  = 'grey',
                                 corner_radius = 5,
                                 width = 100,
                                 height = 30
                                 )
        
        wideText.pack(padx = 3, pady = 3)
        self.wideLabel.pack(padx = 3, pady = 3)
        self.widesFrame.grid(column = 2, row = 4, columnspan = 2, padx = 3, pady = 3)

        self.noBallFrame = ctk.CTkFrame(self)
        noBallText = ctk.CTkLabel(self.noBallFrame, text = 'No balls',
                                font = ("Bahnschrift SemiBold",18) 
                                )
        self.noBallLabel = ctk.CTkLabel(self.noBallFrame, text = str(self.teamNoBalls),
                                 font = ("Bahnschrift SemiBold",20),
                                 fg_color  = 'grey',
                                 corner_radius = 5,
                                 width = 100,
                                 height = 30
                                 )
        noBallText.pack(padx = 3, pady = 3)
        self.noBallLabel.pack(padx = 3, pady = 3)
        self.noBallFrame.grid(column = 2, row = 5, columnspan = 2, rowspan = 2, padx = 3, pady = 3)

        self.buttonsFrame = ctk.CTkFrame(self)
        addBallsButton = ctk.CTkButton(self.buttonsFrame, text = '+ Balls',
                                        fg_color = 'green', 
                                        bg_color = 'transparent',
                                        text_color= 'black',
                                        font = ("Bahnschrift SemiBold",18),
                                        width = 120,
                                        corner_radius= 5,
                                        command = lambda: addBalls(1)
                                        )
        addBallsButton.grid(column = 0, row = 0, padx = 3, pady = 5)

        addWideBallButton = ctk.CTkButton(self.buttonsFrame, text = '+ Wide Ball',
                                        fg_color = 'green', 
                                        bg_color = 'transparent',
                                        text_color= 'black',
                                        font = ("Bahnschrift SemiBold",18),
                                        width = 120,
                                        corner_radius= 5,
                                        command = lambda: addWideBall(1)
                                        )
        addWideBallButton.grid(column = 0, row = 1, padx = 3, pady = 5)

        addNoBallButton = ctk.CTkButton(self.buttonsFrame, text = '+ No Ball',
                                        fg_color = 'green', 
                                        bg_color = 'transparent',
                                        text_color= 'black',
                                        font = ("Bahnschrift SemiBold",18),
                                        width = 120,
                                        corner_radius= 5,
                                        command = lambda: addNoBall(1)
                                        )
        addNoBallButton.grid(column = 0, row = 2, padx = 3, pady = 5)
        
        removeBallsButton = ctk.CTkButton(self.buttonsFrame, text = '- Ball',
                                        fg_color = 'red', 
                                        bg_color = 'transparent',
                                        text_color= 'black',
                                        font = ("Bahnschrift SemiBold",18),
                                        width = 120,
                                        corner_radius= 5,
                                        command = lambda: addBalls(-1)
                                        )
        removeBallsButton.grid(column = 1, row = 0, padx = 3, pady = 5)

        removeWideBallButton = ctk.CTkButton(self.buttonsFrame, text = '- Wide Ball',
                                        fg_color = 'red', 
                                        bg_color = 'transparent',
                                        text_color= 'black',
                                        font = ("Bahnschrift SemiBold",18),
                                        width = 120,
                                        corner_radius= 5,
                                        command = lambda: addWideBall(-1)
                                        )
        removeWideBallButton.grid(column = 1, row = 1, padx = 3, pady = 5)

        removeNoBallButton = ctk.CTkButton(self.buttonsFrame, text = '- No Ball',
                                        fg_color = 'red', 
                                        bg_color = 'transparent',
                                        text_color= 'black',
                                        font = ("Bahnschrift SemiBold",18),
                                        width = 120,
                                        corner_radius= 5,
                                        command = lambda: addNoBall(-1)
                                        )
        removeNoBallButton.grid(column = 1, row = 2, padx = 3, pady = 5)
        
        self.buttonsFrame.grid(column = 2, row = 7, columnspan = 2, padx = 3, pady = 5)

        self.removeBatterFrame = ctk.CTkFrame(self)
        batterLabel = ctk.CTkLabel(self.removeBatterFrame, text = 'Batter out',
                                   font = ("Bahnschrift SemiBold",15)
                                   )
        bowlerLabel = ctk.CTkLabel(self.removeBatterFrame, text = 'Bowler',
                                   font = ("Bahnschrift SemiBold",15)
                                   )
        
        batterLabel.grid(row = 0, column = 0, sticky = 'w', padx = 5)
        bowlerLabel.grid(row = 0, column = 1, sticky = 'w', padx = 5)

        self.batterSelect = ctk.CTkOptionMenu(self.removeBatterFrame, values=self.players,
                                         width = 120,
                                         corner_radius= 5,
                                         font = ("Bahnschrift SemiBold",15),
                                         fg_color = 'grey'
                                         )
        self.bowlerSelect = ctk.CTkOptionMenu(self.removeBatterFrame, values = self.opposing,
                                         width = 120,
                                         corner_radius= 5,
                                         font = ("Bahnschrift SemiBold",15),
                                         fg_color = 'grey'
                                         )
        self.batterSelect.set('Select batter')
        self.bowlerSelect.set('Select bowler')
        self.batterSelect.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.bowlerSelect.grid(row = 1, column = 1, padx = 5, pady = 5)

        batterRemoveButton = ctk.CTkButton(self.removeBatterFrame, text = 'Batter out',
                                           fg_color = 'green',
                                           font = ("Bahnschrift SemiBold",15),
                                           corner_radius = 5,
                                           width = 120,
                                           height = 20,
                                           command = removeBatter
                                           )
        batterRemoveButton.grid(row = 2, column = 0, padx = 3, pady = 3)
        self.remainingBattersLabel = ctk.CTkLabel(self.removeBatterFrame, text = f'Remaining batters:\n{len(self.players)}')
        self.remainingBattersLabel.grid(row = 2, column = 1)
        self.removeBatterFrame.grid(column = 4, row = 2, columnspan = 2, rowspan = 2)

        self.outsFrame = ctk.CTkScrollableFrame(self, height = 200, width = 240)
        for row,out in enumerate(self.battersOut):
            nameFrame = ctk.CTkFrame(self.outsFrame, height = 20, width = 210)
            batterName = ctk.CTkLabel(nameFrame, text = out[0], width = 70)
            middle = ctk.CTkLabel(nameFrame, text = 'out by', width = 70)
            bowlerName = ctk.CTkLabel(nameFrame,text = out[1], width = 70)
            batterName.grid(row = 0, column = 0, padx = 3)
            middle.grid(row = 0, column = 1, padx = 3)
            bowlerName.grid(row = 0, column = 2, padx = 3)
            nameFrame.grid(row = row, column = 0, columnspan = 2, pady = 5)

        self.outsFrame.grid(column = 4, row = 4, columnspan = 2, rowspan = 2, pady = 5)
        
        endButton = ctk.CTkButton(self, text = 'End Game',
                                  font = ("Bahnschrift SemiBold",20),
                                  height = 50, width = 150,
                                  corner_radius=5,
                                  fg_color='red',
                                  text_color= 'black',
                                  command = endGame
                                  )
        endButton.grid(column = 4, row = 7)

def switchToNewScreen(oldFrame,newFrame): #general purpose switch screen function
    oldFrame.forget()
    newFrame.pack()
    return

def startGame(oldFrame, newFrame, t1Name, t2Name, t1Entries, t2Entries): #function to initialise start of the game and scoreboards tabview

    t1_name = t1Name.get()
    t2_name = t2Name.get()
    t1Players = []
    t2Players = []

    for textbox in t1Entries:
        name = textbox.get()
        t1Players.append(name)

    for textbox in t2Entries:
        name = textbox.get()
        t2Players.append(name)

    if '' in t2Players or '' in t1Players or t1_name == '' or t2_name == '':
        messagebox.showerror('Input error',"Please enter all player and team names!")
        return
    
    global t1ScoreFrame 
    global t2ScoreFrame
    global gameTab

    gameTab = None
    gameTab = ctk.CTkTabview(master = root, width = 900, height = 700, border_color = "black", fg_color= 'black' )

    msg_box = messagebox.askokcancel(title='Warning!', message='Please do not close the program at any time during the game, as data will be lost!\nPress OK to begin game.')
    if msg_box == False:
        return

    #adding game screens to the tabview
    gameTab.add(t1_name)
    gameTab.add(t2_name)

    t1ScoreFrame = ScoringFrame(gameTab.tab(t1_name), t1_name, t1Entries, t2Entries,1)
    t2ScoreFrame = ScoringFrame(gameTab.tab(t2_name), t2_name, t2Entries, t1Entries,2)

    oldFrame.forget()   
    gameTab.pack()
    t2ScoreFrame.pack()
    t1ScoreFrame.pack()
    return

def endGame(): #special function to consolidate all data and display end game screen

    msg_box = messagebox.askokcancel(title='End game?',message = 'Please ensure that all game data is entered, this action cannot be reversed!')
    if msg_box == False: #stops function if user presses cancel
        return
    else:
        pass

    global t1ScoreFrame
    global t2ScoreFrame
    global gameTab
    global endFrame

    if (t1ScoreFrame.teamRuns == 0 and t2ScoreFrame.teamRuns == 0) or (t1ScoreFrame.totalBalls==0 or t2ScoreFrame.totalBalls==0):
        messagebox.showerror(title='Error!',message='At least one team must have more than 0 runs and neither teams can have 0 balls! Please check your input!')
        return
    endFrame = gameEndScreen(root,t1ScoreFrame,t2ScoreFrame) #loading endGame screen and removing previous screen
    gameTab.forget()
    endFrame.pack()
    
def closeProgram(): #exits program
    root.quit()
    return

def restart(): #restarts program from start

    msg_box = messagebox.askokcancel(title='Restart game?', message='Restart game? All data will be lost, this action cannot be reversed.')
    if msg_box == False:
        return
    
    global menuScreen
    global endFrame
    global team1Entries
    global team2Entries
    global teamOneName
    global teamTwoName

    t1Name = teamOneName.get()
    t2Name = teamTwoName.get()

    teamOneName.delete(0, len(t1Name))
    teamTwoName.delete(0,len(t2Name))

    for field in team1Entries:
        word  = field.get()
        field.delete(0,len(word))
        

    for field in team2Entries:
        word  = field.get()
        field.delete(0,len(word))
        
    endFrame.forget()
    menuScreen.pack()
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
                           command = lambda: startGame(entryScreen,gameTab,teamOneName,teamTwoName,team1Entries,team2Entries))

nextButton.grid(row=1,column=0,columnspan = 2)

class gameEndScreen(ctk.CTkFrame): #screen containing the final display of the scoring
    def __init__(self, master, team1, team2):
        super().__init__(master, width=900, height = 1000)

        self.team1Data = team1
        self.team2Data = team2

        self.scoreText = ctk.CTkLabel(self, text = 'Final scores',
                                      font = ("Bahnschrift SemiBold",30),
                                      width = 900,
                                      height = 100, 
                                      corner_radius=5,
                                      fg_color='transparent')
        
        self.scoreText.grid(row = 0, column = 0, columnspan = 4, pady = 5)

        class teamDataSubFrame(ctk.CTkFrame): #subframe within screen to display outed players for both teams
            def __init__(self, master, teamData):
                super().__init__(master, width=400, height = 800)

                

                self.teamData = teamData

                teamOneLabel = ctk.CTkLabel(self, width = 150, height = 30, 
                                    text = self.teamData.teamName,
                                    font = ("Bahnschrift SemiBold",20),
                                    fg_color = 'grey',
                                    corner_radius = 5
                                    )
                teamOneLabel.grid(column = 0, row = 0, sticky = 'w')

                self.outsFrame = ctk.CTkScrollableFrame(self, height = 250, width = 400,
                                                         border_color='grey',
                                                         border_width = 5)
                for row,out in enumerate(self.teamData.battersOut):
                    nameFrame = ctk.CTkFrame(self.outsFrame, height = 30, width = 390,
                                             border_color = 'black',
                                             border_width = 2)
                    batterName = ctk.CTkLabel(nameFrame, text = out[0], width = 130, height = 15, pady = 0)
                    middle = ctk.CTkLabel(nameFrame, text = 'out by', width = 130, height = 15, pady = 0)
                    bowlerName = ctk.CTkLabel(nameFrame,text = out[1], width = 130, height = 15, pady = 0)
                    batterName.grid(row = 0, column = 0, padx = 3)
                    middle.grid(row = 0, column = 1, padx = 3)
                    bowlerName.grid(row = 0, column = 2, padx = 3)
                    nameFrame.grid(row = row, column = 0, columnspan = 2, pady = 5)

                self.outsFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 2, pady = 5)

                self.totalsLabel = ctk.CTkLabel(self, text = 'Total:',
                                                font = ("Bahnschrift SemiBold",20),
                                                height = 25, width = 100
                                                )
                self.totalsLabel.grid(column = 0, row =  3, padx = 5, pady = 5, sticky = 'w')

                self.totalsIndicator = ctk.CTkLabel(self, text = f'{self.teamData.teamRuns}/{self.teamData.teamWickets}',
                                                    font = ("Bahnschrift SemiBold",25),
                                                    height = 25, width = 150)
                self.totalsIndicator.grid(column = 1, row = 3, padx = 5, pady = 5, sticky = 'e', rowspan = 2)

                self.legend = ctk.CTkLabel(self, text = 'Runs/Wickets',
                                           font = ("Bahnschrift",15),
                                           height = 18, width = 100
                                           )
                self.legend.grid(column = 0, row = 4, padx = 5, pady = 0, sticky = 'w')

                self.wideBallsLabel = ctk.CTkLabel(self, text = 'Wide balls:',
                                                   font = ("Bahnschrift SemiBold",20),
                                                   height = 25, width = 100
                                                   )
                self.wideBallsLabel.grid(column = 0, row = 5, padx = 5, pady = 5, sticky = 'w')

                self.wideBallsIndicator = ctk.CTkLabel(self, text = self.teamData.wideBalls,
                                                       font = ("Bahnschrift SemiBold",25),
                                                       height = 25, width = 150
                                                       )
                self.wideBallsIndicator.grid(column = 1, row = 5, padx = 5, pady = 5, sticky = 'e')

                self.noBallsLabel = ctk.CTkLabel(self, text = 'No Balls:',
                                                font = ("Bahnschrift SemiBold",20),
                                                height = 25, width = 100
                                                )
                self.noBallsLabel.grid(column = 0, row = 6, padx = 5, pady = 5, sticky = 'w')
                self.noBallsIndicator = ctk.CTkLabel(self, text = self.teamData.teamNoBalls,
                                                     font = ("Bahnschrift SemiBold",25),
                                                     height = 25, width = 150
                                                     )
                self.noBallsIndicator.grid(column = 1, row = 6, padx = 5, pady = 5, sticky = 'e')

                self.runRateIndicator = ctk.CTkLabel(self, text = str(round((teamData.teamRuns/teamData.totalBalls),2)),
                                                     font = ("Bahnschrift SemiBold",25),
                                                     height = 25, width = 150
                                                     )
                self.runRateIndicator.grid(column = 1, row = 7, padx = 5, pady = 5, sticky = 'e')
                self.runRateLabel = ctk.CTkLabel(self, text = 'Run rate:',
                                                font = ("Bahnschrift SemiBold",20),
                                                height = 25, width = 100
                                                )
                self.runRateLabel.grid(column = 0, row = 7, padx = 5, pady = 5, sticky = 'w')

        self.teamOneFrame = teamDataSubFrame(self, self.team1Data)
        self.teamTwoFrame = teamDataSubFrame(self, self.team2Data)
        self.teamOneFrame.grid(row= 1, column = 0, columnspan = 2, pady = 5)
        self.teamTwoFrame.grid(row= 1, column = 2, columnspan = 2, pady = 5)

        if self.team1Data.teamRuns > self.team2Data.teamRuns: #case where team 1 wins
            diff = self.team1Data.teamRuns - self.team2Data.teamRuns
            self.winnersLabel = ctk.CTkLabel(self,text = f'{self.team1Data.teamName} wins by {diff} runs!',
                                             font = ("Bahnschrift SemiBold",35),
                                             height = 50, width = 500
                                             )

        elif self.team2Data.teamRuns > self.team1Data.teamRuns: #case where team 2 wins
            diff = self.team2Data.teamRuns - self.team1Data.teamRuns
            self.winnersLabel = ctk.CTkLabel(self,text = f'{self.team2Data.teamName} wins by {diff} runs!',
                                             font = ("Bahnschrift SemiBold",35),
                                             height = 50, width = 500
                                             )
        elif self.team2Data.teamRuns == self.team1Data.teamRuns:
            self.winnersLabel = ctk.CTkLabel(self,text = f'Tied game!',
                                             font = ("Bahnschrift SemiBold",35),
                                             height = 50, width = 500
                                             )
            
        self.winnersLabel.grid(column = 0, row = 2, columnspan = 4, padx = 5, pady = 5, rowspan = 2)

        self.restartButton = ctk.CTkButton(self,text = 'Restart!', command=restart,
                                           font = ("Bahnschrift SemiBold",25),
                                           fg_color = 'red',
                                           width=150, height = 30)
        self.restartButton.grid(column = 0, row = 4, columnspan = 4) 



root.mainloop()
