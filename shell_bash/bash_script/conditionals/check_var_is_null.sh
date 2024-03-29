# Get the list of modified files
modified=$(git status | awk '/modified:/ { print $2 }')

# Get the list of untracked files
untracked=$(git status --porcelain | awk '/^\?\?/ { print $2 }')

# Create commit message with the modified and untracked files
if [ -z "$untracked" ] && [ -n "$modified" ]; then
    gitmessage="Modified notes $modified."
elif [ -n "$untracked" ] && [ -n "$modified" ]; then
    gitmessage="Added notes on $untracked. Modified notes $modified."
elif [ -n "$untracked" ] && [ -z "$modified" ]; then
    gitmessage="Added notes on $untracked."
fi
