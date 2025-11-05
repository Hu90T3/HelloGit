import time
import math
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def heart_wave(t):
    for y in range(12, -12, -1):
        line = ""
        for x in range(-30, 30):
            # Ecuación del corazón
            eq = ((x*0.05)**2 + (y*0.1)**2 - 1)**3 - (x*0.05)**2 * (y*0.1)**3
            # Pulso usando sin
            if eq <= 0 and math.sin(t + x*0.1) > 0:
                line += "❤️"
            else:
                line += "  "
        print(line)

t = 0
try:
    while True:
        clear_console()
        heart_wave(t)
        t += 0.3
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n¡Se acabó el corazón palpitante! 💔")