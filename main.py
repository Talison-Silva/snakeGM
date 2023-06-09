from museigen.script import Museigen
from objects.snake.script import Snake2
from objects.coin.script import Coin

class SnakeGM(Museigen):
    #@--------------------------------------------------------------------@
    def Objects(self):
        #--@definindos os objetos--@
        self.snake=Snake2()        #
        self.coin=Coin()           #
        #@-------------------------@
        #--@definindo o fps--@
        self.fps=15          #
        #@-------------------@

    #@--------------------------------------------------------------------@
    def gamer(self):
        #--@executando os objetos e seus comportamentos--@
        self.snake.inited(self,len(self.coin.delete))    #
        self.coin.inited(self,self.snake.header[-1])     #
        #@-----------------------------------------------@
        #--@fim do jogo----------------@
        if self.snake.die()==True:     #
            self.game=False            #
        #@-----------------------------@

    #@--------------------------------------------------------------------@


SnakeGM().inited()

