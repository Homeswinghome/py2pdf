#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#~~ ---
#~~ title : Automatic pdf report from a python script with pandoc
#~~ author : ChristianV
#~~ date : 14 Oct 2022
#~~ abstract : Export a pdf report (code, outputs) commented with the Markdown embedded in the python script, a bash preprocessing and pandoc. Everything is launched whithin the python script.
#~~ lang: en-US
#~~ geometry:
#~~ - margin = 2cm
#~~ - a4paper
#~~ toc: true
#~~ toc_depth: 2
#~~ numbersections: true
#~~ links-as-notes: false
#~~ linkcolor: blue
#~~ ---
#~~ 
#~~ # Which problem does this solve?
#~~ 
#~~ To have the possibility to make a report
#~~..../
#Some more lines here 
#~~./...
#~~ Some code is also needed to store the desired matplotlib graphs.
#~~ 
#~~ The command lines are embedded in a bash file called at the end of the script. In this example the bash file is in the same directory than the python script. For a more productive configuration, the bash file might be located in one directory, an alias added in ".bashrc". The call to script is then :
#~~ ```
#~~ py2pdf scriptname
#~~ ```
#~~ "py2pdf" being the alias.
#~~ 
#~~ Then in the ".bashrc" file :
#~~ ```bash
#~~ # my scripts
#~~ p="$HOME/0_myscripts/" # or any other path to your scripts
#~~ alias py2pdf="$p/py2pdf"
#~~ ```
#~~ 
#~~ ### Resources
#~~ * pandoc : [pandoc.org](https://pandoc.org/)
#~~ * python, bash, perl : standard of Linux distribution?
#~~ 
#~~ # python code
#~~ 
#~~ ## Import modules
#~~ ```python

# import
import os # for py2pdf
import matplotlib.pyplot as plt # for the demo
import numpy as np # for the demo
#~~ ```
#~~ 
#~~ ## Functions
#~~ 
#~~ This is a demo file. In other applications, for a better readability, those specific functions might be included in a library to import in the above section.
#~~ ```python

def print_twice(log,*args,**kwargs):
    # the double print function (to console and to log)
    print(*args,**kwargs)
    with open(log,"a") as f:  # appends to file and closes it when finished
        print(file=f,*args,**kwargs)
#~~..../
#Some more lines here 
#~~./...
#~~ ```
#~~ ## Main code
#~~ 
#~~ ### Code section 1
#~~ ```python
# lines to be included for py2pdf export
scriptname = os.path.basename(__file__).split('.')[0] # get this script file name without extension
logfile = "./py2pdf_files/log1.txt" # define the logfile
outputdir() # create the directory to store the output
clearlog(logfile) # clear the logfile (in case script is ran several times)

# code for console output demo
path = os.getcwd() # get the path of the current directory
print_twice(logfile, "Path of the current directory : " + path)
print_twice(logfile, "python script name : ",scriptname)
print_twice(logfile, "Directory content :")
print_twice(logfile, "\n".join(os.listdir(path)))
print_twice(logfile, "Logfile : ", logfile)
#~~ ```
#~~ ### Code Output (section 1)
#~~ ```
#~~ ![[./py2pdf_files/log1.txt]]
#~~ ```
#~~..../
#Some more lines here 
#~~./...
# prepare the command to launch the report creation
cmd = "./py2pdf.sh " + scriptname

# code for console output demo
print_twice(logfile, "launch command : ",cmd) # for demo
print_twice(logfile, "pdf should be available soon") # for demo
# launch the report creation
os.system(cmd) # to launch the bash file (copy, preprocessing, pandoc to pdf)
