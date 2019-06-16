
#!/bin/sh

export parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

. $parent_path/Parameter.prm

echo "Executing script to create the output files for assignment. If you are unsure about the assignment, please go through with assissignment.md file"
echo "---------------------------------------------------------------------------------------------------------"


echo "Checking if python is install or not"
echo "---------------------------------------------------------------------------------------------------------"

CheckPythonVersion=`which python`

if [ $CheckPythonVersion == "" ]
then
        echo "Python is not installed in this machine, hence quitting the script"
        echo "---------------------------------------------------------------------------------------------------------"
        echo "exit 3"
        exit 3
fi


echo "Installing the required dependencies"
echo "---------------------------------------------------------------------------------------------------------"

pip install -r $parent_path/Requirement.txt -t $Code_dir

if [ -d $Input_Dir ]
then
    echo "$Input_Dir exists"
else
    echo "$Input_Dir Does not exists"
    mkdir $Input_Dir
fi


if [ -d $Ref_Dir ]
then
    echo "$Ref_Dir exists"
else
    echo "$Ref_Dir Does not exists"
    mkdir $Ref_Dir
fi

if [ -d $Output_dir ]
then
    echo "$Output_dir exists"
    echo "Removing any File from this directory"
    rm $Output_dir/*
else
    echo "$Output_dir Does not exists"
    mkdir $Output_dir
fi

if [ -d $Code_dir ]
then
    echo "$Code_dir exists"
else
    echo "$Code_dir Does not exists"
    mkdir $Code_dir
fi



echo "checking the input file is present or not, if not present than file will be using the link present  in parameter file"
echo "---------------------------------------------------------------------------------------------------------"

if [ -f $Input_Dir/$Input_file_name ]
then
	echo "Input File exists"
else
	echo "Input File Does not Exists!!! Downloading the file from portal"
	wget -P $Input_Dir $Input_File_Download_Link
	if [ $? != 0 ]
	then
		echo "Error Occured While Downloading the file"
		echo "Quitting the Script with exit 1"
		echo "exit 1"
	else
		echo "Input File Downloaded Successfully"
		echo "---------------------------------------------------------------------------------------------------------"

	fi
fi	
	
if [ -f $Ref_Dir/$Ref_file_name ]
then
	echo "Input File exists"
else
	echo "Input File Does not Exists!!! Downloading the file from portal"
	wget -P $Ref_Dir $Ref_File_Download_Link
	if [ $? != 0 ]
	then
		echo "Error Occured While Downloading the file"
		echo "Quitting the Script with exit 1"
		echo "exit 2"
		exit 2
	else
		echo "Reference File Downloaded Successfully"
		echo "---------------------------------------------------------------------------------------------------------"

	fi
	
fi


echo "Executing the command to process the input file to create 2 output files as per requirement"
echo "---------------------------------------------------------------------------------------------------------"

python $Code_dir/MainFunction.py

if [ $? != 0 ]
then
	echo "Script Failed to execute.Please check the logs to find the error"
	echo "---------------------------------------------------------------------------------------------------------"
	echo "exit 4"
	exit 4
else
	echo "Script Successfull Executed. Please Checked $Output_dir to get required result"
	echo "---------------------------------------------------------------------------------------------------------"
fi

echo "Initiating Clean up process Directories"
echo "---------------------------------------------------------------------------------------------------------"

echo "Removing Input file"
rm $Input_Dir/*

echo "Removing Dependency Files from Code Directory"
cd $Code_Dir
rm -rf !(CommonFunctions.py|MainFunction.py|ParameterFilesandValue.py)



