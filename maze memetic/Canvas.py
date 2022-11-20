from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import time
from PIL import Image, ImageTk, ImageSequence
import PIL.ImageGrab as ImageGrab
import customtkinter
from pathlib import Path
import MainProgram as Program

class Paint_lite():
    
    def __init__(self, windowScreen):
        self.windowScreen = windowScreen
        self.windowScreen.title("Maze Generator")   
        # Window Settings     
        height = 900
        width = 1200
        x = (windowScreen.winfo_screenwidth()//2)-(width//2)
        y = (windowScreen.winfo_screenheight()//2)-(height//2)
        self.windowScreen.geometry('{}x{}+{}+{}'.format(width, height, x, y))  
        


# Making Widget for the app

        # Title
        self.canvasTitle = Label(self.windowScreen, text='Canvas Window', font=("System", 46), bg="#edede9", fg="#22333b")
        self.canvasTitle.place(relx=.5, rely=.07, anchor=CENTER)
        # Colors
        self.brushColor = "black"
        self.eraserColor = "white"
        #  scale Frame pixel
        self.brushSize = Scale(from_=15, to=15)
        self.brushSize.set(1)
        # Brush Button
        self.brushButton = customtkinter.CTkButton(master = windowScreen, text="Brush",text_font=("Britannic Bold", 12),command=self.Brush, corner_radius=30, text_color="#edede9", fg_color="#22333b", bg_color="#edede9")
        self.brushButton.place(relx=.2, rely=.16, anchor=CENTER)
        # Eraser Button
        self.eraserButton = customtkinter.CTkButton(master = windowScreen, text="Eraser",text_font=("Britannic Bold", 12),command=self.Eraser, corner_radius=30, text_color="#edede9", fg_color="#22333b", bg_color="#edede9")
        self.eraserButton.place(relx=.35, rely=.16, anchor=CENTER)
        #  Clear Button
        self.clearButton = customtkinter.CTkButton(master = windowScreen, text="Clear",text_font=("Britannic Bold", 12), command=lambda: self.canvasWindow.delete("all"), corner_radius=30, text_color="#edede9", fg_color="#22333b", bg_color="#edede9")
        self.clearButton.place(relx=.5, rely=.16, anchor=CENTER)
        # Save Button
        self.saveButton = customtkinter.CTkButton(master = windowScreen, text="Save",text_font=("Britannic Bold", 12), command=self.SaveFunction, corner_radius=30, text_color="#edede9", fg_color="#22333b", bg_color="#edede9")
        self.saveButton.place(relx=.65, rely=.16, anchor=CENTER)
        # Exit Button
        self.saveButton = customtkinter.CTkButton(master = windowScreen, text="Exit",text_font=("Britannic Bold", 12), command=self.exitFunction, corner_radius=30, text_color="#edede9", fg_color="#22333b", bg_color="#edede9")
        self.saveButton.place(relx=.8, rely=.16, anchor=CENTER)
        # Continue Button
        self.continueButton = customtkinter.CTkButton(master = windowScreen, text="Continue",text_font=("Britannic Bold", 12), command=self.continueFunction, corner_radius=30, text_color="#edede9", fg_color="#22333b", bg_color="black")
        self.continueButton.place(relx=.8, rely=.93, anchor=CENTER)
        # Canvas Frame
        self.canvasWindow = Canvas(self.windowScreen, bg='white', bd=5, height=600, width=600, highlightbackground="#22333b", highlightthickness=5)
        self.canvasWindow.place(relx=.5, rely=.55, anchor=CENTER)
        # Binding mouse with application
        self.canvasWindow.bind("<B1-Motion>", self.Paint)

    # Paint Function
    def Paint(self, event):
        x1, y1 = (event.x-2), (event.y-2)
        x2, y2 = (event.x+2), (event.y+2)
        self.canvasWindow.create_oval(x1, y1, x2, y2, fill=self.brushColor, outline=self.brushColor, width=self.brushSize.get())

    # Color Function
    def SelectColor(self, col):
        self.brushColor = col

    # Brush Function
    def Brush(self):
        colors = ["#000000"]
        for color in colors:
            col = color 
            self.SelectColor(col)

    # Eraser Function
    def Eraser(self):
        self.brushColor = self.eraserColor

    # Save Function
    def SaveFunction(self):
        try:
            # Default save the file as png
            fileName = filedialog.asksaveasfilename(defaultextension='.png')
            x = self.windowScreen.winfo_rootx() + self.canvasWindow.winfo_x()
            y = self.windowScreen.winfo_rooty() + self.canvasWindow.winfo_y()
            x1 = x + self.canvasWindow.winfo_width()
            y1 = y + self.canvasWindow.winfo_height()
            ImageGrab.grab().crop((x+5, y+5, x1-5, y1-5)).save(fileName)
            # Display message after successfuly saving
            messagebox.showinfo("Paint", "Image is saved as " + str(fileName))
        except:
            # Display error message after failed saving
            messagebox.showerror("Paint", "Something went wrong. Unable to save the image.")

    # Saving for the best maze
    def saveBest(self):
        imageFolder = Path().resolve()
        bestLocation = imageFolder / "Saved Images/Best Maze.png"
        best = Image.open(bestLocation)
        try:
            fileName = filedialog.asksaveasfilename(defaultextension='.png')
            best.save(fileName)
            messagebox.showinfo("Paint", "Image is saved as " + str(fileName))
        except:
            messagebox.showerror("Paint", "Something went wrong. Unable to save the image.")

    # Exit Function
    def exitFunction(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit")
        if op > 0:
            self.windowScreen.destroy()
        else:
            return

    # New window for showing the maze process
    def newWindow(self, numGen):
        imageFolder = Path().resolve()
        imageLocation = imageFolder / "Saved Sketches/sketch.png"
        pixelLocation = imageFolder/ "Saved Images/pixelized.png"
        gifLocation = imageFolder / "Saved Images/All Mazes.gif"
        bestLocation = imageFolder / "Saved Images/Best Maze.png"
        
        newWindow = Toplevel(self.windowScreen)
        newWindow.title("Maze Generator")
        newWindow.geometry("1200x900")
        newWindow.configure(bg='black')

        trigger = False
        while trigger != True:
            sketchLabel = Label(newWindow, text='Sketch:', font=("System", 20), bg="black", fg="white")
            sketchLabel.place(relx = .2, rely = .05, anchor=CENTER)
            #Display Sketch
            sketch = Image.open(imageLocation)
            sketchPosition = Label(newWindow, relief="raised")
            sketchPosition.place(relx = .3, rely = .25, anchor=CENTER)
            sketch = sketch.resize((300,300))
            sketch = ImageTk.PhotoImage(sketch)
            sketchPosition.config(image = sketch)
            newWindow.update()

            pixelLabel = Label(newWindow, text='Pixelized Sketch:', font=("System", 20), bg="black", fg="white")
            pixelLabel.place(relx = .71, rely = .05, anchor=CENTER)
            #Display Pixel
            pixel = Image.open(pixelLocation)
            pixelPosition = Label(newWindow, relief="raised")
            pixelPosition.place(relx = .71, rely = .25, anchor=CENTER)
            pixel = pixel.resize((300,300))
            pixel = ImageTk.PhotoImage(pixel)
            pixelPosition.config(image = pixel)
            newWindow.update()

            bestLabel = Label(newWindow, text='Best Generated Maze:', font=("System", 20), bg="black", fg="white")
            bestLabel.place(relx = .71, rely = .5, anchor=CENTER)
            #Display Best Maze
            best = Image.open(bestLocation)
            bestPosition = Label(newWindow, relief="raised")
            bestPosition.place(relx = .71, rely = .7, anchor=CENTER)
            best = best.resize((300,300))
            best = ImageTk.PhotoImage(best)
            bestPosition.config(image = best)
            newWindow.update()

            #Save Button for Best
            self.saveButton = customtkinter.CTkButton(master = newWindow, text="Save",text_font=("System", 12), command=self.saveBest, text_color="black", fg_color="white", hover_color = "grey")
            self.saveButton.place(relx = .9, rely = .93, anchor = CENTER)
            newWindow.update()

            gifLabel = Label(newWindow, text='All Generated {} Mazes: '.format(numGen), font=("System", 20), bg="black", fg="white")
            gifLabel.place(relx = .3, rely = .5, anchor=CENTER)
            #Display Gif
            gif = Image.open(gifLocation)
            gifPosition = Label(newWindow, relief="raised")
            gifPosition.place(relx = .3, rely = .7, anchor=CENTER)
            for gif in ImageSequence.Iterator(gif):
                gif = gif.resize((300,300))
                gif = ImageTk.PhotoImage(gif)
                gifPosition.config(image = gif)
                newWindow.update()
                time.sleep(0.3)
            newWindow.after(100)
    # Continue Function
    def continueFunction(self):

        imageFolder = Path().resolve()
        imageLocation = imageFolder / "Saved Sketches/sketch.png"
        x = self.windowScreen.winfo_rootx() + self.canvasWindow.winfo_x()
        y = self.windowScreen.winfo_rooty() + self.canvasWindow.winfo_y()
        x1 = x + self.canvasWindow.winfo_width()
        y1 = y + self.canvasWindow.winfo_height()
        fileName = ImageGrab.grab().crop((x+5, y+5, x1-5, y1-5))
        fileName.save(imageLocation) #save the sketch after clicking continue

        # Call for the maze generator program    
        numGen = Program.start()
        # Open the new window that displays results
        self.newWindow(numGen)

if __name__ == "__main__":
    windowScreen = Tk()
    P = Paint_lite(windowScreen)
    windowScreen.mainloop()