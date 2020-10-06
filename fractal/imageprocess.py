#!/usr/bin/python3
import os
import numpy as np
import matplotlib.pyplot as plt
import logging

class HandleImage:
    """
        Class take responsibility for read, write to file
    """
    def __init__(self, logger):
        self.logger = logger
    

    def to_image(self, image=None, name="default.jpg"):
        self.__write_to_file(image, name)


    def __write_to_file(self, image, name):
        try:
            plt.figure()
            plt.imshow(image.T, cmap="hot")
            plt.axis("off")
            plt.imsave(name, image)
            plt.show()
            self.logger.info(f"[SUCCESS] write image to: {name}")          
        except Exception as e:
            logging.error(e)
        
