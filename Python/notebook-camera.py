# DAS ALLES GEHÖRT IN EINE ZELLE!

import cv2


# Verbindung mit der Standardkamera des Computers
cap = cv2.VideoCapture(0)


# Verwende automatisch Breite und Höhe des Video-Feeds
# (gibt eine Gleitkommazahl (float) zurück, die wir später in eine Ganzzahl (integer) umwandeln müssen!)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    
    # Erfasse Frame (Einzelbild) für Frame
    ret, frame = cap.read()

    # Hier werden unsere Operationen auf das Frame angewendet
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Zeige das resultierende Frame an
    cv2.imshow('frame',gray)
    
    # Dieser Befehl lässt uns das Programm beenden durch Drücken der "q"-Taste auf der Tastatur.
    # Einfach nur das X des Fensters drücken funktioniert nicht!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Beende die Bilderfassung und zerstöre das Fenster, wenn alles getan ist
cap.release()
cv2.destroyAllWindows()
