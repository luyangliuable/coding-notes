
* Assign a list of process that has discord in process name to highest priority
```sh
sudo renice -n -20 -p $(pgrep -f Discord)
```
