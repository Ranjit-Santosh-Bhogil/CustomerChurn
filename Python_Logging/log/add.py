from logger import logging 

def add(a,b):
    logging.debug("adding of numbers {} and {}".format(a,b))
    return a+b;

logging.info("Addition of 2 and 3 is: {}".format(add(2,3)))
add(2,3);