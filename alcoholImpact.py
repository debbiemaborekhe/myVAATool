from tkinter import *

from matplotlib.figure import Figure

from showDataTable import *
from tkcalendar import Calendar, DateEntry
import matplotlib.pyplot as plt


def getAlcoholImpact(db):
    # def showResult1():
    #     startDateValue = startDate.get_date()
    #     endDateValue = endDate.get_date()
    #     query = (
    #         'ACCIDENT_DATE>="'
    #         + str(startDateValue)
    #         + '" and ACCIDENT_DATE<"'
    #         + str(endDateValue)
    #         + '"'
    #     )
    #
    #     db3 = db.query(query)
    #     if db3.empty:
    #         lblError.config(text="Sorry, No Results found for Selected Dates")
    #     else:
    #         lblError.config(text="")
    #         db3 = db3.query('ALCOHOLTIME=="Yes"')
    #         if db3.empty:
    #             lblError.config(
    #                 text="Sorry, No Results found for Selected Dates with AlcoholTime=Y"
    #             )
    #         else:
    #             lblError.config(text="")
    #             db3["WDNUM"] = db3["ACCIDENT_DATE"].dt.dayofweek
    #             db3["WDNAME"] = db3["ACCIDENT_DATE"].dt.day_name()
    #             db3 = db3[
    #                 [
    #                     "ACCIDENT_DATE",
    #                     "ALCOHOLTIME",
    #                     "LIGHT_CONDITION",
    #                     "ALCOHOL_RELATED",
    #                     "WDNAME",
    #                     "WDNUM",
    #                 ]
    #             ]
    #             main1 = db3
    #             main2 = main1.query('ALCOHOL_RELATED=="Yes"')
    #             if main2.empty:
    #                 lblError.config(
    #                     text="Sorry, No Results found for Selected Dates with AlcoholRelated=Y"
    #                 )
    #             else:
    #                 lblError.config(text="")
    #                 db5 = main2
    #                 db6 = (
    #                     db5.groupby(["ACCIDENT_DATE", "WDNAME", "WDNUM"])["WDNUM"]
    #                     .count()
    #                     .reset_index(name="COUNT")
    #                 )
    #                 db7 = db6.groupby(["WDNAME"])[["WDNAME", "COUNT", "WDNUM"]].mean()
    #                 db7 = db7.reset_index()
    #                 db7 = db7.sort_values(by="WDNUM")
    #                 db7.plot(
    #                     x="WDNAME",
    #                     y="COUNT",
    #                     kind="bar",
    #                     color="green",
    #                     title="Impact of drinking alcohol on accidents",
    #                 )
    #                 plt.show()
    #
    #                 db6 = main2[
    #                     main2["LIGHT_CONDITION"].str.contains("dark", case=False)
    #                 ]
    #                 db7 = db6.groupby("LIGHT_CONDITION")["WDNUM"].count()
    #                 db8 = db7.reset_index(name="COUNT")
    #                 db8.plot(
    #                     kind="pie",
    #                     xlabel="",
    #                     ylabel="",
    #                     title="Impact of drinking Alcohol",
    #                 )
    #                 plt.show()
    #
    #                 db3 = db.query(query)
    #     if db3.empty:
    #         lblError.config(text="Sorry, No Results found for Selected Dates")
    #     else:
    #         lblError.config(text="")
    #         db3 = db3.query('ALCOHOLTIME=="Yes"')
    #         if db3.empty:
    #             lblError.config(
    #                 text="Sorry, No Results found for Selected Dates with AlcoholTime=Y"
    #             )
    #         else:
    #             lblError.config(text="")
    #             db3["WDNUM"] = db3["ACCIDENT_DATE"].dt.dayofweek
    #             db3["WDNAME"] = db3["ACCIDENT_DATE"].dt.day_name()
    #             db3 = db3[
    #                 [
    #                     "ACCIDENT_DATE",
    #                     "ALCOHOLTIME",
    #                     "LIGHT_CONDITION",
    #                     "ALCOHOL_RELATED",
    #                     "WDNAME",
    #                     "WDNUM",
    #                 ]
    #             ]
    #             main1 = db3
    #             main2 = main1.query('ALCOHOL_RELATED=="Yes"')
    #             if main2.empty:
    #                 lblError.config(
    #                     text="Sorry, No Results found for Selected Dates with AlcoholRelated=Y"
    #                 )
    #             else:
    #                 lblError.config(text="")
    #                 db6 = main2[
    #                     main2["LIGHT_CONDITION"].str.contains("dark", case=False)
    #                 ]
    #                 db7 = db6.groupby("LIGHT_CONDITION")["WDNUM"].count()
    #                 db8 = db7.reset_index(name="COUNT")
    #                 # print(db8)
    #                 db8.plot(
    #                     kind="pie",
    #                     # ylabel="label",
    #                     autopct="%1.1f%%",
    #                     y="COUNT",
    #                     labels=db8["LIGHT_CONDITION"],
    #                     title="Traffic light violation accidents",
    #                 )
    #                 plt.axis("equal")
    #                 plt.show()
    #
    #     return dbFrame

    def showResult2():
        startDateValue = startDate.get_date()
        endDateValue = endDate.get_date()
        query = (
            'ACCIDENT_DATE>="'
            + str(startDateValue)
            + '" and ACCIDENT_DATE<"'
            + str(endDateValue)
            + '"'
        )

        db3 = db.query(query)
        if db3.empty:
            lblError.config(text="Sorry, No Results found for Selected Dates")
        else:
            lblError.config(text="")
            db3 = db3.query('ALCOHOLTIME=="Yes"')
            if db3.empty:
                lblError.config(
                    text="Sorry, No Results found for Selected Dates with AlcoholTime=Y"
                )
            else:

                lblError.config(text="")
                db3["WDNUM"] = db3["ACCIDENT_DATE"].dt.dayofweek
                db3["WDNAME"] = db3["ACCIDENT_DATE"].dt.day_name()
                db3 = db3[
                    [
                        "ACCIDENT_DATE",
                        "ALCOHOLTIME",
                        "LIGHT_CONDITION",
                        "ALCOHOL_RELATED",
                        "WDNAME",
                        "WDNUM",
                    ]
                ]
                main1 = db3
                main2 = main1.query('ALCOHOL_RELATED=="Yes"')
                if main2.empty:
                    lblError.config(
                        text="Sorry, No Results found for Selected Dates with AlcoholRelated=Y"
                    )
                else:
                    win = Tk()
                    fig = Figure(figsize=(5, 5), dpi=100)
                    lblError.config(text="")
                    db6 = main2[
                        main2["LIGHT_CONDITION"].str.contains("dark", case=False)
                    ]
                    db7 = db6.groupby("LIGHT_CONDITION")["WDNUM"].count()
                    db8 = db7.reset_index(name="COUNT")
                    # print(db8)
                    a = fig.add_subplot(122)
                    db8.plot(
                        kind="pie",
                        # ylabel="label",
                        autopct="%1.1f%%",
                        y="COUNT",
                        labels=db8["LIGHT_CONDITION"],
                        title="Traffic light violation accidents",
                    )
                    #a.plot(labels=db8["LIGHT_CONDITION"], y, marker="o", label="October")
                    plt.axis("equal")
                    plt.show()


        return None

    root = Frame()
    root.grid(row=3, column=0)
    root.place(relwidth=1, relheight=1, x=460)

    lblError = Label(root, text="", fg="red", pady=5)
    lblError.grid(row=7, column=0, padx=5, pady=5, sticky=E)

    # title = Label(root, text="Victoria Accident Analysis Tool", fg="blue", bg="white", )
    # title.grid(row=0, column=2, padx=250, pady=20)

    Label(root, text="From date", bg="lightgrey").grid(4, column=1, padx=5, pady=5, sticky=E)
    # Label(root, text="inches", bg="lightgrey").grid(row=4, column=3, sticky=W)
    startDate = DateEntry(root, bd=3)
    startDate.grid(row=4, column=2, padx=5, pady=5)

    Label(root, text="To date", bg="lightgrey").grid(row=5, column=1, padx=5, pady=5, sticky=E)
    # Label(root, text="lbs", bg="lightgrey").grid(row=5, column=3, sticky=W)
    endDate = DateEntry(root, bd=3)
    endDate.grid(row=5, column=2, padx=5, pady=5)



    # btnShowResult1 = Button(root, text="Alcohol Impact Analysis - Annual Report", command=showResult1, bg="grey")
    # btnShowResult1.grid(row=6, column=2)

    btnShowResult2 = Button(root, text="Alcohol Impact Analysis - Last 5 years", command=showResult2)
    btnShowResult2.grid(row=6, column=3)

    return root
