# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 15:21:28 2019

@author: ashis.prasad
"""

from CommonFunctions import *
from ParameterFilesandValue import *

import sys


if __name__ == '__main__':
    print("Calling Function GenerateDeNormalizedDF() to Denormalize the data")
    try:
        InputDataFrame=GenerateDeNormalizedDF()
        
        print("Calling Function GenerateTopTippingZone(InputDataFrame) to generate top_tipping_zones.csv")
        GenerateTopTippingZone(InputDataFrame)
        print("Calling Function GenerateLongestTripperDay(InputDataFrame) to generate longest_trips_per_day.csv")
        GenerateLongestTripperDay(InputDataFrame)
        del(InputDataFrame)
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
