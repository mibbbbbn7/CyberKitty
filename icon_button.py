import pygame

class Icon_button(pygame.sprite.Sprite):
    def __init__(self, images, groups, pos, indexx):
        super().__init__(groups)
        self.images = images
        self.indexx = indexx
        self.image = self.images[self.indexx]
        self.pos = pos
        self.rect = self.image.get_frect(center = self.pos)
    
    def update(self, delta_t, window_w, window_h):
        ciao="non devo fare nulla"
    
    def on(self):
        if (self.indexx % 2) == 1:
            self.indexx -= 1
            self.image = self.images[self.indexx]
    #dato che usero questa classe per bottoni con sprite diversi ma tutti salvati nello stesso array,
    #per evitare incasinamenti con gli indici il metodo on() cambia l'immagine solo se l'indice è dispari
    #dal momento che nel main importo prima il bottone acceso(avra indice pari come 0 2 4 ecc) e poi quello spento
    #che avra indice dispari.
    #questo if aggiunge la sicurezza di cambiare stato ad acceso solo quando prima si trovava su spento


    def off(self):
        if (self.indexx % 2) == 0:
            self.indexx += 1
            self.image = self.images[self.indexx]