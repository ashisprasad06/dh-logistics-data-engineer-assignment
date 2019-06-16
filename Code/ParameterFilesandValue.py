# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:50:01 2019

@author: ashis.prasad
"""

# Below are the list of global variables which will used to read the data

from os import environ

global workdirectory
global inputpath
global inputfilename
global referencepath
global referencefilname
global outputpath
global outputfilenames

# Below are the list of values which can be changed as per user configuration
# Incase you are working on Mac or Unix workdirectory parameter will 
# automatically get changed, this has been handled by Bash script

# For InputFileName you can pass the html link or the filename you have downloaded.
# If you are given just the file name make sure you keep the file in inputpath


# For referencefilname you can pass the html link or the filename you have downloaded.
# If you are given just the file name make sure you keep the file in referencepath


inputpath=environ['Input_Dir']+'/'
inputfilename=environ['Input_file_name']
referencepath=environ['Ref_Dir']+'/'
referencefilname=environ['Ref_file_name']
outputpath=environ['Output_dir']+'/'
Output_File_TopTipping_Zone=environ['Output_File_TopTipping_Zone']
Output_File_LongTripPerDay=environ['Output_File_LongTripPerDay']
