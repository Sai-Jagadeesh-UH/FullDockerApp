import sys
import os
import logging
from datetime import datetime


Log_Dir = os.path.join(os.getcwd(), "logFiles",
                       datetime.today().strftime("%m_%d_%Y"))
os.makedirs(Log_Dir, exist_ok=True)
File_name = datetime.now().strftime("%m_%d_%Y_%H")


logger_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]+"_Logger"

# logger creation
logger = logging.getLogger(logger_name)
logger.setLevel(logging.INFO)

# Handler creation
lh = logging.FileHandler(os.path.join(
    Log_Dir, File_name+".log"), mode='a')
lh.setLevel(logging.INFO)

# formatter creation
lf = logging.Formatter(
    fmt="%(asctime)s : %(name)s \n%(levelname)s : %(message)s \n")

# adding formatter to handler
lh.setFormatter(lf)

# adding handler to logger
logger.addHandler(lh)

if __name__ == '__main__':
    logging.info("starting logging")
