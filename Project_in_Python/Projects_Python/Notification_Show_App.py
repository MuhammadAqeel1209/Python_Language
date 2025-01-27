from plyer import notification
import time

while True:
    notification.notify(
        title = "Please take Nutrition ", 
        message = """Women ages 19 to 50 should aim for 1,800 to 2,000 daily calories, and women ages 51 and older 1,600 calories. 
        Men ages 19 to 50 should aim for 2,200 to 2,400 calories, and those ages 51 and older 2,000 calories.""",
        app_icon = "E:\Python\Projects\icon.ico" ,
        timeout = 3
        )
    time.sleep(10)