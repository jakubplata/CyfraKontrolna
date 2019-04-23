# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import showerror
from nr_kw import NumerKW, NumeryKW
import sys

class CyfraKontrolnaGUI:

    def __init__(self, root):
        self.root = root
        self.root.title(u'CK')

        self.make_widgets()
        self.root.bind('<Return>', self.sprawdz_nr_kw)
        self.root.bind('<Delete>', self.clear)
        self.root.bind('<Shift-Delete>', self.clear_all)
        self.root.bind('<Alt-c>', self.copy)
        self.root.iconbitmap('./img/ck.ico')

    def make_widgets(self):
        ramka_spr = LabelFrame(self.root, text='Cyfra kontrolna')
        ramka_spr.pack(side=TOP)

        self.sad_spr = Entry(ramka_spr, width=6, font="Helvetica 20 bold")
        self.sad_spr.pack(side=LEFT, ipady=5)
        Label(ramka_spr, text='/', font="Helvetica 24 bold").pack(
            side=LEFT)
        self.numer_kw_spr = Entry(ramka_spr, width=9,
                                     font="Helvetica 20 bold")
        self.numer_kw_spr.pack(side=LEFT, ipady=5)
        Label(ramka_spr, text='/', font="Helvetica 24 bold").pack(
            side=LEFT)
        self.cyfra_kw_spr = Label(ramka_spr, width=2,
                                     font="Helvetica 20 bold",
                                     foreground='green')
        self.cyfra_kw_spr.pack(side=LEFT, ipady=5)

        self.sad_spr.focus()

        self.szukaj_kw = Button(self.root,
                                   text='Sprawdź',
                                   command=self.sprawdz_nr_kw)
        self.szukaj_kw.pack(side=LEFT)
        self.c_all = Button(self.root, text=u'Czyść całość', command=self.clear_all).pack(side=RIGHT)
        self.c = Button(self.root, text=u'Czyść', command=self.clear).pack(side=RIGHT)
        #self.szukaj_kw.pack(side=BOTTOM, anchor=NW)

    def sprawdz_nr_kw(self, event=None):
        numer = '/'.join((self.sad_spr.get(), self.numer_kw_spr.get()))
        try:
            nk = NumerKW(numer)
            kw = nk.cyfra_kontrolna()
            self.root.clipboard_clear()
            self.root.clipboard_append(kw)
            sad, numer, cyfra = kw.split('/')
        except KeyError:
            showerror('BŁĄD', 'Błędny numer KW')
        else:
            self.sad_spr.delete(0, END)
            self.sad_spr.insert(0, sad)
            self.numer_kw_spr.delete(0, END)
            self.numer_kw_spr.insert(0, numer)
            self.cyfra_kw_spr.config(text=cyfra)

    def clear_all(self, event=None):
        self.sad_spr.delete(0, END)
        self.numer_kw_spr.delete(0, END)
        self.cyfra_kw_spr.config(text='')
        self.sad_spr.focus()

    def clear(self, event=None):
        self.numer_kw_spr.delete(0, END)
        self.cyfra_kw_spr.config(text='')
        self.numer_kw_spr.focus()

    def copy(self, event=None):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.numer_kw_spr.get())


if __name__ == "__main__":
    if len(sys.argv) == 2:
        nk = NumeryKW(sys.argv[1])
        nk.oblicz_numery()
    else:
        root = Tk()
        CyfraKontrolnaGUI(root)
        root.mainloop()