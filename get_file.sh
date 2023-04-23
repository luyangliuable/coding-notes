function get_file {
    if [ -z $1 ]; then
        file=$(ls -t ~/Desktop | head -1)
    else
        file=$(ls -t $0 | head -1)
    fi
        
    echo "The latest screenshot file is $file"

    full_file_path=~/Desktop/$file

    current_dir="$(pwd)"

    new_file_name=$(openssl rand -base64 48 | cut -c1-4)

    mv "$full_file_path" "$current_dir/$new_file_name.png"
}

get_file
