import pygame



class Map(object):
    def __init__(self,*List):
        w=[]
        for k in List:
            for i in range(k[1],k[3]+1):
                for j in range(k[0],k[2]+1):
                    w.append([[j,i],k[4]])
        self.wallplace = w

M=[Map((2,2,3,10,0),(6,2,7,10,0),(10,2,11,8,0),(14,2,15,8,0),(18,2,19,10,0),(22,2,23,10,0),(10,11,11,12,0),(14,11,15,12,0),(4,13,7,14,0),(0,13,1,13,0),(18,13,21,14,0),(24,13,25,13,0),(2,17,3,23,0),(6,17,7,23,0),(10,15,11,20,0),(12,16,13,17,0),(14,15,15,20,0),(18,17,19,23,0),(22,17,23,23,0),(11,23,14,23,0),(11,24,11,25,0),(14,24,14,25,0),(12,6,13,7,1),(0,14,1,14,1),(24,14,25,14,1),(-1,-1,26,-1,2),(-1,-2,-1,25,2),(-1,26,26,26,2),(26,-2,26,25,2),(12,24,13,25,2),(12,24,13,25,9)),
   Map((10,2,11,2,0),(8,3,17,3,0),(7,4,19,4,0),(7,5,21,5,0),(6,6,22,7,0),(5,8,7,8,0),(14,8,19,8,0),(22,8,22,9,0),(5,9,5,11,0),(16,9,19,9,0),(16,10,18,13,0),(4,12,5,13,0),(8,13,11,13,0),(4,14,19,15,0),(3,16,20,17,0),(2,18,21,18,0),(6,19,17,19,0),(8,20,15,20,0),(10,21,13,21,0),(2,20,5,21,0),(6,21,7,21,0),(18,20,21,20,0),(16,21,21,21,0),(16,22,19,22,0),(11,23,14,23,0),(11,24,11,25,0),(14,24,14,25,0),(8,10,8,11,1),(12,10,12,11,1),(0,6,1,6,1),(24,4,25,4,1),(0,24,1,25,1),(24,24,25,25,1),(0,22,1,23,3),(2,24,3,25,3),(2,0,6,1,3),(0,2,3,3,3),(0,4,1,5,3),(22,0,23,1,3),(24,2,25,3,3),(24,20,25,21,3),(22,22,25,23,3),(20,24,23,25,3),(-1,-1,26,-1,2),(-1,-2,-1,25,2),(-1,26,26,26,2),(26,-2,26,25,2),(12,24,13,25,2),(12,24,13,25,9))]


