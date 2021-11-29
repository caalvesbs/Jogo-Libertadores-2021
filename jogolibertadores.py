import pygame
from random import randint

pygame.init()

#Variaveis de posição
''' dudu43'''
x = 200
y = 200
''' rodrigo '''
pos_x = 60
pos_y = 500
''' diego '''
pos_y_a = 1200
''' rodinei '''
pos_y_c = 1600

#tela de inicio
janela = pygame.display.set_mode((545, 690))
pygame.display.set_caption("Libertadores 2021")

inicio = pygame.image.load("telainicio.jpg")
pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play
janela.blit(inicio, (0,0))
pygame.display.update()

janela_aberta = True

pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                janela_aberta = False

#variaveis de velocidade
velocidade = 15
velocidade_outros = 8

#imagens
fundo = pygame.image.load('campo.png')
dudu43 = pygame.image.load('dudu43.png')
rodrigo = pygame.image.load('rodrigo.png')
diego = pygame.image.load('diego.png')
#xb = 493
rodinei = pygame.image.load('rodinei.png')
#xp = 640

''' Definições do cronometro '''
timer = 0
tempo_segundo = 0

font = pygame.font.SysFont('arial black', 15) 
texto = font.render("Tempo: ", True, (255,255,255), (0,0,0)) 
post_texto = texto.get_rect()
post_texto.center = (66,27) 

'''difinições da janela'''
janela = pygame.display.set_mode((540, 690))
pygame.display.set_caption("Libertadores 2021") 
janela_aberta = True 

while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    '''definição das teclas de movimentação do dudu43'''
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT] and x <= 400:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 0:
        x -= velocidade

    ''' Configurações cronometro '''
    if (timer < 10):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (255,255,255), (0,0,0))
        timer = 0


    '''respawn aleatorio, determinada entre limites'''
    if (pos_y <= -200) and (pos_y_a <= -200) and (pos_y_c <= -200):
        pos_y = randint(800,1100) #rodrigo
        pos_y_a = randint(1400,2000)#diego
        pos_y_c = randint(2300,3000)#rodinei

    '''tornando velocidade dos jogadores aleatorias'''
    pos_y -= velocidade_outros + randint(1,20)
    pos_y_a -= velocidade_outros + randint(1,20)
    pos_y_c -= velocidade_outros + randint(1,20)

    '''Jogando na tela'''
    janela.blit(fundo,(0,0)) 
    janela.blit(dudu43, (x,y)) #dudu43
    janela.blit(rodrigo, (30, pos_y)) #rodrigo
    janela.blit(diego,(pos_x + 163, pos_y_a)) #diego
    janela.blit(rodinei,(pos_x + 310, pos_y_c)) #rodinei
    janela.blit(texto, post_texto) 

    pygame.display.update()

pygame.quit()
