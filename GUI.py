from tkinter import *

class GUI:
    def __init__(self, glavni):
        self.okno = glavni

        # MATRIKA A
        self.Text1 = Label(glavni, text='Št Vrstic A')
        self.Text1.pack()
        self.VrsticaA = Entry(glavni)
        self.VrsticaA.pack()

        self.Text2 = Label(glavni, text='Št Stolpcev A')
        self.Text2.pack()
        self.StolpecA = Entry(glavni)
        self.StolpecA.pack()

        self.getGumb = Button(glavni, text='zagon', command=self.zagon)
        self.getGumb.pack()

    def zagon(self):
        print(self.VrsticaA.get(), self.StolpecA.get())

jedro = Tk()
start = GUI(jedro)
jedro.mainloop()

class Matrika(Frame):
    def __init__(self, glavni, st_vrstic, st_stolpcev):
        Frame.__init__(self, glavni)

        self._entry = {}
        self.st_vrstic = st_vrstic
        self.st_stolpcev = st_stolpcev

        for vrsta in range(self.st_vrstic):
            for stolpec in range(self.st_stolpcev):
                index = (vrsta, stolpec)
                e = Entry(self)
                e.grid(row=vrsta, column=stolpec)
                self._entry[index] = e

    def get(self):
        matrika = []
        for vrsta in range(self.st_vrstic):
            current_row = []
            for stolpec in range(self.st_stolpcev):
                index = (vrsta, stolpec)
                current_row.append(self._entry[index].get())
            matrika.append(current_row)
        return matrika

class Primer(Frame, GUI):
    def __init__(self, glavni):
        Frame.__init__(self, glavni)
        self.table = Matrika(self, 2, 2)
        self.submit = Button(self, text="Zaženi", command=self.klik)
        self.table.pack(side="top", fill="both")
        self.submit.pack(side="bottom")
        self.exitGumb = Button(glavni, text='exit', command=glavni.quit)
        self.exitGumb.pack(side='bottom')

    def klik(self):
        print(self.table.get())

root = Tk()
Primer(root).pack(side="top", fill="both")
root.mainloop()