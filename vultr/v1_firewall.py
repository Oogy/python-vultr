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

    def rule_create(self, fireallgroupid, direction, ip_type, protocol, subnet, subnet_size, port, notes, params=None)
	'''/v1/firewall/rule_create
        POST - account
        Create a rule in a firewall group.

        https://www.vultr.com/api/#firewall_rule_create
	'''
        params = update_params(params, {
            'FIREWALLGROUPID': fireallgroupid,
            'direction': direction,
            'ip_type': ip_type,
            'protocol': protocol,
            'subnet': subnet,
            'subnet_size': subnet_size,
            'port': port,
            'notes': notes
        })
        return self.request('v1/firewall/rule_create', params, 'POST')

    def rule_delete(self, firewallgroupid, rulenumber, params=None)
	'''/v1/firewall/rule_delete
        POST - account
        Delete a rule in a firewall group.

        Link: https://www.vultr.com/api/#firewall_rule_delete
	'''
        params = update_params(params, {
            'FIREWALLGROUPID': firewallgroupid,
            'rulenumber': rulenumber
        })
        return self.request('v1/firewall/rule_delete', params, 'POST')

    def rule_list(self, firewallgroupid, direction, ip_type, params=None)
	'''/v1/firewall/rule_list
        GET - account
        List the rules in a firewall group.

        Link: https://www.vultr.com/api/#firewall_rule_delete
	'''
        params = update_params(params, {
            'FIREWALLGROUPID': firewallgroupid,
            'direction': direction,
            'ip_type': ip_type
        })
        return self.request('v1/firewall/rule_list', params, 'GET')


