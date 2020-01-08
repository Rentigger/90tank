import pygame


class Enemy(object):
    def __init__(self,enemypos,Direction,Type,blood,speed,frequency,goal):
        self.enemypos = enemypos
        self.Direction = Direction
        self.Type = Type
        self.blood=blood
        self.speed=speed
        self.frequency = frequency
        self.goal = goal
