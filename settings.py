# -*- coding: utf-8 -*-
from Tkinter import * # per costruire la maschera
import tkMessageBox # per finestre di warning
import tkFont # per le etichette
from os import path, makedirs # per gestire i file di dati

# Toplevel
maskInfo = Tk()
maskInfo.wm_title("")

# Frame
infoFrame0 = Frame(maskInfo,padx=5,pady=5,bg="#5a5a5a",width=500,height=40)
infoFrame1 = Frame(maskInfo,padx=5,pady=10)
infoFrame1 = Frame(maskInfo,padx=15,pady=10)
infoFrame3 = Frame(maskInfo,padx=15,pady=10)
buttonFrame = Frame(maskInfo,pady=5,height=40)

# Font dei titoli di sezione
sectionFont = tkFont.Font(family='sans serif',weight='bold')

# ------------------------------------
# Intestazione
# ------------------------------------
font = tkFont.Font(family='sans serif',weight='bold',size=14)
titleLabel = Label(infoFrame0,text="",font=font,bg="#5a5a5a",fg="white")

# ------------------------------------
# Impostazioni soggetto
# ------------------------------------
subjectLabel = Label(infoFrame1,text="Subject information",font=sectionFont)

# Variabili
SubjCode = IntVar()
Age = IntVar()
Year = IntVar()
Sex = StringVar()

# Codice soggetto
subjCodeLabel = Label(infoFrame1,text="Code")
subjCodeCell  = Entry(infoFrame1,textvariable=SubjCode,bg="#ffff60",width=9,cursor="xterm")
# Anno di nascita
yearLabel = Label(infoFrame1,text="Year of birth")
yearCell  = Entry(infoFrame1,textvariable=Year,bg="white",width=9,cursor="xterm")
# Anni compiuti
ageLabel = Label(infoFrame1,text="Age")
ageCell  = Entry(infoFrame1,textvariable=Age,bg="white",width=9,cursor="xterm")
# Sesso
sexLabel = Label(infoFrame1,text="Sex")
sexF = Radiobutton(infoFrame1,text="Female",value="F",variable=Sex)
sexM = Radiobutton(infoFrame1,text="Male",value="M",variable=Sex)
# sexM.select()

# ------------------------------------
# Impostazioni monitor/esperimento
# ------------------------------------
settingsLabel = Label(infoFrame1,text="Experiment settings",font=sectionFont)

# Variabili
MonitorResW = IntVar()
MonitorResW.set(1366)
MonitorResH = IntVar()
MonitorResH.set(768)
ScreenCol = StringVar()
ScreenCol.set('#b4b4b4')
StimCol = StringVar()
StimCol.set('#000000')
FS = IntVar()
FS.set(1)
FirstSeq = IntVar()
FirstSeq.set(0)
Isi = DoubleVar()
Isi.set(1.5)
IsTrain = IntVar()
IsTrain.set(0)

# Risoluzione monitor (base)
reswLabel = Label(infoFrame1,text="Resolution width (pixel)")
reswCell  = Entry(infoFrame1,textvariable=MonitorResW,bg="white",width=9,cursor="xterm")
# Risoluzione monitor (altezza)
reshLabel = Label(infoFrame1,text="Resolution height (pixel)")
reshCell  = Entry(infoFrame1,textvariable=MonitorResH,bg="white",width=9,cursor="xterm")
# Colore sfondo
screenColLabel = Label(infoFrame1,text="Background color")
screenColCell  = Entry(infoFrame1,textvariable=ScreenCol,bg="white",width=9,cursor="xterm")
# Colore linea
stimColLabel = Label(infoFrame1,text="Stimuli color")
stimColCell  = Entry(infoFrame1,textvariable=StimCol,bg="white",width=9,cursor="xterm")
# Fullscreen
fullscreenBut = Checkbutton(infoFrame1,text="Full screen",variable=FS)
# Inter stimulus interval
isiLabel = Label(infoFrame1,text="ISI")
isiCell  = Entry(infoFrame1,textvariable=Isi,bg="white",width=9,cursor="xterm")
# Sequenza di partenza
seqLabel = Label(infoFrame1,text="First sequence")
seqCell  = Entry(infoFrame1,textvariable=FirstSeq,bg="#ffff60",width=9,cursor="xterm")
# Sessione di prova
istrialBut = Checkbutton(infoFrame1,text="Training session",variable=IsTrain)

