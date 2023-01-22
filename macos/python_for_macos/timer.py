import rumps
import datetime

class Timer(rumps.App):
    @rumps.timer(1)
    def update_time(self, _):
        self.title = str(datetime.datetime.now().time())

    @rumps.clicked("Preferences")
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")


if __name__ == "__main__":
    Timer("Timer").run()
