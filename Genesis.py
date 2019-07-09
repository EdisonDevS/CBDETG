import numpy as np
import random

class Genesis:
	def __init__(self):
		self.map=[]
		#mapa
		self.MAPSIZE = [5, 5]
		self.MAXROOMSIZE = [10, 21]
		self.MINROOMSIZE = [10, 21]


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

		roomType = self.roomTypeSelector()

		self.fillRoom(room, roomType)

		self.printRoom(room)
		
		return room


	def fillRoom(self, room, roomType):
		self.putFloor(room, roomType[0])
		self.solidPatternDesigner(room, roomType[1])
		self.putWalls(room, roomType[2])


	def putFloor(self, room, roomType):
		floor = np.random.choice(roomType[0], p=roomType[1], size=(10, 21))

		for j in range(10):
			for k in range(21):
				room[j][k] = floor[j][k]



	def putWalls(self, room, roomType):
		dimensions=room.shape

		#se pone la pared superior
		for i in range(dimensions[1]):
			room[0][i] = np.random.choice(roomType[0], p=roomType[1], size=(1,1))[0]

		#se pone la pared inferior
		for i in range(dimensions[1]):
			room[dimensions[0] - 1][i] = np.random.choice(roomType[0], p=roomType[1], size=(1,1))[0]

		#se pone la pared lateral izquierda
		for i in range(dimensions[0]):
			room[i][0] = np.random.choice(roomType[0], p=roomType[1], size=(1,1))[0]

		#se pone la pared lateral derecha		
		for i in range(dimensions[0]):
			room[i][dimensions[1] - 1] = np.random.choice(roomType[0], p=roomType[1], size=(1,1))[0]


	def solidPatternDesigner(self, room, roomType):
		solidPatterns=0
		#se escoge la cantidad de patrones de bloques solidos a partir de el tamaño
		#de la mazmorra
		if room.shape[1] <= 11:
			solidPatterns = 1

		elif room.shape[1] <= 16:
			solidPatterns = 2

		elif room.shape[1] <= 21:
			solidPatterns = 3

		increment = 0
		col = 2

		for i in range(solidPatterns):
			shape = self.solidShapeRandomizer(roomType)

			row = random.randint(2,4)
			col += increment

			for j in shape:
				for k in j:
					room[row][col] = k
					col += 1
				row += 1
				col -= len(j)

			increment = 5


	def roomTypeSelector(self):
		"""
		[
			([piso],[p piso]),
			([obstaculos], [p obstaculos]),
			([paredes], [p paredes])
		]
		"""
		return random.choice(
			[
				[
					([1,2],[0.8, 0.2]),
					([3,4,1,2], [0.3,0.2,0.3,0.2]),
					([5,6], [0.8, 0.2])
				]
			]
			)


	def solidShapeRandomizer(self, roomType):
		return np.random.choice(roomType[0], p=roomType[1], size=(4, 4))


	def printRoom(self, room):
		dimensions=room.shape

		for i in room:
			print(i)