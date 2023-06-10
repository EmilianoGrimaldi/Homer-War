import pygame
import sys
from config import *
from donas import *
import random

pygame.init()

ventana = pygame.display.set_mode((TAM_PANTALLA))
pygame.display.set_caption("Donus war")

reloj = pygame.time.Clock()

icono = pygame.transform.scale(pygame.image.load(".\src\img\dona.png").convert_alpha(), SIZE_ICONO)
pygame.display.set_icon(icono)
fondo = pygame.transform.scale(pygame.image.load(".\src\img\\background.jpg").convert(), TAM_PANTALLA)

homero_l = pygame.transform.scale(pygame.image.load(".\src\img\homer_left.png").convert_alpha(), HOMER_TAM)
homero_l_rect = homero_l.get_rect()
homero_l_rect.midbottom = BOTTOM_MID

homero_r = pygame.transform.scale(pygame.image.load(".\src\img\homer_right.png").convert_alpha(), HOMER_TAM)
homero_r_rect = homero_r.get_rect()
homero_r_rect.midbottom = BOTTOM_MID

homero = homero_l

donas = []

for i in range(10):
    x = random.randrange(30, ANCHO - 30)
    y = random.randrange(-1000, 0)
    dona = Dona(DONA_TAM, (x, y), ".\src\img\dona.png")
    donas.append(dona)

# dona = pygame.transform.scale(pygame.image.load(".\src\img\dona.png").convert_alpha(), DONA_TAM)
# dona_rect = dona.get_rect()
# dona_rect.midtop = TOP_MID
flag_dona = True

rect_boca_homer = pygame.Rect(0, 0, 50, 10)
rect_boca_homer.x = homero_l_rect.x + 40
rect_boca_homer.y = homero_l_rect.y + 130

pygame.mixer.music.load("src\sounds\ouch.mp3")
flag_sonido = False


fuente = pygame.font.Font("src\\fonts\simpsons.ttf", 48)
score = 0

while True:
    reloj.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if homero_l_rect.right <= ANCHO_MAX:
            homero_l_rect.x += VELOCIDAD_HOMER
            rect_boca_homer.x = homero_l_rect.x + 70
            rect_boca_homer.y = homero_l_rect.y + 130
            homero = homero_r

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if homero_l_rect.left >= ANCHO_INICIAL:
            homero_l_rect.x -= VELOCIDAD_HOMER
            rect_boca_homer.x = homero_l_rect.x + 40
            rect_boca_homer.y = homero_l_rect.y + 130
            homero = homero_l
            
    
    
    pygame.draw.rect(ventana, RED, rect_boca_homer)   
    ventana.blit(fondo, COORD_ORIGEN)
    ventana.blit(fuente.render(f"Score: {score}", True, GREEN), SCORE_POS)
    ventana.blit(homero, homero_l_rect)
    
    for dona in donas:
 
        if dona.rect.bottom <= ALTURA_MAX:
            flag_dona = True
            flag_sonido = True
            if dona.activa:
                dona.actualizar()
            else:
                dona.rect.y = 0
                
            if rect_boca_homer.colliderect(dona.rect):
                
                dona.activa = False
                if flag_sonido:
                    score += 1
                    pygame.mixer.music.play()
                    pygame.mixer_music.set_pos(0.3)
                    flag_sonido = False
                else:
                    flag_sonido = True
            
            if dona.activa:
                ventana.blit(dona.image, dona.rect)    
    
    
        
     
    pygame.display.flip()