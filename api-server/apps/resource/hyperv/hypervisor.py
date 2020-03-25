import wmi




class HypervisorClient(object):

    def get_hypervisor_list(self):
        conn = wmi.connect_server(server="172.30.126.56", user="administrator", password="passw0rd#!1", namespace=r"root\virtualization\v2")
        client = wmi.WMI(wmi=conn)
        vms_obj = client.query("select Name,ElementName,Status,EnabledState from Msvm_ComputerSystem")
        for vm in vms_obj:
            print vm