# Vim and emacs

## [use find and replace on a wildcard string in VIM?](https://stackoverflow.com/questions/10336609/is-it-possible-to-use-find-and-replace-on-a-wildcard-string-in-vim)

### vim syntax

```vim
:%s/foo\(\w+\)Bar/& = \1 + \1\Old/
```

Can use \0 for all before


### Before
```txt
fooVal1Bar;

fooVal2Bar;

fooVal3Bar;
```

### After

```txt
fooVal1Bar = Val1 + Val1Old;

fooVal2Bar = Val2 + Val2Old;

fooVal3Bar = Val3 + Val3Old;
```
