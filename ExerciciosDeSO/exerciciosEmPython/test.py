import sys
import time

frase = " Frase animada aqui Frase dois  "

for i in frase.split():
    print(i, end=' ')
    sys.stdout.flush()
    time.sleep(0.2)
