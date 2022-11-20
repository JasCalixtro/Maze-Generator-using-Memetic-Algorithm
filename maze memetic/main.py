from tkinter import*
from PIL import ImageTk
from pathlib import Path
import customtkinter
import Canvas as canvas

# Creation of the Application Window
windowScreen = customtkinter.CTk()
windowScreen.title("Maze Generator")
height = 900
width = 1200
x = (windowScreen.winfo_screenwidth()//2)-(width//2)
y = (windowScreen.winfo_screenheight()//2)-(height//2)
windowScreen.geometry('{}x{}+{}+{}'.format(width, height, x, y))
imageFolder = Path().resolve()
imageLocation = imageFolder /"icon.ico"
windowScreen.iconbitmap(imageLocation)
img = ImageTk.PhotoImage(file="background.png")

# Buttons and function on calling the next screen
def MainScreen():
    
    # Load the Canvas Window Screen
    def NextScreen():

        appTitle.destroy()
        startButton.destroy()
        exitButton.destroy()

        x = canvas.Paint_lite(windowScreen)
        x.__init__(windowScreen)
    # Background of the app
    backgroundImage = Label(windowScreen, image=img)
    backgroundImage.place(x=0, y=0, relwidth=1, relheight=1)
    # Title of the app
    appTitle = Label(windowScreen, text='Memetic Algorithm \nFor \nMaze Generator', font=("System", 46), bg="#edede9", fg="#22333b")
    appTitle.pack(pady = 45)
    # Start Button
    startButton = customtkinter.CTkButton(master = windowScreen, text="START", text_font=("Britannic Bold", 14), width=150, height=40, command= NextScreen, corner_radius=30, text_color="#edede9", fg_color="#22333b", bg_color="#edede9")
    startButton.pack(pady = 15)
    # Exit Button
    exitButton = customtkinter.CTkButton(master = windowScreen, text="EXIT", text_font=("Britannic Bold", 14), width=150, height=40, command= windowScreen.quit, corner_radius=30, text_color="#edede9", fg_color="#22333b", bg_color="#edede9")
    exitButton.pack(pady = 5)
# Call the function MainScreen to display buttons and labels
MainScreen()
windowScreen.mainloop()