import pygame

class Dona:
    def __init__(self, tam, coordenadas, path_imagen) -> None:
        self.coordenadas = coordenadas
        self.path_imagen = path_imagen
        self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), tam)
        self.rect = self.image.get_rect()
        self.rect.topleft = coordenadas
        self.activa = True
    
    def actualizar(self):
        self.rect.y += 5
        