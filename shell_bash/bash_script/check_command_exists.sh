#! /bin/bash -e
set -o pipefail

# One line version
# type dasdasd &> /dev/null ; echo $?

# function to check if a command exists
check_command_exists () {
    # Check if the command exists and redirect any output to /dev/null
    type "$1" &> /dev/null
}

# check if the "docker" command exists
if ! check_command_exists docker; then
    # if the command does not exist, print an error message and exit with a status code of 1
    echo "You have to install docker command"
    exit 1
fi
