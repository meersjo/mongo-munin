#!/bin/sh

python='';
if type python26 >/dev/null 2>&1; then
  python='python26'
elif type python2.6 >/dev/null 2>&1; then
  python='python2.6'
elif type python >/dev/null 2>&1; then
  python='python'
else
  echo 'No known Python found!' >&2
  exit 10
fi

python="#!/usr/bin/env $python"

for out in `ls src/body_*.py`
do
    echo $out
    x=${out#src/body_}
    x=${x%.py}

    out=mongo_$x

    echo $python > $out

    echo "" >> $out
    echo "## GENERATED FILE - DO NOT EDIT" >> $out

    cat src/header.py >> $out
    cat src/body_$x.py >> $out
    cat src/footer.py >> $out
    chmod 755 $out
done
