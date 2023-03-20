#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
# end of Python header, start of markdown py2pdf
# ~~ ---
# ~~ title : Automatic pdf report from a python script with pandoc - revision 2
# ~~ author : ChristianV
# ~~ date : 19 Mar 2023
# ~~ abstract : Export a pdf report (code, outputs) commented with the Markdown embedded in the python script, a bash preprocessing and pandoc. Everything is launched whithin the python script.
# ~~ lang: en-US
# ~~ geometry:
# ~~ - margin = 2cm
# ~~ - a4paper
# ~~ toc: true
# ~~ toc_depth: 2
# ~~ numbersections: true
# ~~ links-as-notes: false
# ~~ linkcolor: blue
# ~~ ---
# ~~
# ~~ **Revision 2** : improvement to work with a script formated with [Black](https://github.com/psf/black) and inspected with [Pylint](https://pylint.org/).
# ~~
# ~~ # Which problem does this solve?
# ~~
# ~~ To have the possibility to make a report linked to a python script is an interesting function. It allows to keep notes about the script (why, how), to show and share the results. A good location of the report is inside the script itself. A pdf file as documentation has in addition a confortable readability. Tools like [Pweave](https://mpastell.com/pweave/) offer this functionalities, but my knowledge is inadequate to solve the problems that may occur... or occurred like the last time I updated my Manjaro laptop...
# ~~
# ~~ So I came to this solution that uses standard Linux tools, explicit and simple steps.
# ~~
# ~~ # How does it work?
# ~~
# ~~ ## The features
# ~~
# ~~ The expected features are :
# ~~
# ~~ * To export a pdf file that includes :
# ~~     * The python code cut in chunks
# ~~     * All the needed text to explain the goal and outputs of the script
# ~~     * Math and formulas
# ~~     * The outputs of the script, to the console or graphs (matplotlib)
# ~~ * The script shall remain directly executable with no modifications
# ~~ * The only maintained file is the script
# ~~
# ~~ ## The proposed solution
# ~~
# ~~ The script shall include :
# ~~
# ~~ * Some codes to store the outputs
# ~~ * Lines of markdown starting by a mark
# ~~ * Some lines to include external text files
# ~~
# ~~ The mark is a unique sequence of characters starting by "#" (comment in python)
# ~~
# ~~ Then the script is preprocessed to :
# ~~
# ~~ * remove the first lines (python3 and coding specification)
# ~~ * remove the mark
# ~~ * insert the external files
# ~~ * store the result into an intermediate markdown file
# ~~
# ~~ The markdown file is then transformed in pdf with pandoc
# ~~
# ~~ ## The sources of inspiration
# ~~
# ~~ The idea of a mark "#%%" comes from pweave, spyder to embedded markdown in the python script.
# ~~
# ~~ The first test shown that with, at least, a French keyboard this sequence is so easy to use (need AltGr then shift) and is visually intrusive in editor. Several "#" are not allowed (used by markdown) so I changed to "# ~~" as "~" is next key on the left of "#".
# ~~
# ~~ **Revision 2 note 1** : the mark was "#~~" in version 1 which doesn't fit whith Python coding rule (a comment mark # is followed by a blank). In rev 2 : the mark is **"# ~~"**.
# ~~
# ~~ **Revision 2 note 2** : a line "# ~~ end of Python header, start of markdown py2pdf" is added to separate the Python information of the first lines from the beginning of the Pandoc header.
# ~~
# ~~ The script filename.py is copied into an image markdown file temp2.md and then temp.md
# ~~
# ~~ The script can remove the first lines and the mark, remove the line after "# ~~ no export to pdf from here". This separator was created in order to have the possibility to limit the length of the pdf file; for example if showing the code or part of it has no interest.
# ~~
# ~~ **Revision 2 note 3** : the compatibility of the bash file with the original mark "#~~" is kept.
# ~~
# ~~ See at the end of the document the bash script.
# ~~
# ~~ A "magic" call to perl can insert external text files. It is proposed by stackoverflow ie  [Embedding one markdown document in another](https://stackoverflow.com/questions/18438907/embedding-one-markdown-document-in-another/18517316#18517316)
# ~~ ```
# ~~ perl -ne 's/^!\[\[(.+?)\]\].*/`cat $1`/e;print' temp.md > filename.md
# ~~ ```
# ~~ All the found \![[textfilepath]] in temp.md will be replaced by the textfilepath file content in result.md
# ~~
# ~~ This method can be applied to subpart of the file like the header to get more compact script or any other text file to share like a bash file.
# ~~
# ~~ Finally the markdown image is exported to pdf with pandoc
# ~~ ```
# ~~ pandoc -s -o filename.pdf filename.md
# ~~ ```
# ~~ The intermediate files temp2.md, filename.md are delated. The temp.md is kept for debug.
# ~~
# ~~ There are probably more interesting options of pandoc to use... This will be another task
# ~~
# ~~ ## What is missing for the magic complete
# ~~
# ~~ ### Code to be added
# ~~
# ~~ Some code lines are added to prepare the structure : a directory is created to store the output files.
# ~~
# ~~ A local print function allows to print in the console and in a logfile. The logfile name is changed when necessary to separate the output. Inspiration for this comes from stackoverflow [print on console and text file simultaneously python](https://stackoverflow.com/questions/26796592/print-on-console-and-text-file-simultaneously-python#26810469)
# ~~
# ~~ Some code is also needed to store the desired matplotlib graphs.
# ~~
# ~~ The command lines are embedded in a bash file called at the end of the script. The bash file can be in the same directory than the python script. For a more productive configuration, the bash file might be located in one directory, an alias added in ".bashrc". The call to script is then :
# ~~ ```python
# ~~ cmd = "py2pdf scriptname"
# ~~ subprocess.call(['/bin/bash', '-i', '-c', cmd])
# ~~ ```
# ~~ "py2pdf" being the alias.
# ~~
# ~~ Then in the ".bashrc" file :
# ~~ ```bash
# ~~ # my scripts
# ~~ p="$HOME/0_myscripts/" # or any other path to your scripts
# ~~ alias py2pdf="$p/py2pdf"
# ~~ ```
# ~~
# ~~ ### Resources
# ~~ * pandoc : [pandoc.org](https://pandoc.org/)
# ~~ * python, bash, perl : standard of Linux distribution?
# ~~ * about sed [Commande sed : utilisation et exemples](https://www.malekal.com/commande-sed-utilisation-et-exemples/). Sorry it is a page in French but it helps me to write more robust sed commands.
# ~~
# ~~ ### Github repository
# ~~
# ~~ The files are under Github [Homeswinghome/py2pdf](https://github.com/Homeswinghome/py2pdf)
# ~~
# ~~ ## Whish list
# ~~
# ~~ * Replace the bash script by python for a better portability (Pandoc is available for Windows)
# ~~ * Manage versions of the export : it happens a report is replaced by a new trial. Oups!
# ~~ * Find a way to have a shortcut in an editor to insert the mark (my current editors : gedit / VScodium)
# ~~
# ~~ ## What does the python script look like ?
# ~~
# ~~ Here are some lines from the raw file "scriptpython2pdf.py" (do not confuse with its export to pdf):
# ~~
# ~~ ```
# ~~ ![[scriptpython2pdf_extract.py]]
# ~~ ```
# ~~
# ~~ # python code
# ~~
# ~~ ## Import modules
# ~~ ```python

