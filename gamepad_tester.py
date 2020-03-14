import inputs
from time import sleep

while 1:
    events = inputs.get_gamepad()
    for event in events:
        if event.ev_type.strip() == "Sync" or event.code.strip() == "ABS_X" or event.code.strip() == "ABS_Y" or event.code.strip() == "ABS_Y" or event.code.strip() == "ABS_RX" :
            continue
        print(event.ev_type, event.code, event.state)
