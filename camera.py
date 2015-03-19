#coding:utf-8
import pygame
import pygame.camera
from pygame.locals import *

class camera:
    pygame.init()
    pygame.camera.init()
    cam=pygame.camera.Camera("/dev/video0",(320,240))
    li=range(1)
    cam.start()
    for i in li:
	image = cam.get_image()
	#pygame.image.save(image,str(i)+".jpg")
        pygame.image.save(image,"/home/xw/桌面/all/1.jpg")
        cam.stop()




