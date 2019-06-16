
# Data Engineer Test@dh-logistic-data Dated-2019-06-19

I. Pre-Requistes
------------
1. Code requires minimum 4-8 GB of RAM for execution. If you are running on make sure you are running over 8 GB RAM for smooth execution of the process. If you are running on AWS make sure you run it m4.large or above.

2. The code has been built on python, so it assumes that the machine on which we are running the code must have python. Code has Error Handling present which will exit the sript, if it does not find python on the machine.

II. Design
----------
A. Program design

The program has been designed with just 3 steps process. Below the steps mentioned

#1. Download the project from GIT reposistory
Install git if not present. if git is present on the machine then run below mentioned command
			
	git clone https://github.com/ashisprasad06/dh-logistics-data-engineer-assignment.git
			   
#Overview of the downloaded files
#Assignment.md    --> Detail Problem Statement is mentioned in the file. This file stores the link and expected output.

#RunAssignment.sh --> Bash Script to create the solution of the requirement. This is the main script which will be triggered to generated the expected output. The script is bash script which containts the step execution, first checking Pre-Requistes, setting up the dependencies, run the python script which will generated the output files and finally clearing not required files.

#Reference        --> Directory which contains Reference File. The reference file contains the mapping of the Zones with its locationId, this is required to for matching the expected output as hinted in Assingment.md
	
#Parameter.prm    --> This the parameter file which help you to manage the code with minimal changes. this contains all parameters which are required to run the process like, if we decided to change the location of input file name or file name download link, then we can change in this file and code will be automatically directed to required folders
	
#Code 			 --> Directory which contains codes. There are 3 .py files. 1st is ParametersandValuefiles.py this contains the global paramters which are in other .py files. This file takes data from environment variables present in Parameter.prm. Then we have CommonFunctions.py, in this .py file we have 4 functions which are required to perform ETL on input data to attend the expected input. Finally we have MainFunction.py, this file calls CommonFunctions.py functions in a sequence in order to generated the required output.

#Requirement.txt  --> This file stores the list of packages which needs to be installed before 


#2. Execute the process to get expected output

	sh -x ./ashisprasadDataEngineer-dh-logistics-data/RunAssignment.sh

#3. Verify the file in Output Directory

	cat ./ashisprasadDataEngineer-dh-logistics-data/*

