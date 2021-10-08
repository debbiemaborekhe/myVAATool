from tkinter import *
from showDataTable import *
from tkcalendar import Calendar, DateEntry


def getTimeAnalysis(db):
    def showResult():
        startDateValue = startDate.get_date()
        endDateValue = endDate.get_date()
        query = (
            'ACCIDENT_DATE>="'
            + str(startDateValue)
            + '" and ACCIDENT_DATE<"'
            + str(endDateValue)
            + '"'
        )

        resultdb = db.query(query)
        if resultdb.empty:
            lblError.config(
                text="No data exists for the selected date. Try selecting another date"
            )
        else:
            lblError.config(text="")

        dbframe = showOnScreen(root, resultdb, "Some title")
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

    # dbframe.config()
    # dbframe.grid(row=6, column=0)
    # root.place(width=400, height=400, y=140)

    return root
