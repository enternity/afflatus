#!/usr/bin/python3

import sys
import logging
from fractal import FractalGeometry
from imageprocess import HandleImage

def set_up_logger():
    logger = logging.getLogger('')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('my_log_info.log')
    sh = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger

def main():
    logger = set_up_logger()
    logger.info("Started")
    #handleimage = HandleImage("./duc-dep-trai.jpg", logger)
    #logging.info(f"Path image {handleimage.get_path()}")
    fractal = FractalGeometry(logger)
    #fractal.mandelbrotset(rows=1000, cols=1000, iters=150)
    fractal.julia(1000, 1000, 150, -0.42, 0.6)
    logger.info("Stopped")


if __name__ == "__main__":
    main()