# import
import os  # for py2pdf
import subprocess  # for py2pdf with bash with alias
import matplotlib.pyplot as plt  # for the demo
import numpy as np  # for the demo

# ~~ ```
# ~~
# ~~ ## Functions
# ~~
# ~~ This is a demo file. In other applications, for a better readability, those specific functions might be included in a library to import in the above section.
# ~~ ```python


def print_twice(log, *args, **kwargs):
    '''the double print function (to console and to log)'''
    print(*args, **kwargs)
    with open(log, "a") as f:  # appends to file and closes it when finished
        print(file=f, *args, **kwargs)


def outputdir():
    '''create a directory to save outputs'''
    directory = "py2pdf_files"
    if not os.path.exists(directory):
        # print("create directory")
        os.makedirs(directory)
    else:
        pass
        # print("existing directory")


def clearlog(log):
    '''clear logfile'''
    file_to_delete = open(log, "w")
    file_to_delete.close()


# ~~ ```
# ~~ ## Main code
# ~~
# ~~ ### Code section 1
# ~~ ```python
# lines to be included for py2pdf export
# get this script file name without extension
scriptname = os.path.basename(__file__).split(".")[0]  
logfile = "./py2pdf_files/log1.txt"  # define the logfile
outputdir()  # create the directory to store the output
clearlog(logfile)  # clear the logfile (in case script is ran several times)

