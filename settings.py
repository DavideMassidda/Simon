# -*- coding: utf-8 -*-
from Tkinter import *
import tkFont

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
MonitorResW.set(1440)
MonitorResH = IntVar()
MonitorResH.set(900)
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
# Pulsante
# ------------------------------------
goMain = 0
# Se goMain rimane uguale a zero alla fine dello script, l'applicazione verra' chiusa.
# Questo serve perche', se la maschera info viene chiusa dal pulsante x, quindi senza
# premere il pulsante send, la successiva esecuzione del programma non deve avvenire.
def WriteInfo():
    global maskInfo,SubjCode,goMain,IsTrain
    goAhead = 0
    if IsTrain.get() == 1:
        goAhead = 1
    else:
        if SubjCode.get() != 0 and FirstSeq.get() != 0:
            dataFile = open("data/subjects.csv","a")
            dataFile.write("%g;%g;%g;%s;%g\n"%(SubjCode.get(),Year.get(),Age.get(),Sex.get(),FirstSeq.get()))            
            dataFile.close()
            goAhead = 1
    if goAhead == 1 or IsTrain == 1:
        maskInfo.quit()
        goMain = 1

infoBut = Button(buttonFrame,text="START",default="active",bg="#5a5a5a",fg="white",command=WriteInfo)

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
maskInfo.mainloop()
if goMain == 0:
    quit()
else:
    maskInfo.destroy()
