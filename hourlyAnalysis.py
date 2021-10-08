from tkinter import *
from showDataTable import *
from tkcalendar import Calendar, DateEntry
import matplotlib.pyplot as plt
from numpy import arange, sin, pi
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import wx
import sys
import sqlite3




def getHourlyAnalysis(db):
    def showResult():
        #from here
        #=startDateValue = startDate.get_date()
        #endDateValue = endDate.get_date()
        #query = (
        #    'ACCIDENT_DATE>="'
        #    + str(startDateValue)
        #    + '" and ACCIDENT_DATE<"'
        #    + str(endDateValue)
        #    + '"'
        #)

        #db2 = db.query(query)
        #if db2.empty:
        #    lblError.config(
        #        text="No data exists for the selected date. Try selecting another date"
        #    )
        #else:
        #    lblError.config(text="")

        #db2["ACCIDENT_TIME"] = db2["ACCIDENT_TIME"].apply(
        #    lambda s: int(s.split(".")[0])
        #)
        #db4 = db2[["ACCIDENT_DATE", "ACCIDENT_TIME"]]
        #db6 = (
        #    db4.groupby(["ACCIDENT_DATE", "ACCIDENT_TIME"])["ACCIDENT_TIME"]
        #    .count()
        #    .reset_index(name="COUNT")
        #)
        #db7 = db6.groupby(["ACCIDENT_TIME"])[["ACCIDENT_TIME", "COUNT"]].mean()
        #if db7.empty:
        #    lblError.config(text="Sorry, No Results found for Selected Dates")
        #else:
        #    lblError.config(text="")
        #    db7.plot(x="ACCIDENT_TIME", y="COUNT", kind="hist", color="green")
        #    plt.title("subplot 1")
        #    plt.xlabel("Hour of a day")
        #    plt.ylabel("Number of accidents happened")
        #    plt.suptitle("Number of accidents happened per hour chart")
        #    plt.show()
        #

        #plt.figure(figsize=(8, 5))
        #plt.xlabel('Hours')
        #plt.xticks(range(1,24))
        #plt.ylabel('Number of accidents')
        #plt.title('Hourly Analysis of Accidents')

        #plt.show()

        #def hour_analysis()

        connection = sqlite3.connect("crashdb.db")
        cursor = connection.cursor()
        string =  "SELECT cast(ACCIDENT_TIME as int) AS 'HOUR',COUNT(*) AS 'COUNT' FROM CrashStatisticsVictoria GROUP BY HOUR"
        # string="SELECT sum(cast(price as INT)) from listings_dec18 "
        # query=string.format(first=var1,second=var2)
        cursor.execute(string)
        result = cursor.fetchall()
        list1 = []
        list2 = []
        for r in result:
            list1.append(r[0])
            list2.append(r[1])
        connection.close()

        class CanvasPanel(wx.Panel):
            def __init__(self, parent):
                wx.Panel.__init__(self, parent)
                self.figure = Figure()
                self.axes = self.figure.add_subplot(111)
                self.canvas = FigureCanvas(self, -1, self.figure)
                self.sizer = wx.BoxSizer(wx.VERTICAL)
                self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
                self.SetSizer(self.sizer)
                self.Fit()

            def draw(self):
                # plot_ditribution()

                plt.figure(figsize=(8, 5))
                plt.xlabel('Hours')
                plt.xticks(range(1, 25))
                #plt.yticks(range(1, 5000))
                plt.ylabel('Number of accidents')
                plt.title('Hourly Analysis of Accidents')
                plt.plot(list1, list2)
                plt.show()

        # if __name__ == "__main__":
        app = wx.PySimpleApp()
        fr = wx.Frame(None, title='test')
        panel = CanvasPanel(fr)
        panel.draw()
        fr.Show()
        app.MainLoop()

        return dbframe

    root = Frame()
    root.grid(row=3, column=0)
    root.place(relwidth=1, relheight=1, x=460)

    lblError = Label(root, text="", fg="red", pady=5)
    lblError.grid(row=6, column=1, padx=5, pady=5, sticky=E)

    Label(root, text="From date", bg="lightgrey").grid(
        row=4, column=1, padx=5, pady=5, sticky=E
    )
    # Label(root, text="inches", bg="lightgrey").grid(row=4, column=3, sticky=W)
    startDate = DateEntry(root, bd=3)
    startDate.grid(row=4, column=2, padx=5, pady=5)

    Label(root, text="To date", bg="lightgrey").grid(
        row=5, column=1, padx=5, pady=5, sticky=E
    )
    # Label(root, text="lbs", bg="lightgrey").grid(row=5, column=3, sticky=W)
    endDate = DateEntry(root, bd=3)
    endDate.grid(row=5, column=2, padx=5, pady=5)

    btnShowResult = Button(root, text="Show result", command=showResult)
    btnShowResult.grid(row=6, column=2)

    return root
