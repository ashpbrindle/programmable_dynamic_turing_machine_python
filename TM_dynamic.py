from State import State, StateContext
from time import sleep
from collections import defaultdict
from Tkinter import *
import tkMessageBox
import sys

DIRECTION = 0
NEW_SYMBOL = 1
NEXT_STATE = 2


class TuringMachineGUI():
    '''Handles all of the GUI aspects of the program, such as updating the interface 
    and resetting the machine'''

    def __init__(self, window):

        # defines all of the fonts used in the GUI
        self.tape_font = ("times", 20)
        self.position_font = ("times", 15, "italic")
        self.instruction_font = ("times", 15)
        self.addInstruction_font = ("times", 10)
        self.currentInstruction_font = ("times", 10)
        self.arrow_font = ("calibri", 10, "bold")
        self.run_font = ("bold")
        self.submitTape_font = ("calibri", 10, "bold")
        self.title_font = ("times", 15)
        self.title2_font = ("times", 11)

        # creates an instance of the turing machine to allow for adding the tape, state, position, etc. To the machine
        self.TM = TuringMachine()
        
        # attributes to handle the speed the machine will run (sleep)
        self.speedLabel = 5
        self.speeds = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        self.speedindex = 5

        # the GUI tape positions to handle where each value on the tape will show on the GUI
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
        # draws the GUI aspects on the window
        self.drawWindow()

    def drawWindow(self):

        # shows the tape positions at the top of the window
        self.lblPositions = Label(
            root, 
            text= "-3             -2             -1             0              1              2              3              4",
            fg = "gray26",
            font = self.position_font)
        self.lblPositions.pack()
        self.lblPositions.place(x = 80, y = 5)

        # the following represents each square of the tape
        self.lblTape0 = Label(
            root, 
            text= "#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape0.pack()
        self.lblTape0.place(x = 62, y = 30)

        self.lblTape1 = Label(
            root, 
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape1.pack()
        self.lblTape1.place(x = 142, y = 30)

        self.lblTape2 = Label(
            root, 
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape2.pack()
        self.lblTape2.place(x = 222, y = 30)

        self.lblTape3 = Label(
            root, 
            text="#",
            bg = "DarkOliveGreen3",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape3.pack()
        self.lblTape3.place(x = 302, y = 30)

        self.lblTape4 = Label(
            root, 
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape4.pack()
        self.lblTape4.place(x = 382, y = 30)

        self.lblTape5 = Label(
            root, 
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape5.pack()
        self.lblTape5.place(x = 462, y = 30)

        self.lblTape6 = Label(
            root, 
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape6.pack()
        self.lblTape6.place(x = 542, y = 30)

        self.lblTape7 = Label(
            root, 
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape7.pack()
        self.lblTape7.place(x = 622, y = 30)

        # allows for moving right
        self.btnRight = Button(
            root,
            text = ">",
            bg = "DarkGoldenrod3",
            fg = "black",
            font = self.arrow_font,
            height = 4,
            width = 2,
            borderwidth = 1,
            relief = "solid",
            command = self.scrollRight
            )
        self.btnRight.pack()
        self.btnRight.place(x = 700, y = 30)

        # allows for moving left
        self.btnLeft = Button(
            root,
            text = "<",
            bg = "DarkGoldenrod3",
            fg = "black",
            font = self.arrow_font,
            height = 4,
            width = 2,
            borderwidth = 1,
            relief = "solid",
            command = self.scrollLeft
            )
        self.btnLeft.pack()
        self.btnLeft.place(x = 30, y = 30)

        # title for the add instruction section
        self.lblInstructionsTitle = Label(
            root,
            text = "Add Instruction:",
            font = self.title_font)
        self.lblInstructionsTitle.pack()
        self.lblInstructionsTitle.place(x = 468, y = 115)

        # border for adding instructions
        self.lblAddInstructionsBorder = Label(
            root, 
            text= "Scanned State: \n"
                                    "Scanned Symbol: \n"
                                    "Direction: \n"
                                    "New Symbol: \n"
                                    "New State:",
            bg = "white",
            fg = "black",
            font = self.instruction_font,
            height = 5,
            width = 23,
            borderwidth = 2,
            relief = "solid",
            justify = LEFT,
            anchor = "w")
        self.lblAddInstructionsBorder.pack()
        self.lblAddInstructionsBorder.place(x = 468, y = 140)

        # the following allow the user to add instructions
        self.txtScannedState = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtScannedState.pack()
        self.txtScannedState.place(x = 675, y = 146)

        self.txtScannedSymbol = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtScannedSymbol.pack()
        self.txtScannedSymbol.place(x = 675, y = 168)

        self.txtDirection = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtDirection.pack()
        self.txtDirection.place(x = 675, y = 188)

        self.txtNewSymbol = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtNewSymbol.pack()
        self.txtNewSymbol.place(x = 675, y = 208)

        self.txtNewState = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtNewState.pack()
        self.txtNewState.place(x = 675, y = 230)

        # saves the instructions to the machine
        self.btnSaveInstruction = Button(
            root,
            text = "Save Instruction",
            bg = "green4",
            fg = "white",
            font = self.arrow_font,
            height = 1,
            width = 36,
            borderwidth = 1,
            relief = "solid",
            command = self.setInstruction)
        self.btnSaveInstruction.pack()
        self.btnSaveInstruction.place(x = 468, y = 265)

        # title for the running instructions
        self.lblInstructionsTitle = Label(
            root,
            text = "Running Instruction:",
            font = self.title_font)
        self.lblInstructionsTitle.pack()
        self.lblInstructionsTitle.place(x = 468, y = 293)

        # border for the running instructions
        self.lblInstructionsBorder = Label(
            root, 
            text= "Scanned State: \n"
                                    "Scanned Symbol: \n"
                                    "Direction: \n"
                                    "New Symbol: \n"
                                    "New State:",
            bg = "white",
            fg = "black",
            font = self.instruction_font,
            height = 5,
            width = 23,
            borderwidth = 2,
            relief = "solid",
            justify = LEFT,
            anchor = "w")
        self.lblInstructionsBorder.pack()
        self.lblInstructionsBorder.place(x = 468, y = 318)

        # the following shows the currently running instructions
        self.lblScannedState = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblScannedState.pack()
        self.lblScannedState.place(x = 665, y = 324)

        self.lblScannedSymbol = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblScannedSymbol.pack()
        self.lblScannedSymbol.place(x = 665, y = 346)

        self.lblDirection = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblDirection.pack()
        self.lblDirection.place(x = 665, y = 366)

        self.lblNewSymbol = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblNewSymbol.pack()
        self.lblNewSymbol.place(x = 665, y = 386)

        self.lblNewState = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblNewState.pack()
        self.lblNewState.place(x = 665, y = 408)

        # title for showing the listbox of instructions
        self.lblAllInstructionsTitle = Label(
            root,
            text = "All Instructions:",
            font = self.title_font)
        self.lblAllInstructionsTitle.pack()
        self.lblAllInstructionsTitle.place(x = 262, y = 115)

        # the following handles the list box for isntructions
        self.instructionsFrame = Frame(
            root,
            borderwidth = 2,
            relief = "solid")
        self.instructionsFrame.pack()
        self.instructionsFrame.place(x = 262, y = 140)
        # with a scroll bar
        self.scrlInstructions = Scrollbar(self.instructionsFrame)
        self.scrlInstructions.pack(side = "right", fill = "y")

        self.lstShowInstructions = Listbox(
            self.instructionsFrame,
            bg = "white",
            yscrollcommand = self.scrlInstructions.set,
            fg = "black",
            height = 15,
            width = 27)
        self.lstShowInstructions.pack(side = "left", fill = "y")
        self.scrlInstructions.config(command = self.lstShowInstructions.yview)

        # the following handles adding a tape to the machine
        self.lblInsertTapeTitle = Label(
            root,
            text = "Insert Tape (CSV):",
            font = self.title_font)
        self.lblInsertTapeTitle.pack()
        self.lblInsertTapeTitle.place(x = 20, y = 115)

        self.txtTape = Text(
            root,
            bg = "white",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.txtTape.pack()
        self.txtTape.place(x = 20, y = 140)

        self.btnTape = Button(
            root,
            text = "Submit Tape",
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid",
            command = self.submitTape)
        self.btnTape.pack()
        self.btnTape.place(x = 19, y = 165)

        # the following handles adding a starting state to the machine
        self.lblStartingTitle = Label(
            root,
            text = "Insert Starting State:",
            font = self.title_font)
        self.lblStartingTitle.pack()
        self.lblStartingTitle.place(x = 20, y = 190)

        self.txtStartState = Text(
            root,
            bg = "white",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.txtStartState.pack()
        self.txtStartState.place(x = 20, y = 215)

        self.btnStartState = Button(
            root,
            text = "Submit State",
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid",
            command = self.setStartingState)
        self.btnStartState.pack()
        self.btnStartState.place(x = 19, y = 240)

        # runs the machine
        self.btnRun = Button(
            root,
            text = "Run Machine",
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid",
            command = self.runMachine)
        self.btnRun.pack()
        self.btnRun.place(x = 19, y = 275)

        # handles changing the speed of the machine
        self.lblCurrentSpeed = Label(
            root,
            text = "Speed: 5", 
            font = self.title_font)
        self.lblCurrentSpeed.pack()
        self.lblCurrentSpeed.place(x = 20, y = 302)

        self.btnIncreaseSpeed = Button(
            root,
            text = "-",
            bg = "red3",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 5,
            borderwidth = 1,
            relief = "solid",
            command = self.increaseSpeed)
        self.btnIncreaseSpeed.pack()
        self.btnIncreaseSpeed.place(x = 150, y = 305)

        self.btnDecreaseSpeed = Button(
            root,
            text = "+",
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 5,
            borderwidth = 1,
            relief = "solid",
            command = self.decreaseSpeed)
        self.btnDecreaseSpeed.pack()
        self.btnDecreaseSpeed.place(x = 200, y = 305)

        # shows help for the machine
        self.btnHelp = Button(
            root,
            text = "Help",
            bg = "DarkGoldenRod3",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid",
            command = self.helpPopup)
        self.btnHelp.pack()
        self.btnHelp.place(x = 19, y = 333)

        # handles displaying the starting state and position of the machine
        self.lblStartingState = Label(
            root,
            text = "Starting State: N/A",
            font = self.title_font)
        self.lblStartingState.pack()
        self.lblStartingState.place(x = 262, y = 390)

        self.lblTapePosition = Label(
            root,
            text = "Tape Position: 0",
            font = self.title_font)
        self.lblTapePosition.pack()
        self.lblTapePosition.place(x = 262, y = 415)

        # handles changing the tape position
        self.lblTapePositionTitle = Label(
            root,
            text = "Tape Position (0 >):",
            font = self.title_font)
        self.lblTapePositionTitle.pack()
        self.lblTapePositionTitle.place(x = 20, y = 360)

        self.txtTapePosition = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.submitTape_font,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.txtTapePosition.pack()
        self.txtTapePosition.place(x = 20, y = 385)

        self.btnTapePosition = Button(
            root,
            text = "Submit Position",
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid",
            command = self.setTapePosition)
        self.btnTapePosition.pack()
        self.btnTapePosition.place(x = 19, y = 411)

        # loads data from file
        self.btnLoadDataFromFile = Button(
            root,
            text = "Reset and Load Data From File",
            bg = "DarkGoldenRod3",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid",
            command = self.loadFromFile)
        self.btnLoadDataFromFile.pack()
        self.btnLoadDataFromFile.place(x = 19, y = 446)

        # deletes all instructions in the machine
        self.btnDeleteAllInstructions = Button(
            root,
            text = "Clear All Instructions",
            bg = "red3",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 26,
            borderwidth = 1,
            relief = "solid",
            command = self.clearInstructions)
        self.btnDeleteAllInstructions.pack()
        self.btnDeleteAllInstructions.place(x = 260, y = 446)

        self.btnExit = Button(
            root,
            text = "Exit Application",
            bg = "red3",
            fg = "white",
            font = self.submitTape_font,
            command = root.destroy,
            height = 1,
            width = 36,
            borderwidth = 1,
            relief = "solid")
        self.btnExit.pack()
        self.btnExit.place(x = 468, y = 446)

    # used to scroll left on the GUI tape
    def scrollLeft(self):
        if len(self.TM.tape) > 0:

            # moves the GUI tape positions to the left, checks for original tape as this will determine if the machine is scrolling while running or before
            if str(self.TM.tape) == str(self.TM.original_tape):
                for index in range(len(self.GUI_tape_positions)):
                    self.GUI_tape_positions[index] -= 1

            if self.GUI_tape_positions[3] == -1:
                for index in range(len(self.GUI_tape_positions)):
                    self.GUI_tape_positions[index] += 1

            # this will handle what values are presented on the GUI tape
            if self.GUI_tape_positions[3] > -1:
                if self.GUI_tape_positions[0] > -1:
                    self.lblTape0.config(text = str(self.TM.tape[self.GUI_tape_positions[0]]))
                else:
                    self.lblTape0.config(text = "#")
                if self.GUI_tape_positions[1] > -1:
                    self.lblTape1.config(text = str(self.TM.tape[self.GUI_tape_positions[1]]))
                else:
                    self.lblTape1.config(text = "#")
                if self.GUI_tape_positions[2] > -1:
                    self.lblTape2.config(text = str(self.TM.tape[self.GUI_tape_positions[2]]))
                else:
                    self.lblTape2.config(text = "#")
                if self.GUI_tape_positions[3] < len(self.TM.tape):
                    self.lblTape3.config(text = str(self.TM.tape[self.GUI_tape_positions[3]]))
                else:
                    self.lblTape3.config(text = "#")
                if self.GUI_tape_positions[4] < len(self.TM.tape):
                    self.lblTape4.config(text = str(self.TM.tape[self.GUI_tape_positions[4]]))
                else:
                    self.lblTape4.config(text = "#")
                if self.GUI_tape_positions[5] < len(self.TM.tape):
                    self.lblTape5.config(text = str(self.TM.tape[self.GUI_tape_positions[5]]))
                else:
                    self.lblTape5.config(text = "#")
                if self.GUI_tape_positions[6] < len(self.TM.tape):
                    self.lblTape6.config(text = str(self.TM.tape[self.GUI_tape_positions[6]]))
                else:
                    self.lblTape6.config(text = "#")
                if self.GUI_tape_positions[7] < len(self.TM.tape):
                    self.lblTape7.config(text = str(self.TM.tape[self.GUI_tape_positions[7]]))
                else:
                    self.lblTape7.config(text = "#")

    def scrollRight(self):
        if len(self.TM.tape) > 0:

            # moves the GUI tape positions to the right
            for index in range(len(self.GUI_tape_positions)):
                self.GUI_tape_positions[index] += 1

            # this will handle what values are presented on the GUI tape
            if self.GUI_tape_positions[0] < len(self.TM.tape) and self.GUI_tape_positions[0] >= 0:
                self.lblTape0.config(text = str(self.TM.tape[self.GUI_tape_positions[0]]))
            else:
                self.lblTape0.config(text = "#")
            if self.GUI_tape_positions[1] < len(self.TM.tape) and self.GUI_tape_positions[1] >= 0:
                self.lblTape1.config(text = str(self.TM.tape[self.GUI_tape_positions[1]]))
            else:
                self.lblTape1.config(text = "#")
            if self.GUI_tape_positions[2] < len(self.TM.tape) and self.GUI_tape_positions[2] >= 0:
                self.lblTape2.config(text = str(self.TM.tape[self.GUI_tape_positions[2]]))
            else:
                self.lblTape2.config(text = "#")
            if self.GUI_tape_positions[3] < len(self.TM.tape):
                self.lblTape3.config(text = str(self.TM.tape[self.GUI_tape_positions[3]]))
            else:
                self.lblTape3.config(text = "#")
            if self.GUI_tape_positions[4] < len(self.TM.tape):
                self.lblTape4.config(text = str(self.TM.tape[self.GUI_tape_positions[4]]))
            else:
                self.lblTape4.config(text = "#")
            if self.GUI_tape_positions[5] < len(self.TM.tape):
                self.lblTape5.config(text = str(self.TM.tape[self.GUI_tape_positions[5]]))
            else:
                self.lblTape5.config(text = "#")
            if self.GUI_tape_positions[6] < len(self.TM.tape):
                self.lblTape6.config(text = str(self.TM.tape[self.GUI_tape_positions[6]]))
            else:
                self.lblTape6.config(text = "#")
            if self.GUI_tape_positions[7] < len(self.TM.tape):
                self.lblTape7.config(text = str(self.TM.tape[self.GUI_tape_positions[7]]))
            else:
                self.lblTape7.config(text = "#")

            # this moves the tape back if the tape is too short for the GUI
            if self.GUI_tape_positions[3] > len(self.TM.tape):
                for index in range(len(self.GUI_tape_positions)):
                    self.GUI_tape_positions[index] -= 1
    
    # method to handle increasing the speed of the machine
    def increaseSpeed(self):
        # handles if the speed goes too high
        if self.speedindex < 10:
            # changes index to be used in speeds list
            self.speedindex += 1
            self.speedLabel -= 1
            self.lblCurrentSpeed.config(text = "Speed: " + str(self.speedLabel))
            # sets the speed using the speeds list defined when initialised, this list holds all the different values the sleep can use in the TuringState
            self.TM.time = self.speeds[self.speedindex]
        else:
            print "Too Slow"
            
        print "Interval: ", self.TM.time

    def decreaseSpeed(self):
        # handles if the speed goes too low
        if self.speedindex > 0:
            # changes index to be used in speeds list
            self.speedindex -= 1
            self.speedLabel += 1
            self.lblCurrentSpeed.config(text = "Speed: " + str(self.speedLabel))
            # sets the speed form the speeds list
            self.TM.time = self.speeds[self.speedindex]
        else:
            print "Too Fast"
        
        print "Interval: ", self.TM.time

    def setInstruction(self):
        # gets all of the instructions from the textboxes
        state = self.txtScannedState.get()
        self.txtScannedState.delete(0,END)
        symbol = self.txtScannedSymbol.get()
        self.txtScannedSymbol.delete(0,END)
        direction = self.txtDirection.get()
        self.txtDirection.delete(0,END)
        new_symbol = self.txtNewSymbol.get()
        self.txtNewSymbol.delete(0,END)
        new_state = self.txtNewState.get()
        self.txtNewState.delete(0,END)
        root.update()

        # and adds them to the temp_instructions using setInstructions
        self.TM.setInstruction(state, symbol, direction, new_symbol, new_state)

    def submitTape(self):
        # gets the tape from the textbox and if the textbox is empty the tape is filled with blank symbols
        if self.txtTape.get("1.0", END) == "\n":
            self.txtTape.insert(END, "#")

        # fills the tape until it reaches a length of 8 (16 is used due to the commas in the string)
        while len(str(self.txtTape.get("1.0", END))) < 16:
            self.txtTape.insert(END, ",#")

        # gets the tape
        input_tape = str(self.txtTape.get("1.0", END))
        # removes the new line
        input_tape = input_tape[:-1]
        # using CSV, seperate the values on the tape
        self.TM.tape = input_tape.split(",")
        # sets the original tape used for navigation when the machine is not running
        self.TM.original_tape = self.TM.tape
        ## fills the tape with the new tape values
        self.fillTape()
        # emptys the testbox
        self.txtTape.delete('1.0', END)
        print "Current Tape: ", self.TM.tape  
        # resets the tape position
        self.TM.tape_position = 0 

    def fillTape(self):
        # initially resets the GUI tape
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
        self.lblTape0.config(text = "#")
        self.lblTape1.config(text = "#")
        self.lblTape2.config(text = "#")
        self.lblTape3.config(text = "#")
        self.lblTape4.config(text = "#")
        self.lblTape5.config(text = "#")
        self.lblTape6.config(text = "#")
        self.lblTape7.config(text = "#")

        # sets the values on the tape depending on the the length
        if len(self.TM.tape) >= 5:
            self.lblTape3.config(text = str(self.TM.tape[0]))
            self.lblTape4.config(text = str(self.TM.tape[1]))
            self.lblTape5.config(text = str(self.TM.tape[2]))
            self.lblTape6.config(text = str(self.TM.tape[3]))
            self.lblTape7.config(text = str(self.TM.tape[4]))
        elif len(self.TM.tape) >= 4:
            self.lblTape3.config(text = str(self.TM.tape[0]))
            self.lblTape4.config(text = str(self.TM.tape[1]))
            self.lblTape5.config(text = str(self.TM.tape[2]))
            self.lblTape6.config(text = str(self.TM.tape[3]))
        elif len(self.TM.tape) >= 3:
            self.lblTape3.config(text = str(self.TM.tape[0]))
            self.lblTape4.config(text = str(self.TM.tape[1]))
            self.lblTape5.config(text = str(self.TM.tape[2]))
        elif len(self.TM.tape) >= 2:
            self.lblTape3.config(text = str(self.TM.tape[0]))
            self.lblTape4.config(text = str(self.TM.tape[1]))
        elif len(self.TM.tape) >= 1:
            self.lblTape3.config(text = str(self.TM.tape[0]))

    def setStartingState(self):
        # if the textbox has a value
        if str(self.txtStartState.get("1.0", END)) != "":
            # it will get the value
            self.TM.starting_state = str(self.txtStartState.get("1.0", END))
            # and set that as the next starting state
            self.TM.starting_state = self.TM.starting_state[:-1]
            print "starting State set to: ", self.TM.starting_state
            self.lblStartingState.config(text = "Starting State: " + self.TM.starting_state)
            # emptys the textbox
            self.txtStartState.delete(1.0, END)

    def setTapePosition(self):
        # if the textbox has a value
        if str(self.txtTapePosition.get()) != "":
            # and if the int value in is more than 0 (avoids setting position in the minus')
            if int(str(self.txtTapePosition.get())) >= 0:    
                # sets the new tape position
                self.TM.tape_position = int(self.txtTapePosition.get())
                print "Tape Position set to: ", str(self.TM.tape_position)
                self.lblTapePosition.config(text = "Tape Position: " + str(self.TM.tape_position))
                # deletes the textbox contents
                self.txtTapePosition.delete(0, END)
                # and resets the tape positions before moving the tape to the right
                self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
                # moves the tape to the right on the tape position number
                for x in range(self.TM.tape_position):
                    app.scrollRight()

    def finaliseTape(self):
        finaltapestr = ""

        # removes the blank symbols on the front of the tape
        while self.TM.tape[0] == "#":
            self.TM.tape.pop(0)
            if self.TM.tape[0] != "#":
                break
        # removes the blank symbols on the end of the tape
        if len(self.TM.tape) > 1:
            while self.TM.tape[-1] == "#":
                self.TM.tape.pop(-1)
                if self.TM.tape[-1] != "#":
                    break

        # finialises the tape and makes it readable for the user
        for index in range (len(self.TM.tape)):
            finaltapestr += "[" + str(self.TM.tape[index]) + "] "
        return finaltapestr

    def runMachine(self):
        # resets the GUI tape positions beack to its initial state
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
        # re-fills the tape
        self.fillTape()
        root.update()
        # starts the machine using the Turing machine instance
        self.TM.startMachine()

    # displays a popup window showing the final tape of the machine
    def finalTapePopup(self):

        # calls finaliseTape to get the string to print to the popup window
        finaltape_str = self.finaliseTape()

        popup_finaltape = Toplevel()
        popup_finaltape.title("Final Tape")
        popup_finaltape.geometry("300x150+750+250")
        # sets the final tape on the pop up
        lblInstructionFound = Label(popup_finaltape, text = "Final Tape: " + finaltape_str)
        lblInstructionFound.pack()

        lblFinalTape = Label(popup_finaltape, text = finaltape_str)
        lblFinalTape.pack()

        btnDismiss = Button(popup_finaltape, text="Dismiss Window", command = popup_finaltape.destroy)
        btnDismiss.pack()

        btnDismiss.focus()

        # when the popup runs, the machine will reset allowing for another instance of the Turing Machine to run
        self.resetMachine()

    def helpPopup(self):
        # string for the help window, explaining how to use the machine
        help_string = """A turing machine works by a set of instructions and acting accordingly depending on what state the machine is and what is present on the tape
        An example instruction would be, if in state A and symbol is 0, change symbol to 1 and move to state B, then move right.
        
        <--- All INSTRUCTIONS LIST --->
	        the instructions can be read as follows
	        [STATE, SYMBOL, DIRECTION, NEW SYMBOL, NEW STATE]
        
        <--- ADD INSTRUCTIONS --->
	        instructions can be added to the machine on the right side of the window and will be appeneded to the All Instructions window in the center
        
        <--- INSERT TAPE --->
	        to insert a tape use comma seperated values such as [1, 2, 1, 2, 3, 4, 1, 2]
	        this will then show on the tape at the top of the window
        
        <--- INSERT STARTING STATE --->
	        allows you to change teh starting state of the machine and will be displayed at the bottom of the window
        
        <--- SPEED --->
	        allows for change of speed for a max of 10 (will run instantly) and min of 0
        
        <--- TAPE POSITION --->
	        allows the setting of changing the position on the tape, to any value above 0
        
        <--- RESET AND LOAD DATA FROM FILE --->
	        allows the use of pre loaded data into the machine of instructions and a tape. State and position will be set seperatly
	        use files instructions.txt and tape.txt
	        instructions are written in format: state,symbol,direction,new_symbol,new_state A,1,R,0,B (each line will represent a new instruction)
	        tape is written in format: 1,2,3,1,2,3,4,1
        
        <--- TAPE DIRECTION --->
	        use the arrows on either side of the tape to navigate through the tape (viewing experience only whilst the machine is not running)
        
        <--- RUNNING INSTRUCTIONS --->
	        will show the currently executed instructions                  
        
        <--- CLEAR ALL INSTRUCTIONS --->
	        clears all of the instructions from the machine                 """

        popup_finaltape = Toplevel()
        popup_finaltape.title("Help")
        popup_finaltape.geometry("1000x650+750+250")
        lblInstructionFound = Label(
            popup_finaltape, 
            text = help_string)
        lblInstructionFound.pack()

        btnDismiss = Button(popup_finaltape, text="Dismiss Window", command = popup_finaltape.destroy)
        btnDismiss.pack()

        btnDismiss.focus()

    def clearInstructions(self):
        # resets the instructions on the machine
        self.TM.temp_instructions = {}
        # this avoids key errors, and creates the key if it does not exist
        self.TM.temp_instructions = defaultdict(dict)
        self.lstShowInstructions.delete(0, END)

    def resetMachine(self):
        # resets everything in the machine to its default attributes
        self.lblTape0.config(text = "#")
        self.lblTape1.config(text = "#")
        self.lblTape2.config(text = "#")
        self.lblTape3.config(text = "#")
        self.lblTape4.config(text = "#")
        self.lblTape5.config(text = "#")
        self.lblTape6.config(text = "#")
        self.lblTape7.config(text = "#")
        self.TM.tape_position = 0
        self.TM.tape = []
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]  # positions of the tape, which will change depending on left or right
        self.TM.available_states = {}
        self.TM.temp_instructions = {}
        self.TM.temp_instructions = defaultdict(dict)
        self.TM.state = None
        self.TM.starting_state = None
        self.TM.original_tape = []
        self.TM.current_state = None
        self.lstShowInstructions.delete(0,END)

        self.lblStartingState.config(text = "Starting State: N/A")
        self.lblTapePosition.config(text = "Tape Position: 0")

        self.lblScannedState.config(text = "N/A")
        self.lblScannedSymbol.config(text = "N/A")
        self.lblDirection.config(text = "N/A")
        self.lblNewSymbol.config(text = "N/A")
        self.lblNewState.config(text = "N/A")
        
        root.update()

    def loadFromFile(self):
        instruction = []
        # resets the machine before loading from a file
        self.resetMachine()
        try:
            # sets the file to the instructions.txt for reading
            file = open("instructions.txt", "r")
        except IOError: # IOError handles if the file does not exist
            print "Instructions file does not exist"
            return
        for line in file:
            # for each line in the file, it is stripped and split using commas, and appaended to the instructions 2D list
            instruction = map(str, line.strip().split(','))
            self.TM.setInstruction(instruction[0], instruction[1], instruction[2], instruction[3], instruction[4])
        file.close

        try:
            # sets teh file to tape.txt for reading
            file = open("tape.txt", "r")
        except IOError: # IOError for if the file does not exist
            print "Tape file does not exist"
            return
        for line in file:
            # reads the tape from the file, using CSV
            self.TM.tape = map(str, line.strip().split(','))
        self.fillTape()
        self.TM.original_tape = self.TM.tape

        file.close        

class Transition:

    # if the state machine cannot run the transition between each state this will serve as a default message
    def executeInstruction(self):
        print "Cannot Execute Instruction"
        return False


class TuringState(State, Transition):
    ''' this will serve as the main state in the state machine and will be used to
    dynamically create the states needed in the machine this is done through looking
    through the instructions provided and adding the states which have been speicifed
    as a TuringState() object. This means that there will be multiple of this state in
    the state machine, each representing the different states in the State and Turing Machine'''

    # depending on the state the machine is in, a dictionary will be used to contain all
        # instructions which can be executed in the current state. This will be different with each state in the machine

    instructions = {}

    # when the state is created the instructions which are relevent to the state will be passed in through a
        # parameter and then saved in the current states instructions dictionary

    def __init__(self, context, new_instructions):
        State.__init__(self, context)
        self.instructions = new_instructions

    def executeInstruction(self):
        print "(" + str(self.instructions) + ") Instructions Asociated with State: (" + self.current_context.state

        # the machine gets the current symbol on the tape and saves it to a variable to be used

        current_symbol = self.current_context.tape[self.current_context.tape_position]

        # if the symbol on the tape exists in the instructions, the instructions relevent to
            # the symbol will be carried out

        if current_symbol in self.instructions:

            # prints out the current state of the machine and has a sleep for readability

            print "(" + self.current_context.state + ") Current State"
            app.lblScannedState.config(text = self.current_context.state)
            sleep(self.current_context.time)
            root.update()

            # prints the current symbol read from the tape

            app.lblScannedSymbol.config(text = current_symbol)
            sleep(self.current_context.time)
            root.update()

            # prints the direction the machine will take next

            print "(" + self.instructions[current_symbol][DIRECTION] + ") Direction"
            app.lblDirection.config(text = self.instructions[current_symbol][DIRECTION])
            sleep(self.current_context.time)
            root.update()

            # the machine will then change the current symbol on the tape to the new symbol provided in the instructions

            self.current_context.tape[self.current_context.tape_position] = self.instructions[current_symbol][NEW_SYMBOL]
            print "(" + self.instructions[current_symbol][NEW_SYMBOL] + ") New Symbol"
            app.lblNewSymbol.config(text = self.instructions[current_symbol][NEW_SYMBOL])
            sleep(self.current_context.time)
            root.update()

            # then the machine will transition to the new state in the machine

            self.current_context.setState(self.instructions[current_symbol][NEXT_STATE])
            print "(" + self.instructions[current_symbol][NEXT_STATE] + ") New State"
            app.lblNewState.config(text = self.instructions[current_symbol][NEXT_STATE])
            sleep(self.current_context.time)
            root.update()

            # the machine will move either left or right depending on the instructions,
                # if an invalid direction is provided, the heads position on the tape will not move

            if self.instructions[current_symbol][DIRECTION] == "R":
                if self.current_context.tape_position >= (len(self.current_context.tape) - 2):
                    self.current_context.tape += ["#"]
                self.current_context.tape_position += 1
                app.scrollRight()
                root.update()
            elif self.instructions[current_symbol][DIRECTION] == "L":
                self.current_context.tape = ["#"] + self.current_context.tape
                app.scrollLeft()
                root.update()
            else:
                print "Not a Valid Direction"
            print "New Tape: ", self.current_context.tape
        else:
            return False


class TuringMachine(StateContext, Transition):
    ''' the main TuringMachine class will be the main way to access the state machine
    and set all of the correct attributes for defining the condition of the Turing Machine.
    This class will also include methods for adding an instruction to the temp_instructions
    dictionary which will handle all of the states in the machine and their associated instructions,
    as well as handle adding all of the states to the machine'''

    def __init__(self):

        # default attributes for the Turing Machine

        self.tape = []
        self.original_tape = []
        self.starting_state = None
        self.tape_position = 0
        self.time = 0.2
        
        # this will hold all of the instructions before they are initalised in the machine,
            # this is a nested dictionary containing 2 sets of keys,
            # the state keys and the symbol keys
        
        self.temp_instructions = {}

        # this is used through the collections library, giving the ability to create a key
            # in the nested dictionary if none is present

        self.temp_instructions = defaultdict(dict)

    # calls the correct method with the current state of the machine
    def executeInstruction(self):
        return self.current_state.executeInstruction()

    # this method is used to save an instruction to the machines temporary dictionary.
        # This will be called whenever a single instruction is submitted and adds the
        # instruction or creates a new key if needed in the nested dictionary

    def setInstruction(self, state, symbol, direction, new_symbol, new_state):
        
        # saves the instruction to the nested dictionary using the state and the symbol provided,
            # while saving a list of the actions the machine will take

        self.temp_instructions[state][symbol] = [direction, new_symbol, new_state]
        sinstruction = "[" + state + ", " + symbol + "]:    " + str(self.temp_instructions[state][symbol])
        app.lstShowInstructions.insert(END, sinstruction)

    # this method will initalise the machine when all of the instructions are present.
        # The machine will create the states dynamically depending on what instructions are saved
        
    def startMachine(self):

        # depending on the tape position, the machine will scroll right that many times to appear correctly on the GUI

        for x in range(self.tape_position):
            app.scrollRight()

        # firstly the machine will get all of the keys (states) that are used in the instructions
        states = self.temp_instructions.keys()  

        # if there is not starting state, the first state in the instructions will be set as so

        if self.starting_state is None:
            self.starting_state = states[0]
            print "Starting State set to: " + self.starting_state
            app.lblStartingState.config(text = "Starting State: " + self.starting_state)

        # and will then cycle through the states and add them to the machine with the instructions
            # associated with each state, passed in via a method parameter

        for state in states:
            self.availableStates[state] = TuringState(self, self.temp_instructions[state])

        # the machine will then go through all of the states that the machine should be able to transition to
            # and if it does not exist it will create it by looking into the nested dictionaries contents.
            # If the state does not exist it will be create with an empty set of instructions, these instructions
            # are set to be empty as the state will not transition anywhere

        for state in self.temp_instructions:
            for symbol in self.temp_instructions[state]:
                if self.temp_instructions[state][symbol][NEXT_STATE] not in self.availableStates.keys():
                    self.availableStates[self.temp_instructions[state][symbol][NEXT_STATE]] = TuringState(self, {})

        # the starting state will then be set
        self.setState(self.starting_state)

        # runs the machine while the machine does not reach a HALT or finds instructions
        while (True):
            if self.state == "HALT":
                app.finalTapePopup()
                break
            if (self.executeInstruction() == False):
                app.finalTapePopup()
                break


if __name__ == '__main__':
    root = Tk()
    app = TuringMachineGUI(root)
    root.geometry("750x480+250+250")
    root.title("Dynamic Custom Turing Machine")
    root.mainloop()

