from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkFont
import wx
from accidentPerPeriod import *
# from listAccidentsPerHourInPeriod import *
# # from searchAccidentByDcaCode import *
#
from accidentByKeyword import getSearchAccidentsFrame
# from showImpactOfAlcohol import *
from csvReader import *
# from listAccidentsInRegion import *


window = Tk()
window.title("Victoria State Accident Analysis program")
window.geometry("800x800")
window.configure(bg="white")

png = wx.Image('logo.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
wx.StaticBitmap(-1, png, (10,5), (png.GetWidth(), png.GetHeight()))

helv12 = tkFont.Font(family="Helvetica", size=12, weight="bold")
helv14 = tkFont.Font(family="Helvetica", size=14, weight="bold")
helv16 = tkFont.Font(family="Helvetica", size=16, weight="bold")

lbltitle = Label(
    window,
    text="Victoria State Accident Analysis program",
    pady=20,
    font=helv14,
    fg="blue",
    bg="white",
)
lbltitle.grid(row=0, column=0)

fileName = "CrashStatisticsVictoria.csv"
db = loadData(fileName)


def showAccidentsInPeriod():
    print("Opening window")
    fr = getAccidentsFrame(db)
    fr.lift()

#
# def showAccidentsPerHourInPeriod():
#     print("Opening window")
#     fr = getAccidentsInHourFrame(db)
#     fr.lift()
#
#
# def searchAccidentsByKeyword():
#     print("Opening window")
#     fr = getSearchAccidentsFrame(db)
#     fr.lift()
#
#
# def showImpactOfAlcohol():
#     print("Opening window")
#     fr = getImpactOfAlcoholChartFrame(db)
#     fr.lift()
#
#
# def listAccidentsInRegion():
#     print("Opening window")
#     listAccidentsInRegionFrame(db)
#

b1 = Button(
    window,
    text="List accidents in period",
    command=showAccidentsInPeriod,
    width=40,
    font=helv12,
    bg="lightgrey",
)
# b2 = Button(
#     window,
#     text="Histogram of accident per hour in period",
#     command=showAccidentsPerHourInPeriod,
#     width=40,
#     font=helv12,
#     bg="lightgrey",
# )
# b3 = Button(
#     window,
#     text="Search accidents in period by DCA_CODE",
#     command=searchAccidentsByKeyword,
#     width=40,
#     font=helv12,
#     bg="lightgrey",
# )
# b4 = Button(
#     window,
#     text="Show impact of Alcohol in relation to traffic lights",
#     command=showImpactOfAlcohol,
#     width=40,
#     font=helv12,
#     bg="lightgrey",
# )
#
# b5 = Button(
#     window,
#     text="Additional analysis",
#     command=listAccidentsInRegion,
#     width=40,
#     font=helv12,
#     bg="lightgrey",
# )
#
b1.grid(row=5, column=0, padx=5, pady=5)
# b2.grid(row=6, column=0, padx=5, pady=5)
# b3.grid(row=7, column=0, padx=5, pady=5)
# b4.grid(row=8, column=0, padx=5, pady=5)
# b5.grid(row=9, column=0, padx=5, pady=5)


#frame = Frame()
#frame.grid(row=0, column=4)
#frame.place(relwidth=1, relheight=1, y=200)
#frame.config()


#lbl = Label(
#    frame, text="Please select on of the menu above to start.", pady=20, font=helv16
#)
#lbl.pack(in_=frame)

window.mainloop()
