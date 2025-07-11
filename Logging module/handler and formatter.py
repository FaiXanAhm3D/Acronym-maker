import logging
logging.basicConfig(level=logging.INFO,
                    filename='customlog.log',
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger=logging.getLogger(__name__)

handler = logging.FileHandler('test.log') #this would handle the log in a new file
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #this would format the log in the new file
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("Test the custom logger")