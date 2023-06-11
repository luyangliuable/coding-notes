# Tricks from Using Bash to Simply Tasks

* Bash change all files starting with weather* to Weather*

```sh
for file in weather*; do mv "$file" "Weather${file#weather}"; done
```

