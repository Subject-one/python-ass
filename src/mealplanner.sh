#!/bin/bash
if [[ $1 == "-help" ]]
then 
cat help.md
exit 0
fi

if [[ -x "$(command -v python3)" ]]
then 
    pyv="$(python3 -V 2>&1)"
    echo $pyv
    if [[ $pyv == "Python 3"* ]]
    then
        python3 -m pip install simple-term-menu
        if [[ $1 == "--random" ]]
        then 
        python3 main.py $1
        else 
        python3 main.py
        fi
    exit 0
    else
        echo "You are using the wrong version of Python." >&2
        exit 1
    fi
elif [[ -x "$(command -v python)" ]]
    then 
        pyv="$(python -V 2>&1)"
        echo $pyv
    if [[ $pyv == "Python 3"* ]]
    then
        python -m pip install simple-term-menu
        if [[ $1 == "--random" ]]
        then 
        python main.py $1
        else 
        python main.py
        fi
        exit 0
    else
        echo "You are using the wrong version of Python." >&2
        exit 1
    fi
else
    echo "You don't have Python installed!"
    exit 1
fi