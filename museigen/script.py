import pygame,sys
from pygame.locals import *

#registrando o modulo
sys.path.insert(0,'/home/talison/Documentos/snakeGM')


class Museigen:
    #------------------------------------------------------------
    def __init__(self):
        #keys
        self.keydown={'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False, '8': False, '9': False, '10': False, '11': False, '12': False, '13': False, '14': False, '15': False, '16': False, '17': False, '18': False, '19': False, '20': False, '21': False, '22': False, '23': False, '24': False, '25': False, '26': False, '27': False, '28': False, '29': False, '30': False, '31': False, '32': False, '33': False, '34': False, '35': False, '36': False, '37': False, '38': False, '39': False, '40': False, '41': False, '42': False, '43': False, '44': False, '45': False, '46': False, '47': False, '48': False, '49': False, '50': False, '51': False, '52': False, '53': False, '54': False, '55': False, '56': False, '57': False, '58': False, '59': False, '60': False, '61': False, '62': False, '63': False, '64': False, '65': False, '66': False, '67': False, '68': False, '69': False, '70': False, '71': False, '72': False, '73': False, '74': False, '75': False, '76': False, '77': False, '78': False, '79': False, '80': False, '81': False, '82': False, '83': False, '84': False, '85': False, '86': False, '87': False, '88': False, '89': False, '90': False, '91': False, '92': False, '93': False, '94': False, '95': False, '96': False, '97': False, '98': False, '99': False, '100': False, '101': False, '102': True, '103': False, '104': False, '105': False, '106': False, '107': False, '108': False, '109': False, '110': False, '111': False, '112': False, '113': False, '114': False, '115': False, '116': False, '117': False, '118': False, '119': False, '120': False, '121': False, '122': False, '123': False, '124': False, '125': False, '126': False, '127': False}
        self.keyup={'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False, '8': False, '9': False, '10': False, '11': False, '12': False, '13': False, '14': False, '15': False, '16': False, '17': False, '18': False, '19': False, '20': False, '21': False, '22': False, '23': False, '24': False, '25': False, '26': False, '27': False, '28': False, '29': False, '30': False, '31': False, '32': False, '33': False, '34': False, '35': False, '36': False, '37': False, '38': False, '39': False, '40': False, '41': False, '42': False, '43': False, '44': False, '45': False, '46': False, '47': False, '48': False, '49': False, '50': False, '51': False, '52': False, '53': False, '54': False, '55': False, '56': False, '57': False, '58': False, '59': False, '60': False, '61': False, '62': False, '63': False, '64': False, '65': False, '66': False, '67': False, '68': False, '69': False, '70': False, '71': False, '72': False, '73': False, '74': False, '75': False, '76': False, '77': False, '78': False, '79': False, '80': False, '81': False, '82': False, '83': False, '84': False, '85': False, '86': False, '87': False, '88': False, '89': False, '90': False, '91': False, '92': False, '93': False, '94': False, '95': False, '96': False, '97': False, '98': False, '99': False, '100': False, '101': False, '102': True, '103': False, '104': False, '105': False, '106': False, '107': False, '108': False, '109': False, '110': False, '111': False, '112': False, '113': False, '114': False, '115': False, '116': False, '117': False, '118': False, '119': False, '120': False, '121': False, '122': False, '123': False, '124': False, '125': False, '126': False, '127': False}
        #definindo parâmetros importantes
        self.game=True
        self.clock=pygame.time.Clock()
        self.fps=30
        self.gameSize=[600,600]
        self.background=[0,0,0]
        self.Objects()

    def Objects(self):
        #aqui dentro é definido os objetos que seram instanciados...
        pass


    def inited(self):
        #inicializando o pygame
        pygame.init()
        
        #-|inicializando o jogo|----------------------------


        #criando o display /tela
        self.screen=pygame.display.set_mode(self.gameSize)

        while self.game:
            self.clock.tick(self.fps)
            #preenchendo o fundo com uma cor
            self.screen.fill(self.background)
            #configurações o butão de cancelar janela
            self.keyboards()
            #ijdjds
            self.gamer()

            #atualizando a tela
            pygame.display.update()

    #------------------------------------------------------------       

    def gamer(self):
        pass

    #|RECURSOS|-------------------------------------------------

    def draw(self,objects):
        for obj in objects:
                pygame.draw.rect(self.screen,obj['color'],[obj['pos'][0],obj['pos'][1],obj['size'][0],obj['size'][1]])

    def keyRegistrer(self,numbers):
        for number in numbers:
            if not number in self.keys:
                self.keys.append(number)

    def keyboards(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                for chave in range(1,128):
                    if event.key==chave:
                        self.keydown[f'{chave}']=True
                        self.keyup[f'{chave}']=False
                    else:
                        self.keydown[f'{chave}']=False

            if event.type == KEYUP:
                for chave in range(1,128):
                    if event.key==chave:
                        self.keydown[f'{chave}']=False
                        self.keyup[f'{chave}']=True
                    else:
                        self.keyup[f'{chave}']=False

#---------------------------------------------------------------------------------------------------|