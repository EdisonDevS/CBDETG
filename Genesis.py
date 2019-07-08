import numpy as np
import random

class Genesis:
	def __init__(self):
		self.map=[]
		#mapa
		self.MAPSIZE = [5, 5]
		self.MAXROOMSIZE = [10, 21]
		self.MINROOMSIZE = [10, 10]



	def generateMap(self):
		for i in range(self.MAPSIZE[0]):
			row=[]

			for j in range(self.MAPSIZE[1]):
				room = self.createRoom()
				row.append(room)

			self.map.append(row)

		return self.map



	def createRoom(self):
		#Construccion de las dimensiones que tendrá la nueva habitacion
		xDimension=random.randint(self.MINROOMSIZE[0],self.MAXROOMSIZE[0])
		yDimension=random.randint(self.MINROOMSIZE[1],self.MAXROOMSIZE[1])

		#se establece el shape del arreglo de numpy
		roomDimensions=[xDimension, yDimension]
		
		#se crea el array de numpy de acuerdo a las especificaciones
		room=np.zeros(roomDimensions)

		self.fillRoom(room)

		self.printRoom(room)
		
		return room



	def fillRoom(self, room):
		self.solidPatternDesigner(room)
		self.putWalls(room)



	def putWalls(self, room):
		dimensions=room.shape

		#se pone la pared superior
		for i in range(dimensions[1]):
			room[0][i] = 1

		#se pone la pared inferior
		for i in range(dimensions[1]):
			room[dimensions[0] - 1][i] = 1

		#se pone la pared lateral izquierda
		for i in range(dimensions[0]):
			room[i][0] = 1

		#se pone la pared lateral derecha		
		for i in range(dimensions[0]):
			room[i][dimensions[1] - 1] = 1



	def solidPatternDesigner(self, room):
		solidPatterns=0
		#se escoge la cantidad de patrones de bloques solidos a partir de el tamaño
		#de la mazmorra
		if room.shape[1] == 10:
			solidPatterns = 1

		elif room.shape[1] <= 16:
			solidPatterns = 2

		elif room.shape[1] <= 21:
			solidPatterns = 3


		increment = 0
		col = 2

		for i in range(solidPatterns):
			shape = self.solidShapeRandomizer()

			row = random.randint(2,3)
			col += increment

			for j in shape:
				for k in j:
					room[row][col] = k
					col += 1
				row += 1
				col -= len(j)

			increment = 5


	def solidShapeRandomizer(self):
		return random.choice([
			[[2,0,0,0],[2,2,0,0],[2,2,2,0],[2,2,0,0],[2,0,0,0]],
			[[0,0,0,2],[0,0,2,0],[0,2,0,0],[2,0,0,0]],
			[[2,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,2]],
			[[2,0,0,0],[0,2,0,0],[0,2,0,0],[2,0,0,0]],
			[[0,0,0,2],[0,0,2,0],[0,0,2,0],[0,0,0,2]],
			[[0,0,0,0],[0,2,2,0],[0,2,2,0],[0,0,0,0]],
			[[2,0,0,2],[0,2,2,0],[0,2,2,0],[2,0,0,2]]
		])



	def printRoom(self, room):
		dimensions=room.shape

		for i in room:
			print(i)