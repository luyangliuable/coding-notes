function name {
    echo $0
    file=$(ls -t $0 | head -1)
    echo `The latest screenshot file is $file`
}
name
