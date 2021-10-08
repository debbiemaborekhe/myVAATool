import unittest
from csvReader import *
from timeAnalysis import *
from hourlyAnalysis import *
from searchAccidentByDcaCode import *
from alcoholImpact import *
from geographicImpact import *


class UnitTests(unittest.TestCase):

    existingFileName = "Crash Statistics Victoria.csv"
    nonExistingFileName = "Crash Statistics Victoria Not Exist.csv"

    def testLoadingExistingData(self):
        db = loadData(self.existingFileName)
        self.assertFalse(db.empty)

    def testLoadingNonExistingData(self):
        db = loadData(self.nonExistingFileName)
        self.assertTrue(db.empty)

    def testValidationData(self):
        db = loadData(self.existingFileName)
        result = validateData(db)
        self.assertFalse(db.empty)

    def testFrameDisplayedForSelectedPeriod(self):
        db = loadData(self.existingFileName)
        frame = getAccidentsFrame(db)
        self.assertTrue(frame)

    def testFrameDisplayedForSelectedPeriodInHourOfDay(self):
        db = loadData(self.existingFileName)
        frame = getAccidentsInHourFrame(db)
        self.assertTrue(frame)

    def testFrameDisplayedForSearchByDCACode(self):
        db = loadData(self.existingFileName)
        frame = getSearchAccidentsFrame(db)
        self.assertTrue(frame)

    def testFrameDisplayedForImpactOfAlcohol(self):
        db = loadData(self.existingFileName)
        frame = getImpactOfAlcoholChartFrame(db)
        self.assertTrue(frame)

    def testFrameDisplayedForImpactOfAlcohol(self):
        db = loadData(self.existingFileName)
        frame = listAccidentsInRegionFrame(db)
        self.assertTrue(frame)


if __name__ == "__main__":
    unittest.main()