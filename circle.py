from sys import modules
import pygame as pg
import particle as module_p
#initialiser pygame et la fenetre
pg.init
w, h = 600, 600
screen = pg.display.set_mode((w, h))

running = True
#creation de particule
particles = []
for i in range(100):
    particles.append(module_p.Particle(w, h))
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #draw on screen
    screen.fill((10, 10, 30))
    for j in range(100):
        particles[j].draw(screen)
    for p in particles:
        p.draw(screen)
    clock = pg.time.Clock()
    clock.tick(60)
    pg.display.update()


pg.quit()