import tkinter as tk
import json
import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json&valcode=USD")
todos = json.loads(response.text)
a = todos[0]
b = a['rate']

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.lable1 = tk.Label(text="Курс доллара на сегодня " + str(a['rate']))
        self.lable1.pack()
        self.lable2 = tk.Label(text="Введите цену товара в Долларах США")
        self.lable2.pack()
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Рассчитать", command=self.on_button)
        self.entry.pack()
        self.button.pack()



    def on_button(self):
        content = float((self.entry.get()))
        c = int(content * b)
        self.lable3 = tk.Label(text="Цена товара в Гривнах: " + str(c))
        self.lable3.pack()

app = SampleApp()
app.mainloop()