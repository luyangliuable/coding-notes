from Foundation import *
from AppKit import *
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    touchbar_item.setTitle_(current_time)

touchbar_item = NSCustomTouchBarItem.alloc().initWithIdentifier_("Time")
touchbar_item.setView_(NSTextField.alloc().initWithFrame_(NSMakeRect(0, 0, 100, 30)))
touchbar_item.view().setStringValue_("Loading...")
touchbar_item.view().setBezeled_(False)
touchbar_item.view().setDrawsBackground_(False)
touchbar_item.view().setEditable_(False)
touchbar_item.view().setSelectable_(False)

touchbar = NSTouchBar.alloc().init()
touchbar.setDelegate_(touchbar)
touchbar.setCustom
