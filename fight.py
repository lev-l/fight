# preparing
armNum = int(input('number of team1: '))
cells = int(input('cells for team1: '))
arm1Num = int(input('number of team2: '))
cells1 = int(input('cells for team2: '))
print('1:spear; 2:horse; 3:armor; 4:swords; 5:tratatanies; 6:momles; 7:grave; 8:unit; 9:Elit Swords; 10:God;')
armTy = int(input('type of team1: '))
arm1Ty = int(input('type of team2: '))

# dict of soldier's parameters
arms = {1: (4, 2, 50, 2), 2: (6, 3, 70, 5), 3: (2, 5, 80, 1), 4: (5, 2, 65, 2), 5: (5, 3, 60, 2),
		6: (6, 2, 70, 2), 7: (3, 1, 50, 2), 8: (500, 300, 3000, 1), 9: (7, 2, 65, 2),
		10: (1000000, 100000, 10000000, 10)}  # (a = damage, b = armor, c = HP)

arm = arms[armTy]
arm1 = arms[arm1Ty]

# people of war on the map
soldiers = []
# -----------------


class Soldier(object):

	def __init__(self, x, y, damage, armor, hp, speed, index, color):
		self.x = x
		self.y = y
		# params
		self.damage = damage
		self.armor = armor
		self.hp = hp
		self.speed = speed
		# previous x and y
		self.prex = self.x
		self.prey = self.y
		# soldier's index in list
		self.index = index
		self.color = color
		# number of 
		self.i = 20

	def the_enemy(self, brothers):
		way = []
		for ind, s in enumerate(brothers):

			if ind != self.index:

				if s.color != self.color and s.hp > 0:

					if s.x - self.x < 0:
						s1 = (s.x - self.x) * -1
					else:
						s1 = s.x - self.x

					if s.y - self.y < 0:
						s2 = (s.y - self.y) * -1
					else:
						s2 = s.y - self.y

					way.append((s1 + s2, ind))
		if way:
			min_way = min(way)
			return brothers[min_way[1]].x, brothers[min_way[1]].y

	def die(self, brothers):
		if self.hp == 0:
			for sold in brothers:
				if sold.index > self.index:
					sold.index -= 1
			del(brothers[self.index])
			return False
		elif self.hp < 0:
			self.hp = 0
			for sold in brothers:
				if sold.index > self.index:
					sold.index -= 1
			del(brothers[self.index])
			return False
		else:
			return True

	def foots(self, tx, ty):
		i1 = round(tx - self.x)
		if i1 < 0:
			i1 = i1 * -1

		i2 = round(ty - self.y)
		if i2 < 0:
			i2 = i2 * -1

		self.i = (i1 + i2) // self.speed
		if i < 0:
			self.i = self.i * -1

	def go_to_this(self, thx, thy):
		xP = 0
		yP = 0
		self.foots(thx, thy)

		if self.i > 0:
			xP = (thx - self.x) // self.i
			yP = (thy - self.y) // self.i

		self.prex = self.x
		self.prey = self.y
		self.x += xP
		self.y += yP
		self.stop(soldiers)
		self.i -= 1

	def stop(self, brothers):

		for ind, brother in enumerate(brothers):

			if ind != self.index and brother.hp > 0:

				if self.x + 5 > brother.x and self.y + 5 > brother.y \
						and self.x < brother.x + 5 and self.y < brother.y + 5:
					self.x = self.prex
					self.y = self.prey

					if brother.color != self.color and self.hp > 0:
						if self.damage - brother.armor <= 0:
							brother.hp -= 1
						else:
							brother.hp -= self.damage - brother.armor


# create lists of soldiers
x = 5
y = 100
i = 0
while i < armNum:
	soldiers.append(Soldier(x, y, arm[0], arm[1], arm[2], arm[3], i, (255, 0, 0)))

	if armTy == 1 and arm1Ty == 2:
		soldiers[i].damage = 12

	if y < 100 + cells * 5:
		y += 5
	else:
		x += 5
		y = 100
	i += 1

x = 955
y = 100
while i - armNum < arm1Num:
	soldiers.append(Soldier(x, y, arm1[0], arm1[1], arm1[2], arm[3], i, (0, 255, 0)))

	if arm1Ty == 1 and armTy == 2:
		soldiers[i].damage = 12

	if y < 100 + cells1 * 5:
		y += 5
	else:
		x -= 5
		y = 100
	i += 1
print("DONE!")
