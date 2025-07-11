import logging
#configuring out log

logging.basicConfig(level=logging.DEBUG,
                    filename='log.log',
                    filemode='w',
                    format="%(asctime)s - %(levelname)s - %(message)s")
#this specifies from which level the output would come and would store the logging output in the file log.log
#here we have done formatting of the output
#also this line would be run only once hence it should be written at the beggining of your code

#there are different levels of logging

logging.debug("debug") #lvl 1
logging.info ("info") #lvl 2
logging.warning("warning") #lvl 3
logging.error("error") #lvl 4
logging.critical("critical") #lvl 5

#by default anything above or equal lvl 3 to lvl will give output



