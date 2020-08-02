from nose2.tools import *
from fight_V_1a7 import Soldier


def test_stop():
	sold = Soldier(50, 50, 5, 5, 5, 5, 5, (5, 5, 5))
	sold1 = Soldier(54, 53, 5, 5, 5, 5, 5, (5, 5, 5))
	sold.prex = 49
	sold.prey = 48
	sold.stop([sold1])
	assert sold.x == sold.prex and sold.y == sold.prey
	sold.prex = 50
	sold.prey = 50
	sold.stop([sold1])
	assert sold.x != sold.prex and sold.y != sold.prey


def test_foots():
	sold = Soldier(50, 50, 5, 5, 5, 5, 5, (5, 5, 5))
	x = 50
	y = 25
	assert sold.speed == 5
	sold.foots(x, y)
	assert sold.i == 5
	x = 30
	y = 30
	sold.foots(x, y)
	assert sold.i == 8
	x = 70
	y = 30
	sold.foots(x, y)
	assert sold.i == 8


def test_die():
	sold = Soldier(50, 50, 5, 5, 5, 5, 1, (5, 5, 5))
	sold1 = Soldier(50, 50, 5, 5, 5, 5, 2, (5, 5, 5))
	sold2 = Soldier(50, 50, 5, 5, 5, 5, 0, (5, 5, 5))
	assert sold.die([sold1, sold, sold2])
	sold.hp = 0
	brothers = [sold1, sold, sold2]
	assert not sold.die(brothers) and sold1.index == 1 and sold2.index == 0
	assert brothers == [sold1, sold2]
	sold1.hp = -1
	assert not sold1.die([sold1, sold2])


def test_go_to_this():
	sold = Soldier(50, 50, 5, 5, 5, 5, 5, (5, 5, 5))
	x = 50
	y = 60
	sold.go_to_this(x, y)
	assert sold.y == 55
	x = 55
	y = 60
	sold.go_to_this(x, y)
	assert sold.y == 57 and sold.x == 52


def test_the_enemy():
	sold = Soldier(50, 50, 5, 5, 5, 5, 5, (5, 5, 5))
	sold1 = Soldier(50, 25, 5, 5, 5, 5, 5, (5, 5, 5))
	sold2 = Soldier(76, 50, 5, 5, 5, 5, 5, (5, 5, 5))
	sold3 = Soldier(49, 50, 5, 5, 5, 5, 5, (5, 5, 5))
	mins = sold.the_enemy([sold1, sold2, sold3])
	assert not mins
	sold1.color = (20, 20, 20)
	sold2.color = (20, 20, 20)
	sold3.color = (20, 20, 20)
	x, y = sold.the_enemy([sold1, sold2, sold3])
	assert x == 49 and y == 50
