#!/bin/bash
python relative/path/to/my/module.py # change this to correct path
chmod +x wrapper.sh # access command
#if $1 == "--random" then python3 main.py $1

if [[ -x "$(command -v python3)" ]]
then 
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 main.py
        exit 0
    else
        echo "You are using the wrong version of Python." >&2
        exit 1
    fi
else
    echo "You don't have Python installed!"
    exit 1
fi



# optional 
# In termninal /wrapper.sh --random =>passing to bash script ( argv $)
