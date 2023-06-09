from random import randint

class Coin:
	#@-----------------------------------------------------------------@
	def __init__(self):
		#@--definindo atributos para a classe
		self.coins=[]                       #
		self.delete=[]                      #
		self.color=[255,255,0]              #
		self.size=[20,20]                   #
		#@----------------------------------@

	#@-----------------------------------------------------------------@
	def inited(self,kitDeveloper,header):

		#@--definindo o kit de desenvolvimento
		self.kitDeveloper=kitDeveloper       #
		#@-----------------------------------@
		#--@sumonar objetos-----
		if len(self.coins)<3:  #
			self.summer()      #
		#--@-------------------@
		#--@morte do objeto moeda
		self.die(header)        #
		#--@--------------------@
		#--@renderização das moedas
		self.render()			  #
		#--@----------------------@
	#@-------------------------------------------------------------------@
	
	def die(self,header):
		#--@die: metado responsavel por definir a morte das moedas 
		for coin in self.coins:
			if header==coin:
				self.delete.append(coin)
				del self.coins[self.coins.index(coin)]
		#@-------------------------------------------------------@
	#@-------------------------------------------------------------------@

	def render(self):
		#--@render: metado responsavel por renderizar os objetos moedas
		for pos in self.coins:                                         
			self.kitDeveloper.draw([{
				'color':self.color,
				'pos':pos,
				'size':self.size
			}])
		#@------------------------------------------------------------@
	#@--------------------------------------------------------------------@

	def summer(self):
		#--@summer: metado responsavel por definir as moedas que seram rederizadas
		if len(self.coins)<=2:
			#definindos as moedas spownadas
			self.coins.append([randint(1,30)*20,randint(1,30)*20])
		#@-----------------------------------------------------------------------@
	#@--------------------------------------------------------------------@
