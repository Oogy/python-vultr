'''Partial class to handle Vultr Firewall API calls'''
from .utils import VultrBase


class VultrFirewall(VultrBase):
    '''Handles Vultr Firewall API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def group_list(self, params=None):
        ''' /v1/firewall/group_list
        GET - account
        List all firewall groups on the current account.

        Link: https://www.vultr.com/api/#firewall_group_list
        '''
        params = params if params else dict()
        return self.request('/v1/firewall/group_list', params, 'GET')
    
    ''' 
    def group_create(self, description, params=None)
         #create firewall group $description 
         
         params = update_params(params, {'DESCRIPTION': description})
         return self.request('/v1/firewall/group_create', params, 'POST')
    '''
        
    ''' 
    def group_delete(self, firewallgroupid, params=None)
         #delete $firewallgroup
         
         params = update_params(params, {'FIREWALLGROUPID': firewallgroupid})
         return self.request('/v1/firewall/', params, 'POST')
    '''
    
    '''
    def rule_(self, , params=None)
        
        params = update_params(params, {})
        return self.request('v1/firewall/rule_', params, 'POST')
    '''
    
    '''
    def rule_(self, , params=None)
        
        params = update_params(params, {})
        return self.request('v1/firewall/rule_', params, 'POST')
    '''
        
    '''
    def rule_(self, , params=None)
        
        params = update_params(params, {})
        return self.request('v1/firewall/rule_', params, 'POST')
    '''
    
    
