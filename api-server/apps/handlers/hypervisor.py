
from apps.handlers.base import *
from apps.resource.hyperv.hypervisor import HypervisorClient


class ListHypervisorHandler(BaseHandler):
    #@tornado.web.authenticated
    def get(self):
        res = HypervisorClient().get_hypervisor_list()

class OneHypervisorHandler(BaseHandler):
    pass
