from tkinter import *
from showDataTable import *
from tkcalendar import Calendar, DateEntry
import tkinter.font as tkFont
import matplotlib.pyplot as plt


def getGeographicImpact(db):
    def showChart1():
        vcal1 = cal1.get_date()
        vcal2 = cal2.get_date()

        selRegion = options.get()

        if selRegion == "":
            lblError.config(text="Please Select Geographic Location")
            return None
        if vcal1 > vcal2:
            vcal3 = vcal1
            vcal1 = vcal2
            vcal2 = vcal3

        qry = (
            'ACCIDENT_DATE>="' + str(vcal1) + '" and ACCIDENT_DATE<"' + str(vcal2) + '"'
        )
        db2 = db.query(qry)
        if db2.empty:
            lblError.config(text="Sorry, No Results found for Selected Dates")
        else:
            qry2 = 'REGION_NAME=="' + selRegion + '"'
            db2 = db2.query(qry)
            if db2.empty:
                lblError.config(text="Sorry, No Results found for Selected Region")
            else:
                lblError.config(text="")
                db2["WDNUM"] = db2["ACCIDENT_DATE"].dt.dayofweek
                db5 = db2[["ACCIDENT_DATE", "DAY_OF_WEEK", "WDNUM"]]
                db6 = (
                    db5.groupby(["ACCIDENT_DATE", "DAY_OF_WEEK", "WDNUM"])["WDNUM"]
                    .count()
                    .reset_index(name="COUNT")
                )
                db7 = db6.groupby(["DAY_OF_WEEK"])[
                    ["DAY_OF_WEEK", "COUNT", "WDNUM"]
                ].mean()
                db7 = db7.reset_index()
                db7 = db7.sort_values(by="WDNUM")
                db7.plot(x="DAY_OF_WEEK", y="COUNT", kind="bar")
                plt.suptitle("Average Accidents for " + selRegion)
                plt.show()

        return None

    root = Frame()
    root.grid(row=0, column=3)
    root.place(relwidth=1, relheight=1, x=460)

    label2 = Label(root, text="Accidents In A Geographic Location", fg="black", pady=5,)
    label2.grid(row=1, column=0, sticky="N", pady=2)

    lblDateFrom = Label(root, text="From Date: ", fg="black", pady=5)
    lblDateFrom.grid(row=3, column=0, sticky="NW", pady=3)

    lblDateTo = Label(root, text="To Date: ", fg="black", pady=5)
    lblDateTo.grid(row=4, column=0, sticky="NW", pady=3)

    cal1 = DateEntry(root, width=30)
    cal1.grid(row=3, column=1, pady=2)
    cal2 = DateEntry(root, width=30)
    cal2.grid(row=4, column=1, pady=2)

    regions = db["REGION_NAME"].unique()
    options = ttk.Combobox(root, width=40)
    options["values"] = regions.tolist()
    options.current(0)

    lblRegion = Label(root, text="Region: ", pady=5)
    lblRegion.grid(row=5, column=0, pady=2)
    options.grid(row=5, column=1, pady=2)

    btnShow = Button(
        root,
        text="Show Result",
        pady=5,
        bg="gray",
        fg="white",
        command=showChart1,
    )
    btnShow.grid(row=6, column=0, pady=2)

    lblError = Label(root, fg="red", pady=5)
    lblError.grid(row=7, column=0, columnspan=3, pady=3)

    return root