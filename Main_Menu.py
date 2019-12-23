from Tkinter import *
import os

class MainMenu():
    def __init__(self, window):
        # pre-defined fonts for the GUI
        self.title_font = ("times", 15)
        self.dropdown_font = ("times", 10)
        self.submit_font = ("calibri", 10, "bold") 

        # default selection for the drop down menu
        self.machine_selection = "Unary Multiplication Turing Machine"

        # drop down options dict for the state diagram images
        self.machine_state_diagrams = {
            "Unary Multiplication Turing Machine": "TM_multiply_unary_State_Diagram.gif",
            "Unary Addition Turing Machine": "TM_addition_unary_State_Diagram.gif",
            "Hello World Turing Machine": "TM_Hello_World_State_Diagram.gif",
            "Flip 1 | 0 Turing Machine": "TM_flip_1_0_State_Diagram.gif",
            "Infinite Loop, Odd Number of 0s Turing Machine": "TM_odd_number_0s_State_Diagram.gif"
        }

        # drop down options list
        self.turing_machine_options = [
            "Unary Multiplication Turing Machine",
            "Unary Addition Turing Machine",
            "Hello World Turing Machine",
            "Flip 1 | 0 Turing Machine",
            "Infinite Loop, Odd Number of 0s Turing Machine"]

        # drop down options dict for running the python files
        self.machines = {
            "Unary Multiplication Turing Machine": "python TM_multiply_unary.py",
            "Unary Addition Turing Machine": "python TM_addition_unary.py",
            "Hello World Turing Machine": "python TM_Hello_World.py",
            "Flip 1 | 0 Turing Machine": "python TM_flip_1_0.py",
            "Infinite Loop, Odd Number of 0s Turing Machine": "python TM_odd_number_0s.py"
        }
        self.drawWindow()

    # handles drawing all of the GUI aspects of the main menu
    def drawWindow(self):
        self.lblSelectTapeTitle = Label(
            root,
            text = "Select Machine Tape",
            font = self.title_font,
            bg = "white")
        self.lblSelectTapeTitle.pack()
        self.lblSelectTapeTitle.place(x = 90, y = 200)

        self.selected_machine = StringVar()
        self.selected_machine.set(self.turing_machine_options[0])
        self.optTuringMachine = OptionMenu(
            root,
            self.selected_machine,
            *self.turing_machine_options,
            command = self.selection)
        self.optTuringMachine.pack()
        self.optTuringMachine.config(
            bg = "white",
            fg = "black",
            font = self.title_font,
            width = 30,
            borderwidth = 1,
            relief = "solid",
            justify = LEFT)
        self.optTuringMachine["menu"].config(
            bg = "white",
            fg = "black",
            font = self.dropdown_font,
            borderwidth = 1,
            relief = "solid")
        self.optTuringMachine.place(x = 150, y = 10)

        self.btnSelectedMachine = Button(
            root,
            text = "Submit Machine Tape",
            bg = "green4",
            fg = "white",
            font = self.title_font,
            height = 1,
            width = 32,
            borderwidth = 1,
            relief = "solid",
            command = self.submit)
        self.btnSelectedMachine.pack()
        self.btnSelectedMachine.place(x = 510, y = 10)

        self.btnDynamicMachine = Button(
            root,
            text = "Run the Dynamic Turing Machine",
            bg = "green4",
            fg = "white",
            font = self.title_font,
            height = 1,
            width = 65,
            borderwidth = 1,
            relief = "solid",
            command = self.runDynamicMachine)
        self.btnDynamicMachine.pack()
        self.btnDynamicMachine.place(x = 150, y = 60)

        self.imgStates = Canvas(root, highlightthickness = 0, background = 'white')
        self.imgStates.config(width = 1000, height = 800)
        self.photoState = PhotoImage(file = "TM_multiply_unary_State_Diagram.gif")
        self.imgStates.create_image(0,0, image = self.photoState, anchor="nw")
        self.imgStates.place(x = 50, y = 100)

    #  this handles changing the image for each of the machines selected
    def selection(self, item):
        # this is called when an item is selected and passes in the key for the dictionary to set the image
        self.photoState = PhotoImage(file = self.machine_state_diagrams[item])
        self.imgStates.create_image(0,0, image = self.photoState, anchor="nw")
        self.imgStates.place(x = 50, y = 100)
        root.update()
        self.machine_selection = item
    
    # runs the dynamic turing machine python file
    def runDynamicMachine(self):
        os.system("TM_dynamic.py")

    def submit(self):
        os.system(self.machines[self.machine_selection])

if __name__ == "__main__":
    root = Tk()
    app = MainMenu(root)
    root.configure(background = 'white')
    root.geometry("1050x700+250+250")
    root.title("Select a Turing Machine")
    root.mainloop()
        
