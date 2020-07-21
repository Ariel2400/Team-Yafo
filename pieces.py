import pygame as pg



class Piece:
	BLACK = 0,0,0
	WHITE = 255,255,255
    
	def __init__(self, color):
		self.color = color

	def getColor(self):
		return self.color

	def draw(self, screen, x, y):
		pg.draw.circle(screen, self.getColor(), (x + 45, y - 40), 20)
		oppColor = 255-self.color[0], 255-self.color[1], 255-self.color[2]
		pg.draw.circle(screen, oppColor, (x + 45, y - 40), 20, 2)


class Stack:
	def __init__(self, x, y):
		self.items = []
		self.x = x
		self.y = y

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def getColor(self):
		return self.pop().getColor()



	def draw(self, screen):
		x = self.x
		y = self.y
		if y == 0:
			for piece in self.items:
				piece.draw(screen, x, y)
				y += 40
				
				if abs(y - self.y) > 300:
					y = 5
					x -= 5
			
		else:
			for piece in self.items:
				piece.draw(screen, x, y)
				y -= 40
			
				if abs(y - self.y) > 300:
					y = self.y - 5
					x -= 5
			
	


