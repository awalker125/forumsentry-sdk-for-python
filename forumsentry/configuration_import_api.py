'''
Created on 11 Jan 2018

@author: walandre
'''
from forumsentry.api import Api
import requests
from requests.exceptions import HTTPError
from forumsentry_api.models.http_listener_policy import HttpListenerPolicy
from forumsentry.errors import InvalidTypeError
import os.path

class ConfigurationImportApi(Api):
    '''
    classdocs
    '''
    


    def __init__(self, config=None):
        '''
        Constructor
        '''
        super(ConfigurationImportApi, self).__init__(config=config)
    

    def import_fsg(self,fsg,password):
        return self._import_fsg(fsg, password)
        
        
     
     
        





