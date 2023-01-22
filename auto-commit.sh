#!/bin/bash

# TODO Added following line to cron -e
# */30 * * * * cd $PATH_TO_FOLDER && $PATH_TO_FOLDER/coding-notes/auto-commit.sh


# Function to automatically commit changes to a git repository
function auto_commit() {
    # Print the received argument
    echo "Received argument $1"

    # Get the list of modified files
    modified=$(git status | awk '/modified:/ { print $2 }')

    # Get the list of untracked files
    untracked=$(git status --porcelain | awk '/^\?\?/ { print $2 }')

    # Create commit message with the modified and untracked files
    if [ -z "$untracked" ] && [ -n "$modified" ]; then
        gitmessage="Autocommit: Modified $modified."
    elif [ -n "$untracked" ] && [ -n "$modified" ]; then
        gitmessage="Autocommit: Added notes on $untracked. Modified notes $modified."
    elif [ -n "$untracked" ] && [ -z "$modified" ]; then
        gitmessage="Autocommit: Added notes on $untracked."
    fi

    echo $gitmessage

    # Add all changes
    git add .
    # Commit with the generated message
    git commit -m "$gitmessage"
    # Push to remote repository
    git push
}

# Call the function with no arguments
auto_commit
