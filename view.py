import time
from datetime import datetime
import asyncio
from tkinter import *
from threading import Thread
import psutil
from database import  DataBase

data_base = DataBase()

class App:
    write = False
    root = Tk()
    root.title("CPU contoller")
    root.geometry("300x300")

    def __init__(self):
        self.cpu = Label()
        self.virtual_memory = Label()
        self.used_memory = Label()
        self.start_writer = Button(text = "Начать запись", command= self.start_write)
        self.stop_writer = Button(text="Начать запись", command=self.stop_write)

    def start(self):
            self.cpu.pack()
            self.virtual_memory.pack()
            self.used_memory.pack()
            self.start_writer.pack()
            self.root.mainloop()

    def start_write(self):
        print("start write")
        self.start_writer.destroy()
        self.timelabel = Label(text = "")
        self.stop_writer = Button(text="Остановить запись", command=self.stop_write)
        self.timelabel.pack()
        self.stop_writer.pack()
        self.write = True

    def stop_write(self):
        print("stop write")
        self.stop_writer.destroy()
        self.timelabel.destroy()
        self.start_writer = Button(text = "Начать запись", command= self.start_write)
        self.start_writer.pack()
        self.write = False


def update(application):
        timer = 0
        power = 1024 ** 3
        while True:
            timer += 1
            application.cpu["text"] = f"ЦП: {psutil.cpu_percent(interval=0.5)}%"
            application.used_memory["text"] = f"{round(psutil.disk_usage('/').free / power, 2)} GB / {round(psutil.disk_usage('/').total/ power, 2) }GB "
            application.virtual_memory["text"] = f"ОЗУ: {round(psutil.virtual_memory().free / power,2)} GB / {round(psutil.virtual_memory().total/ power, 2)}GB"
            if application.write:
                application.timelabel["text"] = timer
                print("!!!The record has been created!!!")
                data_base.workload_writer(datetime.now(),psutil.cpu_percent(interval=1),
                                          round(psutil.disk_usage('/').free / power, 2),
                                          round(psutil.disk_usage('/').total/ power, 2),
                                          round(psutil.virtual_memory().free / power,2),
                                          round(psutil.virtual_memory().total/ power, 2))
            else:
                timer = 0


def main():

    application = App()
    th = Thread(target=update, args=(application,))
    th.start()
    application.start()







