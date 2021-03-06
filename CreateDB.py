from pathlib import Path
Path('crashDB.db').touch()
import pandas as pd
import sqlite3

def createDBfromCSV(csv_file):
    conn = sqlite3.connect('crashDB.db')
    c = conn.cursor()


    c.execute("DROP TABLE IF EXISTS CrashStatisticsVictoria;")
    c.execute("""CREATE TABLE CrashStatisticsVictoria(OBJECTID	INTEGER PRIMARY KEY,
    ACCIDENT_NO	TEXT,
    ABS_CODE	TEXT,
    ACCIDENT_STATUS	TEXT,
    ACCIDENT_DATE	TEXT,
    ACCIDENT_TIME	TEXT,
    ALCOHOLTIME	TEXT,
    ACCIDENT_TYPE	TEXT,
    DAY_OF_WEEK	TEXT,
    DCA_CODE	TEXT,
    HIT_RUN_FLAG	TEXT,
    LIGHT_CONDITION	TEXT,
    POLICE_ATTEND	TEXT,
    ROAD_GEOMETRY	TEXT,
    SEVERITY	TEXT,
    SPEED_ZONE	TEXT,
    RUN_OFFROAD	TEXT,
    NODE_ID	INTEGER,
    LONGITUDE	REAL,
    LATITUDE	REAL,
    NODE_TYPE	TEXT,
    LGA_NAME	TEXT,
    REGION_NAME	TEXT,
    VICGRID_X	REAL,
    VICGRID_Y	REAL,
    TOTAL_PERSONS	INTEGER,
    INJ_OR_FATAL	INTEGER,
    FATALITY	INTEGER,
    SERIOUSINJURY	INTEGER,
    OTHERINJURY	INTEGER,
    NONINJURED	INTEGER,
    MALES	INTEGER,
    FEMALES	INTEGER,
    BICYCLIST	INTEGER,
    PASSENGER	INTEGER,
    DRIVER	INTEGER,
    PEDESTRIAN	INTEGER,
    PILLION	INTEGER,
    MOTORIST	INTEGER,
    UNKNOWN	INTEGER,
    PED_CYCLIST_5_12	INTEGER,
    PED_CYCLIST_13_18	INTEGER,
    OLD_PEDESTRIAN	INTEGER,
    OLD_DRIVER	INTEGER,
    YOUNG_DRIVER	INTEGER,
    ALCOHOL_RELATED	TEXT,
    UNLICENCSED	INTEGER,
    NO_OF_VEHICLES	INTEGER,
    HEAVYVEHICLE	INTEGER,
    PASSENGERVEHICLE	INTEGER,
    MOTORCYCLE	INTEGER,
    PUBLICVEHICLE	INTEGER,
    DEG_URBAN_NAME	TEXT,
    DEG_URBAN_ALL	TEXT,
    LGA_NAME_ALL	TEXT,
    REGION_NAME_ALL	TEXT,
    SRNS	TEXT,
    SRNS_ALL	TEXT,
    RMA	TEXT,
    RMA_ALL	TEXT,
    DIVIDED	TEXT,
    DIVIDED_ALL	TEXT,
    STAT_DIV_NAME	TEXT
    )""")

    # load the data into a Pandas DataFrame
    users = pd.read_csv(csv_file)
    # write the data to a sqlite table
    users.to_sql('CrashStatisticsVictoria', conn, if_exists='append', index = False)


