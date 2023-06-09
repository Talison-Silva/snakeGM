class Snake2:
	#@------------------------------------------------------@
	def __init__(self):
		#@definido variaveis--------------------@
		self.size=[20,20]
		self.nextMove={
			'left':True,
			'top':True,
			'right':True,
			'bottom':True
		}
		self.vetor={
			'left':False,
			'top':False,
			'right':True,
			'bottom':False
		}
		#@-------------------------------------@

		#@--constituição do corpo (header/body)----@
		self.header=[[0,0]]
		self.list=[]
		self.assimilate=0
		self.body=[]# cls.snake
		#@-----------------------------------------@

	#@------------------------------------------------------@
	def inited(self,kitDeveloper,assimilate):
		#@------------------------------@
		self.kitDeveloper=kitDeveloper
		self.assimilate=assimilate
		#@------------------------------@

		#@--definindo o body-------------------------------------------@
		body=self.list[len(self.list)-self.assimilate:len(self.list)]
		if len(body)!=0:
			del self.body[:]
			for a in body:
				self.body.append(a)
		#@-------------------------------------------------------------@

		#@-------------------------------------------------@
		#habilitando o controle do objeto (Snake)
		self.joystick()
		#habilitando movimento automatico do personagem
		self.update()
		#@-------------------------------------------------@


		#@--definindo header-----------------@
		self.header[0]=self.list[-1]		 #
		#@limite da tela---------------------@
		self.limite()						 #
		#@-----------------------------------@
		self.die()							 #
		#@-----------------------------------@

		#@------------------------------------------------------@
		for pos in self.body:
			self.kitDeveloper.draw([{
				'color':[0,255,255],
				'pos':pos,
				'size':self.size
			}])
		#
		self.kitDeveloper.draw([{
			'color':[255,0,0],
			'pos':self.header[-1],
			'size':self.size
		}])
		#@------------------------------------------------------@


	#@------------------------------------------------------@	
	def joystick(self):
		#|---------------------------------------|
		#|LEFT|----------------------|
		if self.kitDeveloper.keydown['97'] and self.nextMove['left']:
			self.vetor={
				'left':True,
				'top':False,
				'right':False,
				'bottom':False
			}
			if len(self.body)>0:	
				self.nextMove={
					'left':True,
					'top':True,
					'right':False,
					'bottom':True
				}
		#|RIGHT|---------------------|
		elif self.kitDeveloper.keydown['100'] and self.nextMove['right']:
			self.vetor={
				'left':False,
				'top':False,
				'right':True,
				'bottom':False
			}
			if len(self.body)>0:	
				self.nextMove={
					'left':False,
					'top':True,
					'right':True,
					'bottom':True
				}	
		#|TOP|-----------------------|
		elif self.kitDeveloper.keydown['119'] and self.nextMove['top']:
			self.vetor={
				'left':False,
				'top':True,
				'right':True,
				'bottom':False
			}
			if len(self.body)>0:	
				self.nextMove={
					'left':True,
					'top':True,
					'right':True,
					'bottom':False
				}	
		#|BOTTOM|--------------------|
		elif self.kitDeveloper.keydown['115'] and self.nextMove['bottom']:
			self.vetor={
				'left':False,
				'top':False,
				'right':False,
				'bottom':True
			}
			if len(self.body)>0:	
				self.nextMove={
					'left':True,
					'top':False,
					'right':True,
					'bottom':True
				}
		#|---------------------------------------|

	#@------------------------------------------------------@
	def limite(self):
		if self.header[-1][0]<0:
			self.header[-1]=[600,self.header[-1][1]]

		if self.header[-1][0]>600:
			self.header[-1]=[-20,self.header[-1][1]]

		if self.header[-1][1]<0:
			self.header[-1]=[self.header[-1][0],600]

		if self.header[-1][1]>600:
			self.header[-1]=[self.header[-1][0],-20]
		

	#@------------------------------------------------------@
	def die(self):
		if self.header[0] in self.body[0:-1]:
			return True 
		

	#@------------------------------------------------------@	
	def update(self):
		next={
			'top':[],
			'bottom':[],
			'left':[],
			'right':[]
		}
		#selecionando o proximo passo
		if self.vetor['top']: 
			next['top']=[self.header[0][0] , self.header[0][1]-self.size[0]]
		elif self.vetor['left']:
			next['left']=[self.header[0][0]-self.size[0] , self.header[0][1]]
		elif self.vetor['bottom']:
			next['bottom']=[self.header[0][0] , self.header[0][1]+self.size[0]]
		elif self.vetor['right']:
			next['right']=[self.header[0][0]+self.size[0] , self.header[0][1]]


		if not next['top'] ==[]:
			self.list.append(next['top'])
		elif not next['bottom'] ==[]:
			self.list.append(next['bottom'])
		elif not next['right'] ==[]:
			self.list.append(next['right'])
		elif not next['left'] ==[]:
			self.list.append(next['left'])