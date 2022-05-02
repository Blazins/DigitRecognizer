

from pickle import TRUE
import sys
from tokenize import Number
import fontTools
from matplotlib import testing
from matplotlib.pyplot import eventplot
from psutil import WINDOWS
import pygame
from pygame.locals import *
from keras.models import load_model
import cv2
import numpy as np

WINDOWSIZEX = 640
WINDOWSIZEY = 480


BOUNDRYINC = 5
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

#FONT = pygame.font.Font("freesanbold.tff", 18)
DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX,WINDOWSIZEY))
WHILE_INT = DISPLAYSURF.mp.rgb(WHITE)
pygame.display.set_caption("Digit Board")

iswriting = False
image_cnt = 0

PREDICT = True

number_xcord = []
number_ycord = []


while True:

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    
    if event.type == MOUSEMOTION and iswriting:
      xcord,ycord = event.pos
      pygame.draw.circle(DISPLAYSURF, WHITE,(xcord, ycord), 4, 0)

      number_xcord.append(xcord)
      number_ycord.append(ycord)

    if event.type == MOUSEBUTTONDOWN:
      iswriting = True

    if event.type == MOUSEBUTTONUP:
      iswriting = False
      number_xcord = sorted(number_xcord)
      number_ycord = sorted(number_ycord)

      rect_min_x, rect_max_x = max(number_xcord[0]-BOUNDRYINC, 0), min(WINDOWSIZEX, number_xcord[-1]+BOUNDRYINC)
      rect_min_y, rect_max_y = max(number_ycord[0]-BOUNDRYINC), min(number_ycord[-1]+BOUNDRYINC)

      number_xcord = []
      number_ycord = []

      img_arr = np.array(pygame.PixelArray(DISPLAYSURF))[rect_min_x:rect_max_y,rect_min_y:rect_max_y].T.astype(np.float32)

      if IMAGESAVE:
        cv2.imwrite("image.png")
        image_cnt +=1

      #Machine Learning Prediction
      if PREDICT:

        image = cv2.resize(img_arr,(28,28))
        image = np.pad(image,(10,10), 'constant', constant_values = 0)
        image = cv2.resize(image, (28,28))/255

        label = str(LABELS(np.argmax(MODEL.predict(image.reshape(1,28,28,1)))))

        textSurface = fontTools.render(label,True,RED,WHITE)
        textRecObj = testing.get_rect()
        textRecObj.left, textRecObj.bottom = rect_min_x, rect_max_x

        DISPLAYSURF.blit(textSurface,textRecObj)
      
      if event.type == KEYDOWN:
        if event.unicode == "n":
          DISPLAYSURF.fill(BLACK)

