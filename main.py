# -*- coding: utf-8 -*-
from __future__ import division
from psychopy import visual, core, event
from settings import * # Carica la maschera per le impostazioni

# --------------------------------------
# Impostazioni esprimento
# --------------------------------------

buttons = ['l','a']         # Pulsanti di risposta (L:Dx,A:Sx)
subjCode = SubjCode.get()   # Codice numerico del soggetto
seq = FirstSeq.get()        # Codice sequenza di start
isTrain = IsTrain.get()     # Indica se registrare le risposte
ISI =  Isi.get()            # Intervallo inter-stimolo (sec)

# --------------------------------------
# Impostazioni monitor
# --------------------------------------

screenSize = (MonitorResW.get(),MonitorResH.get())  # Risoluzione (w,h)
fullscreen = FS.get()                               # Schermo intero si/no
screenColor = ScreenCol.get()                       # Colore finestra
stimColor = StimCol.get()                           # Colore stimolo

# --------------------------------------
# Organizzazione stimoli
# --------------------------------------
# Fattori sperimentali:
# Stim: stimolo (Cerchio vs Quadrato)
# Side: lato di presentazione (Dx vs Sx)

if isTrain == 0: # Non e' una sessione di prova
    Stim = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]]
    Side = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 0]]
else: # E' una sessione di prova
    seq = 1 # Si parte comunque dalla prima sequenza
    Stim = [
        [0, 1, 0, 1],
        [0, 1, 0, 1]]
    Side = [
        [1, 0, 0, 1],
        [0, 1, 1, 0]]
numStim = len(Stim) # Numero di stimoli da presentare

# --------------------------------------
# Costruzione finestra
# --------------------------------------

screen = visual.Window(size=screenSize,units="pix",fullscr=fullscreen,color=screenColor) # Finestra
screen.setMouseVisible(False) # Mouse
fixation = visual.TextStim(screen,text="+",color=stimColor,height=25,pos=(0,0)) # Punto di fissazione
screen.flip() # Avvio interfaccia

# --------------------------------------
# Istruzioni
# --------------------------------------

textWrapper = [0,0] # Dimensioni del contenitore di testo
textWrapper[0] = round(screenSize[0]*0.75)
textWrapper[1] = round(screenSize[1]*0.1)
InstrFile = open('instructions.txt','r')
instrText = InstrFile.read()
InstrFile.close()
instrStim = visual.TextStim(screen,text=instrText,color=stimColor,height=25,pos=(0,textWrapper[1]),wrapWidth=textWrapper[0])
instrStim.draw()
screen.flip()
event.waitKeys(keyList='space') # Attende che venga premuta la barra spaziatrice

# --------------------------------------
# Inizio esperimento
# --------------------------------------

alertText = "Poni l'indice sinistro sul pulsante " + buttons[1].upper() + " e l'indice destro sul pulsante " + buttons[0].upper() + ".\n\n"
alertText = alertText + "La prova comincera\' tra pochi secondi."
alertStim = visual.TextStim(screen,text=alertText,color=stimColor,height=30,pos=(0,textWrapper[1]),wrapWidth=textWrapper[0])
alertStim.draw()
screen.flip()
core.wait(7)

# --------------------------------------
# Avvio sessione
# --------------------------------------

screen.flip()           # Avvia uno schermo pulito
count = 0               # Conta quante sequenze sono state presentate
seq = seq-1             # Perche' il conteggio degli indici parte da 0 e non da 1
timer = core.Clock()    # Timer per tempi di reazione
while count < numStim:  # Inizia la presentazione degli stimoli
    count = count+1
    for i in range(4):
        fixation.draw()     # Disegna il punto di fissazione
        screen.flip()       # Riavvia la finestra
        fixation.draw()     # (Ripetizione per bug Windows)
        screen.flip()       # (Ripetizione per bug Windows)
        core.wait(ISI)      # Blocca l'esecuzione per ISI
        event.clearEvents() # Ripulisce tutte le precedenti registrazioni di pulsanti
        fixation.draw()     # Disegna il punto di fissazione
        if Stim[seq][i] == 0: # Cerchio
            exactKey = buttons[0] # Pulsante di risposta corretto
            if Side[seq][i] == 0:
                # Cerchio a sinistra
                visual.Circle(screen,radius=80,pos=(-300,0),fillColor=stimColor,lineColor=stimColor,edges=256).draw() # interpolate=True
            else:
                # Cerchio a destra
                visual.Circle(screen,radius=80,pos=(300,0),fillColor=stimColor,lineColor=stimColor,edges=256).draw() # interpolate=True
        else: # Quadrato
            exactKey = buttons[1] # Pulsante di risposta corretto
            if Side[seq][i] == 0:
                # Quadrato a sinistra
                visual.Rect(screen,width=160,height=160,pos=(-300,0),fillColor=stimColor,lineColor=stimColor).draw()
            else:
                # Quadrato a destra
                visual.Rect(screen,width=160,height=160,pos=(300,0),fillColor=stimColor,lineColor=stimColor).draw()
        screen.flip()           # Riavvia la finestra
        timer.reset()           # Azzera il timer
        t0 = timer.getTime()    # Avvia il timer
        respKey = event.waitKeys(keyList=buttons) # Attende la risposta
        t1 = timer.getTime()    # Blocca il timer
        if isTrain == 0:        # Se si deve registrare la risposta
            respTime = (t1-t0)*1000     # Calcolo tempi di reazione
            respTime = str(respTime)    # Trasformazione variabile RT in stringa
            respTime = respTime.replace('.',',') # Sostituzione punti in virgoole nel decimale per csv2
            score = respKey[0] == exactKey # Calcolo score
            if score == True:
                score = 1
            else:
                score = 0
            # Registrazione dati su file
            dataFile = open('data/expdata.csv','a')
            dataFile.write("%s;%s;%s;%s;%s;%s\n"%(subjCode,Stim[seq][i]+1,Side[seq][i]+1,count,score,respTime))
            dataFile.close()
    # Si aggiorna il valore di seq
    seq = seq+1
    if seq == numStim:
        seq = 0

# --------------------------------------
# Conclusione esperimento
# --------------------------------------

fixation.draw()
screen.flip()
core.wait(1)
alertText = "Prova conclusa\n\nGrazie per la partecipazione"
alertStim = visual.TextStim(screen,text=alertText,color=stimColor,height=30,pos=(0,200),wrapWidth=800)
alertStim.draw()
screen.flip()
core.wait(3)
screen.close()
core.quit()
