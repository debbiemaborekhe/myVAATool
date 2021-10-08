import sys

import pandas as pd


def loadData(fileName):
    try:
        CrashFile = pd.read_csv(fileName)

        CrashFile["ACCIDENT_DATE"] = pd.to_datetime(CrashFile["ACCIDENT_DATE"])
        return CrashFile
    except FileNotFoundError:
        # return Empty Dataframe...
        return pd.DataFrame({"A": []})


def validateData(CrashFile):
    if CrashFile.empty:
        print("The file is empty")
        sys.exit()


def clearData(treeView):
    treeView.delete(*treeView.get_children())
    return None
