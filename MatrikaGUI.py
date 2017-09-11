from tkinter import *

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

class Primer(Frame):
    def __init__(self, glavni):
        Frame.__init__(self, glavni)
        self.table = Matrika(self, 2, 2)
        self.submit = Button(self, text="Zaženi", command=self.klik)
        self.table.pack(side="top", fill="both")
        self.submit.pack(side="bottom")

    def klik(self):
        print(self.table.get())

root = Tk()
Primer(root).pack(side="top", fill="both")
root.mainloop()