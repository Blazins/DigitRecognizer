

import sys
from psutil import WINDOWS
import pygame
from pygame.locals import *
from keras.models import load_model
import cv2

WINDOWSIZEX = 640
WINDOWSIZEY = 480

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

IMAGESAVE = False

MODEL = load_model("bestmodel.h5")

LABELS = {0:"Zero", 1:"One",
          2:"Two", 3:"Three",
          4:"Four", 5:"Five",
          6:"Six", 7: "Seven",
          8:"Eight", 9:"Nine",}

#Initialize pygame
pygame.init()

FONT = pygame.font.Font("freesanbold.tff", 18)
pygame.display.set_mode((WINDOWSIZEX,WINDOWSIZEY))
WHILE_INT = DISPLAYSURF.mp.rgb(WHITE)
pygame.display.set_caption("Digit Board")

while True:

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    
    if event.type == MOUSEMOTION and iswriting:
      xcord,ycord = event.pos
      pygame.draw.circle(DISPLAYSURF, WHITE,(xcord, ycord), 4, 0)