# ------------------------------------
# Funzioni e pulsante di avvio
# ------------------------------------

def CloseGUI():
    maskInfo.destroy()
    quit()

def StartSession():
    if IsTrain.get() == 1:
        maskInfo.quit() # Go to the task
    else:
        checkSubj = SubjCode.get() != 0
        checkFirstSeq = FirstSeq.get() > 0 and FirstSeq.get() <= 8
        if checkSubj == True and checkFirstSeq == True:
            if not path.exists("data"):
                makedirs("data")
            if path.isfile("data/subjects.csv") == False:
                subjFile = open("data/subjects.csv","a")
                subjFile.write("%s\n"%("Subject;Birth;Age;Sex;FirstSeq"))
                subjFile.close()
            if path.isfile("data/expdata.csv") == False:
                dataFile = open("data/expdata.csv","a")
                dataFile.write("%s\n"%("Subject;Stimulus;Side;Trial;Score;RT"))            
                dataFile.close()
            subjFile = open("data/subjects.csv","a")
            subjFile.write("%g;%g;%g;%s;%g\n"%(SubjCode.get(),Year.get(),Age.get(),Sex.get(),FirstSeq.get()))
            subjFile.close()
            maskInfo.quit() # Go to the task
        else:
            if checkSubj == False:
                msg = "You must specify a code for participant."
            elif checkFirstSeq == False:
                msg = "You must specify the code of the first sequence (from 1 to 8)."
            warning = Tk()
            warning.wm_withdraw()
            tkMessageBox.showerror(title="Error message",message=msg,parent=warning)

infoBut = Button(buttonFrame,text="START",default="active",bg="#5a5a5a",fg="white",command=StartSession)

# ------------------------------------
# Costruzione interfaccia
# ------------------------------------

infoFrame0.pack()
infoFrame0.grid_propagate(0)
titleLabel.grid(row=1,column=1,columnspan=3)

infoFrame1.pack()
# Impostazioni soggetto
subjectLabel.grid(row=1,column=1,columnspan=2)
subjCodeLabel.grid(row=2,column=1,sticky="e")
subjCodeCell.grid(row=2,column=2,sticky="w")
yearLabel.grid(row=3,column=1,sticky="e")
yearCell.grid(row=3,column=2,sticky="w")
ageLabel.grid(row=4,column=1,sticky="e")
ageCell.grid(row=4,column=2,sticky="w")
sexM.grid(row=5,column=1,sticky="e")
sexF.grid(row=5,column=2,sticky="e")
# Impostazioni monitor/esperimento
settingsLabel.grid(row=1,column=3,columnspan=2)
reswLabel.grid(row=2,column=3,sticky="e")
reswCell.grid(row=2,column=4,sticky="w")
reshLabel.grid(row=3,column=3,sticky="e")
reshCell.grid(row=3,column=4,sticky="w")
screenColLabel.grid(row=4,column=3,sticky="e")
screenColCell.grid(row=4,column=4,sticky="w")
stimColLabel.grid(row=5,column=3,sticky="e")
stimColCell.grid(row=5,column=4,sticky="w")
fullscreenBut.grid(row=6,column=3,columnspan=2,sticky="e")
isiLabel.grid(row=7,column=3,sticky="e")
isiCell.grid(row=7,column=4,sticky="w")
seqLabel.grid(row=8,column=3,sticky="e")
seqCell.grid(row=8,column=4,sticky="w")
istrialBut.grid(row=9,column=3,columnspan=2,sticky="e")

# Pulsante avvio sessione
buttonFrame.pack()
infoBut.grid()

# Loop e chiusura maschera
maskInfo.protocol('WM_DELETE_WINDOW', CloseGUI)
maskInfo.mainloop()
maskInfo.destroy()
