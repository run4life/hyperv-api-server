import wmi

class HypervisorClient(object):
    
    def get_wmi_client(self, server, user, password, namespace):
        conn = wmi.connect_server(server=server, user=user, password=password, namespace=namespace)
        client = wmi.WMI(wmi=conn)
        return client
    
    def _get_cpu_info(self):
        pass
    
    def _get_memory_info(self):
        pass
    
    
    def get_hypervisor_list(self):
        client = get_wmi_client("172.30.126.56", "administrator", "passw0rd#!1", r"root\virtualization\v2")
        vms_obj = client.query("select Name,ElementName,Status,EnabledState from Msvm_ComputerSystem")
        for vm in vms_obj:
            print vm