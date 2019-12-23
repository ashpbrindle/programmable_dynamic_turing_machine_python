from State import State, StateContext
from time import sleep
import sys
from Tkinter import *
import tkMessageBox

class TuringMachineGUI():
    def __init__(self, window):
        self.tape_font = ("times", 20)
        self.position_font = ("times", 15, "italic")
        self.instruction_font = ("times", 15)
        self.addInstruction_font = ("times", 10)
        self.dropdown_font = ("times", 10)
        self.currentInstruction_font = ("times", 10)
        self.arrow_font = ("calibri", 10, "bold")
        self.run_font = ("bold")
        self.submitTape_font = ("calibri", 10, "bold")
        self.run_font = ("calibri", 15, "bold")
        self.title_font = ("times", 15)
        self.title2_font = ("times", 11)

        # these attributes are used before starting the machine and are passed in when starting
        # includes the tape full of blank symbols, tape position which can be changed, as well as the starting state
        self.tape = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        self.tape_position = 0
        self.starting_state = "A"

        # list used to display the instructions on the GUI listbox
        self.list_instructions = [
            "State   Symbol   Dir   New Symbol   New State", 
            "A        1             R      H                     B", 
            "-----------------------------------------------------",
            "B        2             R      E                     C", 
            "-----------------------------------------------------",
            "C        3             R      L                     D", 
            "-----------------------------------------------------",
            "D        4             R      L                     E", 
            "-----------------------------------------------------",
            "E        5             R      O                     F", 
            "-----------------------------------------------------",
            "F        6             R      _                     G",  
            "-----------------------------------------------------",
            "G        7             R      W                     H",
            "-----------------------------------------------------",
            "H        8             R      O                     I",
            "-----------------------------------------------------",
            "I        9             R      R                     J",
            "-----------------------------------------------------",
            "J        10            R      L                     K",
            "-----------------------------------------------------",
            "K        11            R      D                     L",
            "-----------------------------------------------------",
            "L        12            R      !                     A"]

        # a list for the tape dropdown
        self.tape_options = [
            "Empty Tape",
            "[1,2,3,4,5,6,7,8,9,10,11,12,END (Hello_World)",
            "[1,2,3,4,5,END] (Hello)",
            "[7,8,9,10,11,12,END] (World)"]

        # dictionary holding all of the tapes associated with each option
        self.tapes = {
            "Empty Tape": ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            "[1,2,3,4,5,6,7,8,9,10,11,12,END (Hello_World)": ["1","2","3","4","5","6","7","8","9","10","11","12","END"],
            "[1,2,3,4,5,END] (Hello)": ["1","2","3","4","5","END"],
            "[7,8,9,10,11,12,END] (World)": ["7","8","9","10","11","12","END"]
        }

        # a dictionary handling each starting state asociated with each option
        self.starting_states = {
            "Empty Tape": "A",
            "[1,2,3,4,5,6,7,8,9,10,11,12,END (Hello_World)": "A",
            "[1,2,3,4,5,END] (Hello)": "A",
            "[7,8,9,10,11,12,END] (World)": "G"
        }

        # a dictionary to handle the starting positions of each option
        self.tape_positions = {
            "Empty Tape": 0,
            "[1,2,3,4,5,6,7,8,9,10,11,12,END (Hello_World)": 0,
            "[1,2,3,4,5,END] (Hello)": 0,
            "[7,8,9,10,11,12,END] (World)": 0
        }

        # handles the positions each tape value will appear on the tape
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
        # method to draw out the GUI on the window
        self.drawWindow()

    # handles drawing the window
    def drawWindow(self):

        self.lblPositions = Label(
            root,
            text= "-3             -2             -1             0              1              2              3              4",
            fg = "gray26",
            font = self.position_font)
        self.lblPositions.pack()
        self.lblPositions.place(x = 80, y = 5)

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

        self.lblSelectTapeTitle = Label(
            root,
            text = "Select Machine Tape:",
            font = self.title_font)
        self.lblSelectTapeTitle.pack()
        self.lblSelectTapeTitle.place(x = 468, y = 115)

        self.selected_tape = StringVar()
        self.selected_tape.set(self.tape_options[0])
        self.optTape = OptionMenu(
            root,
            self.selected_tape,
            *self.tape_options,
            command = self.selections)
        self.optTape.pack()
        self.optTape.config(
            bg = "white",
            fg = "black",
            font = self.dropdown_font,
            width = 36,
            borderwidth = 1,
            relief = "solid",
            justify = LEFT)
        self.optTape["menu"].config(
            bg = "white",
            fg = "black",
            font = self.dropdown_font,
            borderwidth = 1,
            relief = "solid")
        self.optTape.place(x = 468, y = 143)

        self.lblInstructionsTitle = Label(
            root,
            text = "Running Instruction:",
            font = self.title_font)
        self.lblInstructionsTitle.pack()
        self.lblInstructionsTitle.place(x = 468, y = 293)

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
        self.lblInstructionsBorder.place(x = 468, y = 210)

        self.lblScannedState = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblScannedState.pack()
        self.lblScannedState.place(x = 665, y = 214)

        self.lblScannedSymbol = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblScannedSymbol.pack()
        self.lblScannedSymbol.place(x = 665, y = 236)

        self.lblDirection = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblDirection.pack()
        self.lblDirection.place(x = 665, y = 256)

        self.lblNewSymbol = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblNewSymbol.pack()
        self.lblNewSymbol.place(x = 665, y = 276)

        self.lblNewState = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblNewState.pack()
        self.lblNewState.place(x = 665, y = 298)

        self.lblAllInstructionsTitle = Label(
            root,
            text = "All Instructions:",
            font = self.title_font)
        self.lblAllInstructionsTitle.pack()
        self.lblAllInstructionsTitle.place(x = 30, y = 115)

        self.instructionsFrame = Frame(
            root,
            borderwidth = 2,
            relief = "solid")
        self.instructionsFrame.pack()
        self.instructionsFrame.place(x = 30, y = 140)

        self.scrlInstructions = Scrollbar(self.instructionsFrame)
        self.scrlInstructions.pack(side = "right", fill = "y")

        self.lstShowInstructions = Listbox(
            self.instructionsFrame,
            bg = "white",
            yscrollcommand = self.scrlInstructions.set,
            fg = "black",
            height = 13,
            width = 40,
            font = self.instruction_font)
        self.lstShowInstructions.pack(side = "left", fill = "y")
        self.scrlInstructions.config(command = self.lstShowInstructions.yview)

        for x in range(len(self.list_instructions)):
            self.lstShowInstructions.insert(x, self.list_instructions[x])

        self.btnHelp = Button(
            root,
            text = "Help",
            bg = "DarkGoldenRod3",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 36,
            borderwidth = 1,
            relief = "solid",
            command = self.helpPopup)
        self.btnHelp.pack()
        self.btnHelp.place(x = 468, y = 375)

        self.btnRun = Button(
            root,
            text = "Run Machine",
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 36,
            borderwidth = 1,
            relief = "solid",
            command = self.runMachine)
        self.btnRun.pack()
        self.btnRun.place(x = 468, y = 340)

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
        self.btnExit.place(x = 468, y = 410)

        self.imgStates = Canvas(root)
        self.imgStates.config(width = 6000, height = 500)
        self.photoState = PhotoImage(file = "TM_Hello_World_State_Diagram_small.gif")
        self.imgStates.create_image(0,0, image = self.photoState, anchor="nw")
        self.imgStates.place(x = 750, y = 60)

    # when selecting an item from the tape drop down menu, this method is called
    def selections(self, item):
        # depending on tape selected, the tape, state and tape position will change before starting the machine
        self.tape = self.tapes[item][:]
        self.starting_state = self.starting_states[item]
        self.tape_position = self.tape_positions[item]
        # the next method handles filling the GUI tape
        self.fillTape()
        # moves the tape to the correct position
        if self.tape_position >= 0:
            for pos in range(self.tape_position):
                self.scrollRight(self.tape)
        # updates the GUI
        root.update()

    # this method will move the GUI tape along to the left
    # this is done through the use of a list defining the positions of each element of the tape for the GUI tape
    def scrollLeft(self, current_tape):
        if len(current_tape) > 0:

            # this will check where the tape values are positioned on the tape and any blank squares will be made blank (#)

            if self.GUI_tape_positions[3] == -1:
                for index in range(len(self.GUI_tape_positions)):
                    self.GUI_tape_positions[index] += 1

            if self.GUI_tape_positions[3] > -1:
                if self.GUI_tape_positions[0] > -1:
                    self.lblTape0.config(text = str(current_tape[self.GUI_tape_positions[0]]))
                else:
                    self.lblTape0.config(text = "#")
                if self.GUI_tape_positions[1] > -1:
                    self.lblTape1.config(text = str(current_tape[self.GUI_tape_positions[1]]))
                else:
                    self.lblTape1.config(text = "#")
                if self.GUI_tape_positions[2] > -1:
                    self.lblTape2.config(text = str(current_tape[self.GUI_tape_positions[2]]))
                else:
                    self.lblTape2.config(text = "#")
                if self.GUI_tape_positions[3] < len(current_tape):
                    self.lblTape3.config(text = str(current_tape[self.GUI_tape_positions[3]]))
                else:
                    self.lblTape3.config(text = "#")
                if self.GUI_tape_positions[4] < len(current_tape):
                    self.lblTape4.config(text = str(current_tape[self.GUI_tape_positions[4]]))
                else:
                    self.lblTape4.config(text = "#")
                if self.GUI_tape_positions[5] < len(current_tape):
                    self.lblTape5.config(text = str(current_tape[self.GUI_tape_positions[5]]))
                else:
                    self.lblTape5.config(text = "#")
                if self.GUI_tape_positions[6] < len(current_tape):
                    self.lblTape6.config(text = str(current_tape[self.GUI_tape_positions[6]]))
                else:
                    self.lblTape6.config(text = "#")
                if self.GUI_tape_positions[7] < len(current_tape):
                    self.lblTape7.config(text = str(current_tape[self.GUI_tape_positions[7]]))
                else:
                    self.lblTape7.config(text = "#")

    # this method will move the GUI tape along to the right
    # and will use the GUI tape positions list to determine where the positioning of each tape value will be on the GUI
    # any blank symbols will be filled with (#) to represent it
    def scrollRight(self, current_tape):
        if len(current_tape) > 0:

            for index in range(len(self.GUI_tape_positions)):
                self.GUI_tape_positions[index] += 1

            if self.GUI_tape_positions[0] < len(current_tape) and self.GUI_tape_positions[0] >= 0:
                self.lblTape0.config(text = str(current_tape[self.GUI_tape_positions[0]]))
            else:
                self.lblTape0.config(text = "#")
            if self.GUI_tape_positions[1] < len(current_tape) and self.GUI_tape_positions[1] >= 0:
                self.lblTape1.config(text = str(current_tape[self.GUI_tape_positions[1]]))
            else:
                self.lblTape1.config(text = "#")
            if self.GUI_tape_positions[2] < len(current_tape) and self.GUI_tape_positions[2] >= 0:
                self.lblTape2.config(text = str(current_tape[self.GUI_tape_positions[2]]))
            else:
                self.lblTape2.config(text = "#")
            if self.GUI_tape_positions[3] < len(current_tape):
                self.lblTape3.config(text = str(current_tape[self.GUI_tape_positions[3]]))
            else:
                self.lblTape3.config(text = "#")
            if self.GUI_tape_positions[4] < len(current_tape):
                self.lblTape4.config(text = str(current_tape[self.GUI_tape_positions[4]]))
            else:
                self.lblTape4.config(text = "#")
            if self.GUI_tape_positions[5] < len(current_tape):
                self.lblTape5.config(text = str(current_tape[self.GUI_tape_positions[5]]))
            else:
                self.lblTape5.config(text = "#")
            if self.GUI_tape_positions[6] < len(current_tape):
                self.lblTape6.config(text = str(current_tape[self.GUI_tape_positions[6]]))
            else:
                self.lblTape6.config(text = "#")
            if self.GUI_tape_positions[7] < len(current_tape):
                self.lblTape7.config(text = str(current_tape[self.GUI_tape_positions[7]]))
            else:
                self.lblTape7.config(text = "#")

            if self.GUI_tape_positions[3] > len(current_tape):
                for index in range(len(self.GUI_tape_positions)):
                    self.GUI_tape_positions[index] -= 1

    # this method will fill the GUI tape with the updated values
    def fillTape(self):
        # initially resets the GUI tapes attributes
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
        self.lblTape0.config(text = "#")
        self.lblTape1.config(text = "#")
        self.lblTape2.config(text = "#")
        self.lblTape3.config(text = "#")
        self.lblTape4.config(text = "#")
        self.lblTape5.config(text = "#")
        self.lblTape6.config(text = "#")
        self.lblTape7.config(text = "#")

        # fills the GUI tape with the tape depending on the size
        if len(self.tape) >= 5:
            self.lblTape3.config(text = str(self.tape[0]))
            self.lblTape4.config(text = str(self.tape[1]))
            self.lblTape5.config(text = str(self.tape[2]))
            self.lblTape6.config(text = str(self.tape[3]))
            self.lblTape7.config(text = str(self.tape[4]))
        elif len(self.tape) >= 4:
            self.lblTape3.config(text = str(self.tape[0]))
            self.lblTape4.config(text = str(self.tape[1]))
            self.lblTape5.config(text = str(self.tape[2]))
            self.lblTape6.config(text = str(self.tape[3]))
        elif len(self.tape) >= 3:
            self.lblTape3.config(text = str(self.tape[0]))
            self.lblTape4.config(text = str(self.tape[1]))
            self.lblTape5.config(text = str(self.tape[2]))
        elif len(self.tape) >= 2:
            self.lblTape3.config(text = str(self.tape[0]))
            self.lblTape4.config(text = str(self.tape[1]))
        elif len(self.tape) >= 1:
            self.lblTape3.config(text = str(self.tape[0]))

    # this method will make the tape more readable when the machine has finished, and removing any excess blank symbols added to either side of the tape
    def finaliseTape(self):
        finaltapestr = ""
        # removes blank symbols on the front of the tape
        while self.TM.tape[0] == "#":
            self.TM.tape.pop(0)
            if self.TM.tape[0] != "#":
                break
        # removes blank symbols on the end of the tape
        if len(self.TM.tape) > 1:
            while self.TM.tape[-1] == "#":
                self.TM.tape.pop(-1)
                if self.TM.tape[-1] != "#":
                    break

        # puts each value in a [] to symblise a square on the tape
        for index in range (len(self.TM.tape)):
            finaltapestr += "[" + str(self.TM.tape[index]) + "] "
        return finaltapestr

    # initialises and starts the machine
    def runMachine(self):
        # creates a new instance of the Turing machine using the defined state, tape and position
        self.TM = TuringMachine(self.starting_state, self.tape, self.tape_position)
        root.update()
        # starts to initialise/run the machine
        self.TM.runMachine()

    # resets all machine attributes to its default settings
    def resetMachine(self):
        self.lblTape0.config(text = "#")
        self.lblTape1.config(text = "#")
        self.lblTape2.config(text = "#")
        self.lblTape3.config(text = "#")
        self.lblTape4.config(text = "#")
        self.lblTape5.config(text = "#")
        self.lblTape6.config(text = "#")
        self.lblTape7.config(text = "#")
        self.TM.tape_position = 0
        self.TM.tape = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]

        # positions of the tape, which will change depending on left or right
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]  # positions of the tape, which will change depending on left or right

        self.lblScannedState.config(text = "N/A")
        self.lblScannedSymbol.config(text = "N/A")
        self.lblDirection.config(text = "N/A")
        self.lblNewSymbol.config(text = "N/A")
        self.lblNewState.config(text = "N/A")
        root.update()

    # produces a popup window displaying the final tape of the machine
    def finalTapePopup(self):

        finaltape_str = self.finaliseTape()

        popup_finaltape = Toplevel()
        popup_finaltape.title("Final Tape")
        popup_finaltape.geometry("300x150+750+250")
        lblInstructionFound = Label(popup_finaltape, text = "Final Tape")
        lblInstructionFound.pack()

        lblFinalTape = Label(popup_finaltape, text = finaltape_str)
        lblFinalTape.pack()

        btnDismiss = Button(popup_finaltape, text="Dismiss Window", command = popup_finaltape.destroy)
        btnDismiss.pack()

        btnDismiss.focus()

        self.resetMachine()

    def helpPopup(self):
        # string for the help window, explaining how to use the machine
        help_string = """A turing machine works through actions depending on the instructions in the machine
        for example; if the machine were to be in state A and read a 1 on the tape, it will then proceed to change it to 0, change state to B and move Right
        this will then trigger another instruction to execute if one is present.

        To select a tape, use the drop down menu above for some examples to use, and hit the run button to watch the machine operate
        Each of the instructions are shown on the left of the window and will show in a section (above the run button) the process the machine is taking
        A state diagram is also provided to help the user identify what is happening on that tape at any given time
        
        PICK A TAPE
        WATCH THE MACHINE RUN!"""

        popup_finaltape = Toplevel()
        popup_finaltape.title("Help")
        popup_finaltape.geometry("1000x200+750+250")
        lblInstructionFound = Label(
            popup_finaltape, 
            text = help_string)
        lblInstructionFound.pack()

        btnDismiss = Button(popup_finaltape, text="Dismiss Window", command = popup_finaltape.destroy)
        btnDismiss.pack()

        btnDismiss.focus()
