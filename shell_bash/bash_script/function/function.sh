#!/bin/bash

function foo() {
    : '
    This function prints the number of arguments passed to it and the values of the arguments.
    '
    # Print the number of arguments passed to the function
    echo "Number of arguments: $#"
    # Print the first argument passed to the function
    echo "Received argument $1"
    # Print the second argument passed to the function
    echo "Received argument $2"
}

foo "argument1" "argument2"
