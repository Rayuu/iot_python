import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()
cam=pygame.camera.Camera("/dev/video1",(300,200))
li=range(2)



for i in li:
	cam.start()
	image = cam.get_image()
	pygame.image.save(image,str(i)+".jpg")
	cam.stop()




