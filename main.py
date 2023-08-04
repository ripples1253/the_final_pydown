import pygame

pygame.init()
pygame.mixer.music.load('sounds.xm')
pattern = 10
loop_event = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(loop_event)
pygame.mixer.music.play(start=pattern)

while True:
    for event in pygame.event.get():
        if event.type == loop_event:
            pygame.mixer.music.play(start=pattern)