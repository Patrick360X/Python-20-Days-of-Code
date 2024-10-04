import time
from plyer import notification

title = 'Drink Water Remainder'

message= 'Take a Break have some water, walk around and come back'

notification.notify(title= title,
                    message= message,
                    timeout= 15,
                    toast= False)

time.sleep(60*60)


# to run in backgroup and notify
#pythonw.exe .\<your-file-name-here>