# Redirection

## Bash Redirection
Bash allows us to redirect the input, output, and errors from our commands to files or other commands. This is accomplished using redirection operators.

## Standard Input (stdin)
< file: Redirects the contents of file to the standard input of a command.

```bash
command < file.txt
Standard Output (stdout)
```

## > file: Redirects the standard output of a command to a file, overwriting its contents.

```bash
command > file.txt
```

## >> file: Appends the standard output of a command to a file.

```bash
command >> file.txt
Standard Error (stderr)
```

## 2> file: Redirects the standard error of a command to a file, overwriting its contents.

```bash
command 2> file.txt
2>> file: Appends the standard error of a command to a file.
```

```bash
command 2>> file.txt
Combining stdout and stderr
```

## &> file: Redirects both standard output and standard error of a command to a file, overwriting its contents.
```bash
command &> file.txt
&>> file: Appends both standard output and standard error of a command to a file.
```

```bash
command &>> file.txt
```

## Pipe operator
|: Sends the standard output of one command to the standard input of another.

```bash
command1 | command2
```

## Here Documents and Here Strings
<<END: A here document. Takes the input between the two END statements and feeds it into a command. END can be replaced with any string.

```bash``
command <<END
multi-line
input
END
```

```bash
while IFS= read -r line; do
    new_files+=("$line")
done << "$new_files_output"
```


## <<< "string": A here string. Feeds a string into a command as input.

```bash
command <<< "input string"
```


```bash
python <<< END
print("Hello, World!")
END
```
