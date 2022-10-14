#!/bin/bash
ext1=".py"
ext2=".md"
ext3=".pdf"
scriptfile=$1$ext1
mdcopy=$1$ext2
pdfout=$1$ext3
cp $scriptfile temp.md
sed -i '1,2d' temp.md
sed -i -e 's/#~~ //g' temp.md
perl -ne 's/^!\[\[(.+?)\]\].*/`cat $1`/e;print' temp.md > $mdcopy
pandoc -s -o $pdfout $mdcopy
rm temp.md
rm $mdcopy
