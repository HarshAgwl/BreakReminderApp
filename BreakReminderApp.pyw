import tkinter as tk
from tkinter.font import Font
import datetime
import time
import threading

bgColor = "#32648F"
interval = 25*60
waitTime = 20

root = tk.Tk()
root.attributes("-topmost", True)
root.configure(background=bgColor)

nextTime = datetime.datetime.now()+datetime.timedelta(seconds=interval)
#root.wm_attributes('-type', 'splash')
root.overrideredirect(True)

root.title("Break Reminder")
root.resizable(False, False)  # This code helps to disable windows from resizing

window_width = 900
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def startChecking():
    global nextTime
    while True:
        #print(datetime.datetime.now(),nextTime,datetime.datetime.now()>nextTime)
        if datetime.datetime.now()>nextTime:
            #print("Take a Break")
            root.deiconify()
            time.sleep(waitTime)
            root.withdraw()
            nextTime = datetime.datetime.now()+datetime.timedelta(seconds=interval)
        time.sleep(1)


threading.Thread(target=startChecking).start()

mFont = Font(family="Segoe UI",size=50)
mainLabel = tk.Label(root,text="Take a break Dude!!", bg=bgColor, fg="white")
mainLabel.pack(pady=(50,0))
mainLabel.configure(font=mFont)


text2 = """Things you can do:
● Close your eyes
● Roll your eyes in different directions
● Splash water on your eyes
● Focus on a distant object for 20 seconds
"""
subFont = Font(family="Segoe UI",size=12)
label2 = tk.Label(root,text=text2, bg=bgColor, fg="white", justify=tk.LEFT, anchor='w')
label2.pack(pady=(50,50))
label2.configure(font=subFont)

#closeButton = ttk.Button(root,text="Close")
#closeButton.pack()

root.withdraw()

root.mainloop()

