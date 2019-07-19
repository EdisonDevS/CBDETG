import numpy as np
import random

class Genesis:
	def __init__(self):
		self.map=[]
		#mapa
		self.MAPSIZE = [5, 5]
		self.MAXROOMSIZE = [10, 21]
		self.MINROOMSIZE = [10, 21]


	def generateMap(self, level):
		self.level=level
		self.e=True
		for i in range(self.MAPSIZE[0]):
			row=[]

			for j in range(self.MAPSIZE[1]):
				room = self.createRoom()
				row.append(room)

			self.map.append(row)

		self.e=False
		print("se puso en "+str(self.e))
		self.cleanFirstRoom()
		self.putNPCs()
		self.createBossRoom()


		return self.map


	def createBossRoom(self):
		fila=2
		columna=2

		while(fila==2 and columna==2):
			fila=random.randint(0,4)
			columna=random.randint(0,4)

		room=self.map[fila][columna]

		print("el boss está en " + str(fila) + " : " + str(columna))

		roomType=self.roomTypeSelector()
		self.putFloor(room, roomType[0])
		self.putWalls(room, roomType[2])


		filaNueva=random.randint(0,4)
		columnaNueva=random.randint(0,4)

		while (filaNueva == fila and columnaNueva == columna):
			filaNueva=random.randint(0,4)
			columnaNueva=random.randint(0,4)

		if self.level==1:
			room[5][10][1]=-1000
		else:
			room[5][10][1]=-2000

		room=self.map[filaNueva][columnaNueva]
		print('la llave está en ' + str(filaNueva) + ' : ' + str(columnaNueva))

		room[1][1][1]=8000

		

	def putNPCs(self):
		fila=random.randint(0, 4)
		columna=random.randint(0, 4)
		print("la muerte está en "+ str(fila) + " : " + str(columna))
		room = self.map[fila][columna]

		if self.level==1:
			room[5][10][1]=-100
		else:
			room[5][10][1]=-200



	def cleanFirstRoom(self):
		room = self.map[2][2]

		self.putFloor(room, self.roomType[0])
		self.putWalls(room, self.roomType[2])



	def createRoom(self):
		#Construccion de las dimensiones que tendrá la nueva habitacion
		xDimension=random.randint(self.MINROOMSIZE[0],self.MAXROOMSIZE[0])
		yDimension=random.randint(self.MINROOMSIZE[1],self.MAXROOMSIZE[1])

		#se establece el shape del arreglo de numpy
		roomDimensions=[xDimension, yDimension, 2]

		#se crea el array de numpy de acuerdo a las especificaciones
		room=np.zeros(roomDimensions)

		roomType = self.roomTypeSelector()
		self.roomType=roomType

		self.fillRoom(room, roomType)

		self.printRoom(room)

		return room


	def fillRoom(self, room, roomType):
		self.putFloor(room, roomType[0])
		self.solidPatternDesigner(room, roomType[1])
		self.putWalls(room, roomType[2])


	def putFloor(self, room, roomType):
		if self.level==1:
			arreglo=random.choice([[[-10, -50],[0.05, 0.95]], [[-9, -50],[0.1, 0.9]], [[-8, -50],[0.1, 0.9]], [[-7, -50],[0.1, 0.9]]])
		else:
			arreglo=[[-10, -9, -8, -7, -50], [0.025, 0.025, 0.025, 0.025, 0.9]]

		floor = np.random.choice(roomType[0], p=roomType[1], size=(10, 21))
		enemys = np.random.choice(arreglo[0], p=arreglo[1], size=(10, 21))

		for j in range(10):
			for k in range(21):
				room[j][k][0] = floor[j][k]
				if self.e:
					room[j][k][1] = enemys[j][k]
				else:
					room[j][k][1] = -50



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

		#se ponen las puertas
		room[0][17]=-1
		room[0][16]=-2
		room[6][dimensions[1] - 1] = -3
		room[7][dimensions[1] - 1] = -4
		room[dimensions[0] - 1][4] = -5
		room[dimensions[0] - 1][5] = -6
		room[3][0]=-24
		room[4][0]=-25



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

			increment = 6


	def roomTypeSelector(self):
		"""
		[
			([piso],[p piso]),
			(([obstaculo primario], [muros]), [p obstaculos]),
			([paredes], [p paredes])
		]
		"""
		return random.choice(
			[
				[#azul
					([1,2],[0.8, 0.2]),
					(([3,4,1,2], [17,18,1,2]), [0.3,0.2,0.3,0.2]),
					([5,6], [0.8, 0.2])
				],
				[#oscuro
					([7,8],[0.8, 0.2]),
					(([9,10,7,8], [5,6,7,8]), [0.3,0.2,0.3,0.2]),
					([11,12], [0.8, 0.2])
				],
				[#arenizca
					([13,14],[0.8, 0.2]),
					(([15,16,13,14], [11,12,13,14]), [0.3,0.2,0.3,0.2]),
					([17,18], [0.8, 0.2])
				],
				[#nieve
					([19,20],[0.8, 0.2]),
					(([21,19,20], [24,25,20]), [0.5,0.3,0.2]),
					([22,23], [0.8, 0.2])
				]
			]
			)


	def solidShapeRandomizer(self, roomType):
		bloques=random.choice(roomType[0])
		return np.random.choice(bloques, p=roomType[1], size=(4, 4))


	def printRoom(self, room):
		dimensions=room.shape

		for i in room:
			print(i)