# a transition class used to handle if any of the methods cannot be called in the current machine state
class Transition:
    def foundBlank(self):
        print "Error, [#] or Blank Symbol instruction not found in current state"
        return False

    def found1(self):
        print "Error, [1] instruction not found in current state"
        return False

    def found2(self):
        print "Error, [2] instruction not found in current state"
        return False

    def found3(self):
        print "Error, [3] instruction not found in current state"
        return False

    def found4(self):
        print "Error, [4] instruction not found in current state"
        return False

    def found5(self):
        print "Error, [5] instruction not found in current state"
        return False

    def found6(self):
        print "Error, [6] instruction not found in current state"
        return False

    def found7(self):
        print "Error, [7] instruction not found in current state"
        return False

    def found8(self):
        print "Error, [8] instruction not found in current state"
        return False

    def found9(self):
        print "Error, [9] instruction not found in current state"
        return False

    def found10(self):
        print "Error, [10] instruction not found in current state"
        return False

    def found11(self):
        print "Error, [11] instruction not found in current state"
        return False

    def found12(self):
        print "Error, [12] instruction not found in current state"
        return False

    def foundEND(self):
        print "Error, END instruction not found in current state"
        return False

# one of the states of the machine which will handle changing the tape and the machines state depending on the method called
class TuringStateA(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    # if the machine finds a 0 on the tape it will
    def found1(self):
        # display the current state on the GUI
        print "(A) Current State"
        app.lblScannedState.config(text = "A")
        root.update()
        sleep(0.2)
        
        # display the current symbol read on the tape
        print "(1) Symbol on Tape"
        app.lblScannedSymbol.config(text = "1")
        root.update()
        sleep(0.2)

        # display the direction of the head
        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)
        
        # using current context changes the symbol on the turing machine tape
        self.current_context.tape[self.current_context.tape_position] = "H"
        print "(H) New Symbol on Tape"
        app.lblNewSymbol.config(text = "H")
        root.update()
        sleep(0.2)
        
        # using current context changes to the next state of the machine
        self.current_context.setState("B")
        print "(B) New State"
        app.lblNewState.config(text = "B")
        root.update()
        
        # proceeds to move the tape to the right on the list
        self.current_context.moveRight()
        # and moves the tape right on the GUI
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateB(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found2(self):
        print "(B) Current State"
        app.lblScannedState.config(text = "B")
        root.update()   
        sleep(0.2)

        print "(2) Symbol on Tape"
        app.lblScannedSymbol.config(text = "2")
        root.update()
        sleep(0.2)
        
        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)
        
        self.current_context.tape[self.current_context.tape_position] = "E"
        print "(E) New Symbol on Tape"
        app.lblNewSymbol.config(text = "E")
        root.update()
        sleep(0.2)
        
        self.current_context.setState("C")
        print "(C) New State"
        app.lblNewState.config(text = "C")
        root.update()
        
        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateC(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found3(self):
        print "(C) Current State"
        app.lblScannedState.config(text = "C")
        root.update()
        sleep(0.2)

        print "(3) Symbol on Tape"
        app.lblScannedSymbol.config(text = "3")
        root.update()
        sleep(0.2)
        

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)

        self.current_context.tape[self.current_context.tape_position] = "L"
        print "(L) New Symbol on Tape"
        app.lblNewSymbol.config(text = "L")
        root.update()
        sleep(0.2)

        self.current_context.setState("D")
        print "(D) New State"
        app.lblNewState.config(text = "D")
        root.update()

        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)

        return True

    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateD(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found4(self):
        print "(D) Current State"
        app.lblScannedState.config(text = "D")
        root.update()
        sleep(0.2)

        print "(4) Symbol on Tape"
        app.lblScannedSymbol.config(text = "4")
        root.update()
        sleep(0.2)

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)

        self.current_context.tape[self.current_context.tape_position] = "L"
        print "(L) New Symbol on Tape"
        app.lblNewSymbol.config(text = "L")
        root.update()
        sleep(0.2)

        self.current_context.setState("E")
        print "(E) New State"
        app.lblNewState.config(text = "E")
        root.update()

        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True
        
    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateE(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found5(self):
        print "(E) Current State"
        app.lblScannedState.config(text = "E")
        root.update()
        sleep(0.2)
        
        print "(5) Symbol on Tape"
        app.lblScannedSymbol.config(text = "5")
        root.update()
        sleep(0.2)

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)
        
        self.current_context.tape[self.current_context.tape_position] = "O"
        print "(O) New Symbol on Tape"
        app.lblNewSymbol.config(text = "H")
        root.update()
        sleep(0.2)
        
        self.current_context.setState("F")
        print "(F) New State"
        app.lblNewState.config(text = "F")
        root.update()
        
        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateF(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found6(self):
        print "(F) Current State"
        app.lblScannedState.config(text = "F")
        root.update()
        sleep(0.2)
        
        print "(6) Symbol on Tape"
        app.lblScannedSymbol.config(text = "6")
        root.update()
        sleep(0.2)

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)
        
        self.current_context.tape[self.current_context.tape_position] = "_"
        print "(_) New Symbol on Tape"
        app.lblNewSymbol.config(text = "_")
        root.update()
        sleep(0.2)
        
        self.current_context.setState("G")
        print "(G) New State"
        app.lblNewState.config(text = "G")
        root.update()
        
        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateG(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found7(self):
        print "(G) Current State"
        app.lblScannedState.config(text = "G")
        root.update()
        sleep(0.2)
        
        print "(6) Symbol on Tape"
        app.lblScannedSymbol.config(text = "6")
        root.update()
        sleep(0.2)

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)
        
        self.current_context.tape[self.current_context.tape_position] = "W"
        print "(W) New Symbol on Tape"
        app.lblNewSymbol.config(text = "W")
        root.update()
        sleep(0.2)
        
        self.current_context.setState("H")
        print "(H) New State"
        app.lblNewState.config(text = "H")
        root.update()
        
        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateH(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found8(self):
        print "(H) Current State"
        app.lblScannedState.config(text = "H")
        root.update()
        sleep(0.2)
        
        print "(8) Symbol on Tape"
        app.lblScannedSymbol.config(text = "8")
        root.update()
        sleep(0.2)

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)
        
        self.current_context.tape[self.current_context.tape_position] = "O"
        print "(O) New Symbol on Tape"
        app.lblNewSymbol.config(text = "O")
        root.update()
        sleep(0.2)
        
        self.current_context.setState("I")
        print "(I) New State"
        app.lblNewState.config(text = "I")
        root.update()
        
        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateI(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found9(self):
        print "(I) Current State"
        app.lblScannedState.config(text = "I")
        root.update()
        sleep(0.2)
        
        print "(9) Symbol on Tape"
        app.lblScannedSymbol.config(text = "9")
        root.update()
        sleep(0.2)

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)
        
        self.current_context.tape[self.current_context.tape_position] = "R"
        print "(R) New Symbol on Tape"
        app.lblNewSymbol.config(text = "R")
        root.update()
        sleep(0.2)
        
        self.current_context.setState("J")
        print "(J) New State"
        app.lblNewState.config(text = "J")
        root.update()
        
        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateJ(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found10(self):
        print "(J) Current State"
        app.lblScannedState.config(text = "J")
        root.update()
        sleep(0.2)
        
        print "(10) Symbol on Tape"
        app.lblScannedSymbol.config(text = "10")
        root.update()
        sleep(0.2)

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)
        
        self.current_context.tape[self.current_context.tape_position] = "L"
        print "(L) New Symbol on Tape"
        app.lblNewSymbol.config(text = "L")
        root.update()
        sleep(0.2)
        
        self.current_context.setState("K")
        print "(K) New State"
        app.lblNewState.config(text = "K")
        root.update()
        
        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateK(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found11(self):
        print "(K) Current State"
        app.lblScannedState.config(text = "K")
        root.update()
        sleep(0.2)
        
        print "(11) Symbol on Tape"
        app.lblScannedSymbol.config(text = "11")
        root.update()
        sleep(0.2)

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)
        
        self.current_context.tape[self.current_context.tape_position] = "D"
        print "(D) New Symbol on Tape"
        app.lblNewSymbol.config(text = "D")
        root.update()
        sleep(0.2)
        
        self.current_context.setState("L")
        print "(L) New State"
        app.lblNewState.config(text = "L")
        root.update()
        
        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateL(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found12(self):
        print "(L) Current State"
        app.lblScannedState.config(text = "L")
        root.update()
        sleep(0.2)
        
        print "(12) Symbol on Tape"
        app.lblScannedSymbol.config(text = "12")
        root.update()
        sleep(0.2)

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)
        
        self.current_context.tape[self.current_context.tape_position] = "!"
        print "(!) New Symbol on Tape"
        app.lblNewSymbol.config(text = "!")
        root.update()
        sleep(0.2)
        
        self.current_context.setState("A")
        print "(A) New State"
        app.lblNewState.config(text = "A")
        root.update()
        
        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        self.current_context.tape[self.current_context.tape_position] = "#"
        root.update()
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringMachine(StateContext, Transition):
    # when the machine is initialised the state, tape and position will be set
    def __init__(self, starting_state, tape, starting_position):
        self.tape = tape
        self.tape_position = starting_position
        self.starting_state = starting_state
        # a bool to determine if the machine has completed or not
        self.end_of_machine = False

        # in the available states dict the machine creates an instance of each of the TuringStates under keys used to transition between states
        self.availableStates["A"] = TuringStateA(self)
        self.availableStates["B"] = TuringStateB(self)
        self.availableStates["C"] = TuringStateC(self)
        self.availableStates["D"] = TuringStateD(self)
        self.availableStates["E"] = TuringStateE(self)
        self.availableStates["F"] = TuringStateF(self)
        self.availableStates["G"] = TuringStateG(self)
        self.availableStates["H"] = TuringStateH(self)
        self.availableStates["I"] = TuringStateI(self)
        self.availableStates["J"] = TuringStateJ(self)
        self.availableStates["K"] = TuringStateK(self)
        self.availableStates["L"] = TuringStateL(self)

        # sets the starting state to the one specified
        self.setState(self.starting_state)

    def foundBlank(self):
        return self.current_state.foundBlank()

    def found1(self):
        return self.current_state.found1()

    def found2(self):
        return self.current_state.found2()

    def found3(self):
        return self.current_state.found3()

    def found4(self):
        return self.current_state.found4()

    def found5(self):
        return self.current_state.found5()

    def found6(self):
        return self.current_state.found6()

    def found7(self):
        return self.current_state.found7()

    def found8(self):
        return self.current_state.found8()

    def found9(self):
        return self.current_state.found9()

    def found10(self):
        return self.current_state.found10()

    def found11(self):
        return self.current_state.found11()

    def found12(self):
        return self.current_state.found12()

    def foundEND(self):
        return self.current_state.foundEND()

    # a dictionary used to handle what symbols are read on the tape and run the corrisponding method depending on what was read
    # e.g. if (1) was read on the tape, the machine will run self.found1 form the dictionary
    def runMachine(self):
        symbols = {
            "#": self.foundBlank,
            "1": self.found1,
            "2": self.found2,
            "3": self.found3,
            "4": self.found4,
            "5": self.found5,
            "6": self.found6,
            "7": self.found7,
            "8": self.found8,
            "9": self.found9,
            "10": self.found10,
            "11": self.found11,
            "12": self.found12,
            "END": self.foundEND
        }
        print "\nStarting Tape: ", self.tape
        print "\n - - - - - - - - - - - - - -  \n"

        # for loop which will run through the machine and call the correct methods until the machine reaches a Halting state
        while self.end_of_machine is False:
            if symbols[self.tape[self.tape_position]]() is False:
                break

            # resets the GUI instructions when new instructions are read
            app.lblScannedState.config(text = "N/A")
            app.lblScannedSymbol.config(text = "N/A")    
            app.lblDirection.config(text = "N/A")
            app.lblNewSymbol.config(text = "N/A")
            app.lblNewState.config(text = "N/A")
                
        # when finished the machines tape is finalised
        app.finalTapePopup()

    # handles moving right on the tape
    def moveRight(self):    
        if self.tape_position >= len(self.tape) -2:
            # a # will be added to the end to stop any out of range errors by the GUI
            self.tape.append("#") 
        # moves along once to the right of the tape
        self.tape_position += 1 

    # handles moving left on the tape
    def moveLeft(self):
        # the machine will add a # to the start of the tape to stop any out of rang errors by the GUI
        self.tape = ["#"] + self.tape


if __name__ == "__main__":

    root = Tk()
    app = TuringMachineGUI(root)
    root.geometry("1375x500+250+250")
    root.title("Hello World")
    root.mainloop()