# Set uid

* Permissions are only set by owner

```
setid  rwx   rwx   rwx
     |     |     |     |
      ----- ----- -----
      ownr   grp   othr
```

## Example
```sh
chmod 4755 ./program
```

* 4 -> 100, when the user runs the program, the **root permission is given to this program**. (What users run will give this program root permission)
* 7 -> 111, **owner** can read, write and execute.
* 5 -> 101, **users in the same group** can read and execute.
* 5 -> 101, **users in other groups** can read and execute.
