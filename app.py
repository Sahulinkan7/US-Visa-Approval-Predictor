import sys
from us_visa_src.exception import USvisaException
from us_visa_src.logger import logging

try:
    logging.info("welcome to app")
    print(1/0)
    
except Exception as e:
    logging.info(USvisaException(e,sys))
    raise USvisaException(e,sys)