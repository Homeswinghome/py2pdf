# py2pdf
Export a pdf report from a python script

rev2(20 Mar 2023) : some improvements to work with Black autoformatter

# Which problem does this solve?

To have the possibility to make a report linked to a python script is an interesting function. It allows to keep notes about the script (why, how), to show and share the results. A good location of the report is inside the script itself. A pdf file as documentation has in addition a confortable readability. Tools like [Pweave](https://mpastell.com/pweave/) offer this functionalities, but my knowledge is inadequate to solve the problems that may occur... or occurred like the last time I updated my Manjaro laptop...

So I came to this solution, probably with a lower performance but that uses standard tools, explicit and simple steps.

More details in the python file or the pdf file

# How it works?

## The features

The expected features are :

* To export a pdf file that includes :
    * The python code cut in chunks
    * All the needed text to explain the goal and outputs of the script
    * Math and formulas
    * The outputs of the script, to the console or graphs (matplotlib)
* The script shall remain directly executable with no modifications
* The only maintained file is the script

## The proposed solution

The script shall include :

* Some codes to store the outputs
* Lines of markdown starting by a mark
* Some lines to include external text files

The mark is a unique sequence of characters starting by "#" (comment in python)

Then the script is preprocessed to :

* remove the first lines (python3 and coding specification)
* remove the mark
* insert the external files
* store the result into an intermediate markdown file

The markdown file is then transformed in pdf with pandoc

