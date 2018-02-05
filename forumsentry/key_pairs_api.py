'''
Created on 11 Jan 2018

@author: walandre
'''
from forumsentry.api import Api
from requests.exceptions import HTTPError
from forumsentry.errors import ForumHTTPError
import json
import jmespath

class KeyPairsApi(Api):
    '''
    Api for working with KeyPairs
    '''
    
    
    path = "policies/keyPairs"
    policy_type = "KeyPairs"
    
    import_path = "import"
    

    def __init__(self, config=None):
        '''
        Constructor
        '''
        super(KeyPairsApi, self).__init__(config=config)
    
    def get(self, name):
        ''' gets a KeyPairs
        :param name: The name of the KeyPairs we want to get.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: A string containing the keypair name if found or None if not
        '''
        #the api for key pairs doesnt return a model just a list.
        target_endpoint = "{0}".format(self.path)

        self._logger.debug("target_endpoint: {0}".format(target_endpoint))
        
        
        #Json being returned looks like the following
        #
        #See http://jmespath.org/tutorial.html
        #
        # {
        #   "policy": [
        #     {
        #       "name": "test1"
        #     }
        #   ]
        # }        
        
        
        
        lookup_expr = 'policy[?name==\'{0}\'].name | [0]'.format(name)
        
         
        self._logger.debug("lookup_expr: {0}".format(lookup_expr))
        
        
        try:
            # this method will be patched for unit test
            j = self._request("GET", target_endpoint)
            #print j
            self._logger.debug("json returned from {0} >>>>".format(target_endpoint))
            self._logger.debug(j)
            
            try:
                data = json.loads(j)
                return jmespath.search(lookup_expr, data)
            except Exception as e:
                self._logger.error(e)
                raise e
           
        except HTTPError as e:
            self._logger.debug(e)
            if e.response.status_code == 404:
                self._logger.warn("{0} not found".format(name))
                return None
            else:
                wrapped_error = ForumHTTPError(e)
                self._logger.error(wrapped_error)
                raise wrapped_error

    def delete(self,name):
        ''' delete a KeyPairs
        :param name: The name of the KeyPairs we want to delete.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: True/False.
        '''
        target_endpoint = "{0}/{1}".format(self.path, name)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))

        try:
            # this method will be patched for unit test
            #We dont expect any data back in a delete. If it fails we'll either get a 404 which means it doesnt exist or some other error which will be thrown up the stack.
            self._request("DELETE", target_endpoint)
            return True
           
        except HTTPError as e:
            self._logger.debug(e)
            if e.response.status_code == 404:
                self._logger.warn("{0} not found".format(name))
                return True
            else:
                wrapped_error = ForumHTTPError(e)
                self._logger.error(wrapped_error)
                raise wrapped_error

    def pkcs12(self,name, p12, p12_password, private_key_password,create_signer_group=True):
        '''
        Creates/Updates a KeyPairs on the forum sentry.
        :param name: The name of the KeyPairs we want to create/update..
        :param p12: The p12 file to upload.
        :param p12_password: The password for the p12 file
        :param private_key_password: The password for the private key
        :param create_signer_group: If we should create a signer group from the p12. Default == True
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: The KeyPairs object that was created/updated.
        '''        
        
        target_endpoint = "{0}/import/pkcs12".format(self.path)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))
        body_param = "keyAndCertificateFile"
        form_data = {}
        form_data['createSignerGroup'] = create_signer_group
        form_data['fileIntegrityPassword'] = p12_password
        form_data['password'] = private_key_password
        form_data['name'] = name
        try:
            # this method will be patched for unit test
            return self._request_file(target_endpoint, p12, form_data=form_data, download=False,body_param=body_param)
    
        except HTTPError as e:
            wrapped_error = ForumHTTPError(e)
            self._logger.error(wrapped_error)
            raise wrapped_error

    
    
    

#Exports are only supported in the gui for keypairs

#     def export(self,name,fsg,password, agent=None):
#         ''' export a task list to an fsg file
#         :param name: The name of the task list we want to export.
#         :param fsg: The file to save the export to.
#         :param password: The password to encrypt the export with.
#         :param agent: The agent to use if required
#         :raises requests.exceptions.HTTPError: When response code is not successful.
#         :returns: True/False.
#         '''
#         target_endpoint = "{0}/{1}/fsg".format(self.path, name)
#         
#         self._logger.debug("target_endpoint: {0}".format(target_endpoint))
# 
# 
#         try:
#             # this method will be patched for unit test
#             #We dont expect any data back in a delete. If it fails we'll either get a 404 which means it doesnt exist or some other error which will be thrown up the stack.
#             return self._export_fsg(target_endpoint, fsg, password,agent)
#            
#         except HTTPError as e:
#             self._logger.debug(e)
#             if e.response.status_code == 404:
#                 self._logger.warn("{0} not found".format(name))
#                 return False
#             else:
#                 wrapped_error = ForumHTTPError(e)
#                 self._logger.error(wrapped_error)
#                 raise wrapped_error
    
    def deploy(self, fsg, password):
        '''
        Imports an fsg export. This will overwrite the configuration of the object contained within the export on the forum.
        '''
        return self._import_fsg(fsg, password)
