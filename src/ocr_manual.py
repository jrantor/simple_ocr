import tkinter as tk
from tkinter import *
import pytesseract
from PIL import Image, ImageTk

#mainclass

class MainApp(Frame):
    
    def __init__(self):
        super().__init__()
        self.appGUI()
        
    def appGUI(self):
        
        #title of the gui
        self.master.title("Simple Demonstration of OCR Engine")
        self.pack(fill=BOTH,expand=1)
        
        #image path to open and manipulate
        self.newImage = Image.open('path/to/image/img.png')
        self.tkImageObject = ImageTk.PhotoImage(self.newImage)
        tkShow = Label(self, image = self.tkImageObject)

        #canvas to show the image on gui

        canvas = Canvas(self,width=self.newImage.size[0], 
               height=self.newImage.size[1])
        canvas.create_image(10, 10, anchor = NW, image=self.tkImageObject)
        canvas.pack(side = 'left')

        #button to show results

        self.button_result = Button(self, text = "See Results", command = self.textResults)
        self.button_result.pack(side='top', padx=10, pady=10)

        
    def textResults(self):
        #button functionality - the actual work,passing image to the pytesseract function and initiating language
        self.textof = pytesseract.image_to_string(self.newImage, lang = 'eng+ben')

        #canvas no.2 for showing results in text.
        canvas2 = Canvas(self,width = 700, height = 700)
        canvas2.create_text(100,70, anchor = NW, font='calibri',text = self.textof)
        canvas2.pack(side='left')

def main():
    
    root = tk.Tk()
    mai = MainApp()
    root.geometry('1200x600+100+100')
    root.mainloop()

if __name__ == '__main__':
    main()