# code for console output demo
path = os.getcwd()  # get the path of the current directory
print_twice(logfile, "Path of the current directory : " + path)
print_twice(logfile, "python script name : ", scriptname)
print_twice(logfile, "Hello world")
print_twice(logfile, "Logfile : ", logfile)
# ~~ ```
# ~~ ### Code Output (section 1)
# ~~ ```
# ~~ ![[./py2pdf_files/log1.txt]]
# ~~ ```
# ~~ ### Code section 2
# ~~ From matplotlib site  : [Simple plot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py)
# ~~ This simple example plots the signal :
# ~~ $$ s = 1 + sin(2.\pi.t) $$
# ~~ ```python
# code for matplotlib output demo
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(
    xlabel="time (s)", ylabel="voltage (mV)", title="About as simple as it gets, folks"
)
ax.grid()
# this is the key line to store the matplotlib output
fig.savefig("./py2pdf_files/simple_plot.png")  
plt.show()
# ~~ ```
# ~~ ### Code Output (section 2)
# ~~
# ~~ See figure 1
# ~~
# ~~ ![matplotlib output](./py2pdf_files/simple_plot.png){ width=250px }
# ~~
# ~~ ### Code last section
# ~~ ```python
# lines to be included for py2pdf export
# create a second logfile
logfile = "./py2pdf_files/loglast.txt"  # define the logfile
clearlog(logfile)  # clear the logfile (in case script is ran several times)
# prepare the command to launch the report creation
# cmd = "./py2pdf " + scriptname # for a local bash
# cmd = "~/0_scripts/py2pdf " + scriptname # for a bash in directory in home
cmd = "py2pdf " + scriptname  # alias

# code for console output demo
print_twice(logfile, "launch command : ", cmd)  # for demo
print_twice(logfile, "pdf should be available soon")  # for demo
# launch the report creation
# os.system(cmd) # to launch the bash file (local or directory in home)
subprocess.call(["/bin/bash", "-i", "-c", cmd])  # to launch the bash file (alias)
# ~~ ```
# ~~ **/!\\WARNING : no output after this line can be recorded automatically**
# ~~ ```python
print("Hurra the pdf is created!")
# ~~ ```
# ~~ ### Code output (last section)
# ~~ ```
# ~~ ![[./py2pdf_files/loglast.txt]]
# ~~ ```
# ~~ ### Code of the bash file
# ~~
# ~~ py2pdf.sh
# ~~ ```
# ~~ ![[py2pdf.sh]]
# ~~ ```
# ~~ ## Additional output
# ~~
# ~~ Some pictures or snapshots might be added. It is a manual operation to store them.
# ~~
# ~~ ![terminal](./py2pdf_files/terminal.png){ width=400px }
# ~~
    # ~~ ## Test of indented lines
    # ~~
    # ~~ When markdown lines are in a function, the comments are indented.
    # ~~
# ~~ no export to pdf from here
# ~~ This line and what is below won't be in the markdown and then pdf output.
