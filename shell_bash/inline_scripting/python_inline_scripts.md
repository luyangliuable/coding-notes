# Python Inline Scripts

This is useful if you want to perform scripts on the commandline with pytohn.

## Decode a hex value

```sh
python3 -c "print(bytes.fromhex('78252078').decode())"
```


## Print something x amount of times

```sh
python3 -c "[print('%x', end=' ') for i in range(600)]"
```

* Can be used in conjunction with other programs

```sh
clear && gcc vulnerability.c && ./a.out "`python3 -c "[print('%x', end=' ') for i in range(600)]"`"

```
