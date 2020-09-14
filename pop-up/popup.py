import win10toast as wt
import requests
from bs4 import BeautifulSoup as BS
from tkinter import *


def alert_popup(title, message):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    message = title + '\n' + message
    w = Label(root, text=message, width=120, height=10)
    w.pack()
    mainloop()


toaster = wt.ToastNotifier()
last_header_sent = 0
last_main_sent = 0


while True:
    r = requests.get("http://127.0.0.1:5000/")
    html = BS(r.content, "html.parser")
    for i in html.select('.notifications'):
        title = i.select(".notification_header")
        main = i.select(".notification_main")
#        repeat = i.select(".notification_repeat")
        last_header = title[0].text
        last_main = main[0].text
    if last_main_sent != last_main or last_header_sent != last_header:
        for i in range(5):
            alert_popup(last_header, last_main)
        toaster.show_toast(last_header, last_main, icon_path='', duration=10)
        last_header_sent = last_header
        last_main_sent = last_main
