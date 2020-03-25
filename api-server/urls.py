from apps.handlers.login import *
from apps.handlers.hypervisor import *




url = [
    (r"/login", LoginHandler),
    (r"/hypervisor", ListHypervisorHandler),
    (r"/hypervisor/(.+)", OneHypervisorHandler),
]