#custom loggers

import logging
logging.basicConfig(level=logging.INFO,
                    filename='customlog.log',
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__) #by convention
logger.info("Test the custom logger")