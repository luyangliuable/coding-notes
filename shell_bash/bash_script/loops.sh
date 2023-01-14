#!/bin/bash

first_greeting="Nice to meet you!"
later_greeting="How are you?"
greeting_occasion=0

while [ $greeting_occasion -lt 3 ]
do
    if [ $greeting_occasion -lt 1 ]
    then
        echo $first_greeting
    else
        echo $later_greeting
    fi

    greeting_occasion=$((greeting_occasion+1))
done

# if [ $greeting_occasion -lt 1 ]
# then
#     echo $first_greeting
# else
#     echo $later_greeting
# fi
