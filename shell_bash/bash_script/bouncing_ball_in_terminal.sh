#!/bin/bash

# Set the initial position of the ball
xpos=0
ypos=0

# Set the direction of the ball (1 = right, -1 = left)
xdir=1

# Set the speed of the ball
speed=0.1

# Clear the terminal
clear

while true; do
    # Move the ball
    xpos=$(echo $xpos + $xdir*$speed | bc)
    ypos=$(echo "scale=2; $ypos + sqrt(1-$xpos^2)" | bc -l)

    # Check if the ball has hit the edge of the terminal
    if [ $(echo "$xpos > 1" | bc -l) -eq 1 ]; then
        xdir=-1
    elif [ $(echo "$xpos < -1" | bc -l) -eq 1 ]; then
        xdir=1
    fi

    # Clear the terminal
    clear

    # Draw the ball
    for ((i=0; i<=24; i++)); do
        for ((j=0; j<=79; j++)); do
            if [ $(echo "$i == $(echo "scale=0; 24-$ypos*12" | bc -l) && $j == $(echo "scale=0; 39+$xpos*39" | bc -l)" | bc) -eq 1 ]; then
                echo -n "O"
            else
                echo -n " "
            fi
        done
        echo ""
    done

    # Wait for a bit
    sleep 0.05
done
