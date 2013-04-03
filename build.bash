#!/bin/bash

for out in `ls src/body_*.py`
do
    echo $out
    x=${out#src/body_}
    x=${x%.py}

    out=mongo_$x

    if type "python26" &>/dev/null; then
        echo "#!/usr/bin/env python26" > $out
    else
        if type "python2.6" &>/dev/null; then
            echo "#!/usr/bin/env python2.6" > $out
        else
            echo "#!/usr/bin/env python" > $out
        fi
    fi

    echo "" >> $out
    echo "## GENERATED FILE - DO NOT EDIT" >> $out
    cat src/header.py >> $out
    cat src/body_$x.py >> $out
    cat src/footer.py >> $out
    chmod 755 $out
done
