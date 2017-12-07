import forumsentry_api
import sys

import logging
import os
import platform
import datetime
import time
from forumsentry.api import Api
from forumsentry.config import Config



def main():
    
    start = time.time()
   
    this = os.path.splitext(os.path.basename(__file__))[0]
    
    whereami = os.path.dirname(__file__)  

    this_platform = platform.system()

    log_location = "/var/tmp"
    
    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    
    if this_platform == "Windows":
        log_location = "C:\\" + log_location
    
    if whereami == ".":
        whereami = os.getcwd()
    
    setupLogging(log_location, this, now, True)

    logging.info(this)    
    
    config = Config()
    
    config.host = "forumsentry-dev"
    config.port = 8081
    config.username = "admin"
    config.password = "password"
    config.protocol = "http"
    
    fs = Api(config=config)
    
    
    logging.info(fs.config.protocol)
    logging.info(fs.config.forumsentry_url)
    logging.info(fs.config.basic_authentication_header)
   # fs.testHarness()
    
    copy = fs.getForumSentryPolicy("httpListenerPolicies", "bob")
    
    copy.use_basic_authentication = True
    copy.name = "bill"
    
    fs.createForumSentryPolicy("httpListenerPolicies", "bill", copy)

    end = time.time()
    elapse = end - start

def setupLogging(log_location, this, now, verbose):

    
        # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                    #format='%(asctime)s %(name)-12s %(levelname)-8s (%(threadName)-10s) %(message)s',
                    format='%(asctime)s %(levelname)-8s (%(threadName)-10s) %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=log_location + '/' + this.upper() + "_" + now +'.txt',
                    filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    if verbose:
        console.setLevel(logging.DEBUG)
        
  
        
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(levelname)-8s (%(threadName)-10s) %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    # Now, we can log to the root logger, or any other logger. First the root...
    logging.debug('logging initialised')
    
    logging.debug("debug is on")


if __name__ == '__main__':
 main()