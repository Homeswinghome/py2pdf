#!/bin/bash
echo "python to pdf with pandoc"
ext1=".py"
ext2=".md"
ext3=".pdf"
scriptfile=$1$ext1
mdcopy=$1$ext2
pdfout=$1$ext3
echo "copy to markdown"
# cp $scriptfile temp.md
echo "sed preprocessing"
tac $scriptfile > temp2.md
sed -i '/^# end of Python header, start of markdown py2pdf/,$d' temp2.md
tac temp2.md > temp.md
# rm temp2.md
sed -i '/^#~~ no export to pdf from here/,$d' temp.md
sed -i -e 's/#~~ //1' temp.md
echo "sed preprocessing PEP compatibility"
sed -i '/^# ~~ no export to pdf from here/,$d' temp.md
sed -i -e 's/^\s*# ~~ //' temp.md
sed -i -e 's/^\s*# ~~//' temp.md # added because black remove trailing space
echo "perl preprocessing"
perl -ne 's/^!\[\[(.+?)\]\].*/`cat $1`/e;print' temp.md > $mdcopy
echo "pandoc to pdf"
pandoc -s -o $pdfout --filter pandoc-crossref --citeproc $mdcopy
echo "delete temp files"
# rm temp.md # temp.md never erase for debugging
# rm $mdcopy
echo "end of bash"
