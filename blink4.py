import pygame as pg
from timer_event import TimerEvent
import time

contador = 1
funcionando = True
estado = False
color = [(220,220,0), (50,50,50)]
pg.init()
screen = pg.display.set_mode((500,500), 0, 32)

def blink(packet):
    global estado
    estado = not(estado)

te = TimerEvent(interval=1.0)
te.subscribe("Temporizador1_handler", blink)

while funcionado:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            funcionando = False
            break
    
    screen.fill([100, 100, 100])
    pg.draw.circle(screen, color[estado], (200,200), 70)
    pg.display.flip()

    print(contador, end='\r')
    contador = contador+1

te.stop()
pg.quit()