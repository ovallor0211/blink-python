import pygame as pg
import time

funcionando = True    #esta variable la vamos a usar para parar pygame cuando terminemos
estado = False        #esta variable es para ir cambiando el color del círculo

pg.init()
screen = pg.display.set_mode((500,500), 0, 32)

while funcionando:
    for event in pg.event.get():
        if event.type == pg.QUIT:           
            funcionando = False
            break

    if estado:
        color = [220,220,0]
        estado = False
    else:
        color = [50,50,50]
        estado = True

    screen.fill([100, 100, 100]) 
    pg.draw.circle(screen, color, (200,200), 70)    
    pg.display.flip()

    time.sleep(1)
        
pg.quit()