from tkinter import *
# import tkinter as tk
from tkinter.ttk import *
import tkinter.font as tkFont
from timeAnalysis import *
from hourlyAnalysis import *
from accidentByKeyword import getAccidentByKeyword
from alcoholImpact import *
from geographicImpact import *
from csvReader import *
from PIL import Image, ImageTk


root = Tk()
root.title("VAA Tool")
root.geometry("1000x1000")
root.configure(bg="white")

arial12 = tkFont.Font(family="Arial", size=12, weight="bold")
arial14 = tkFont.Font(family="Arial", size=14, weight="bold")
arial16 = tkFont.Font(family="Arial", size=16, weight="bold")


title = Label(root, text="Victoria Accident Analysis Tool", font=arial16, fg="blue", bg="white",)
title.grid(row=0, column=2, padx=450, pady=20)

fileName = "CrashStatisticsVictoria.csv"
db = loadData(fileName)


def showTimeAnalysis():
    print("Opening Time window")
    fromWindow = getTimeAnalysis(db)
    fromWindow.lift()


def showHourlyAnalysis():
    print("Opening Hourly window")
    fromWindow = getHourlyAnalysis(db)
    fromWindow.lift()


def showAccidentByKeyword():
    print("Opening Accident By Keyword window")
    fromWindow = getAccidentByKeyword(db)
    fromWindow.lift()


def showAlcoholImpact():
    print("Opening Alcohol window")
    fromWindow = getAlcoholImpact(db)
    fromWindow.lift()


def showGeographicImpact():
    print("Opening Geographic window")
    getGeographicImpact(db)


timeButton = Button(root, text="Time Analysis", command=showTimeAnalysis, width=30, font=arial14, bg="lightgrey",)
hourlyButton = Button(root, text="Hourly Accident Analysis", command=showHourlyAnalysis, width=30, font=arial14, bg="lightgrey",)
keywordButton = Button(root, text="Accident by Keyword Analysis", command=showAccidentByKeyword, width=30, font=arial14, bg="lightgrey",)
accidentButton = Button(root, text="Alcohol Impact Analysis", command=showAlcoholImpact, width=30, font=arial14, bg="lightgrey",)
geographicButton = Button(root, text="Geographic Impact Analysis", command=showGeographicImpact, width=30, font=arial14, bg="lightgrey",)

timeButton.grid(row=7, column=0,padx=5, pady=5)
hourlyButton.grid(row=8, column=0, padx=5, pady=5)
keywordButton.grid(row=9, column=0, padx=5, pady=5)
accidentButton.grid(row=10, column=0, padx=5, pady=5)
geographicButton.grid(row=11, column=0, padx=5, pady=5)

VAALogo = ImageTk.PhotoImage(Image.open('logo.PNG'))
logo_label = Label(root, image=VAALogo)
# logo_label.pack()


root.mainloop()
