# CREATING REMINDERS TO DRINK WATER USING PYTHON

# IMPORT SOME REQUIRED PYTHON MODULES
import time
from plyer import notification

# MAIN FUNCTION OF THE PROGRAM
if __name__ == '__main__':

    # CONTINUES WHILE LOOP YOU CAN ALSO USE SIMPLE WHILE LOOP TO SEND THE MESSAGE AGAIN AND AGAIN
    while True:

        # CREATE A NOTIFICATION USING PLYER MODULE
        notification.notify(

            # SET THE SOME NOTIFICATION PARAMETERS : TITLE, DESCRIPTION,  NOTIFICATION ICON AND TIME OF NOTIFICATION
            title="It's time to drink water, please drink water!",
            message="Water boosts energy and it helps weight loss and digestion. Water hydrates skin.",
            # DOWNLOAD THIS ICON HERE: https://icons.iconarchive.com/icons/iconsmind/outline/512/Glass-Water-icon.png
            
            app_icon=r"Glass-Water-icon.ico",
            timeout=5
        )

        # TIME DELAY BETWEEN EACH NOTIFICATION
        # WE SET 60*60 TIME DELAY MEANS IT TAKES 3600 SECONDS ( 1 HOUR ) TO SEND ANOTHER NOTIFICATION FOR DRINK WATER
        time.sleep(60*60)