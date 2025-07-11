#logging variable values

import logging
logging.basicConfig(level=logging.INFO,
                    filename='log.log',
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

x=2

logging.info(f"the value of x is {x}")
