Bash Inline Scripts

* NOPs 100 times repeated in a string
```sh
echo -ne "\x90"{1..100}
```


```sh
a=0; while [ $a -lt 100 ] do; echo -ne "\x90"; a=$((a + 1)); done
```
