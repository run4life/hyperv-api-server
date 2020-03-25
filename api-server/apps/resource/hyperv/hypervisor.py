import wmi

class HypervisorClient(object):
    
    def get_wmi_client(self, server, user, password):
#        if namespace:
#            conn = wmi.connect_server(server=server, user=user, password=password, namespace=namespace)
#        else:
        conn = wmi.connect_server(server=server, user=user, password=password)
        client = wmi.WMI(wmi=conn) 
        return client
    
    def _get_cpu_info(self,client):
#        cpus = client.query(
#            "SELECT Architecture, Name, Manufacturer, MaxClockSpeed, "
#            "NumberOfCores, NumberOfLogicalProcessors FROM Win32_Processor "
#            "WHERE ProcessorType = 3")
        cpus = client.Win32_Processor()
        cpus_list = []
        for cpu in cpus:
            cpu_info = {'Architecture': cpu.Architecture,
                        'Name': cpu.Name,
                        'Manufacturer': cpu.Manufacturer,
                        'MaxClockSpeed': cpu.MaxClockSpeed,
                        'NumberOfCores': cpu.NumberOfCores,
                        'NumberOfLogicalProcessors':
                        cpu.NumberOfLogicalProcessors}
            cpus_list.append(cpu_info)
        print cpus_list
    
    def _get_memory_info(self, client):

        mems = client.query("SELECT TotalVisibleMemorySize, "
                                          "FreePhysicalMemory "
                                          "FROM win32_operatingsystem")[0]
        mems_list = []
        
        mem_info = {'TotalVisibleMemorySize': mem_info.TotalVisibleMemorySize,
                    'FreePhysicalMemory': mem_info.FreePhysicalMemory}
        return mem_info
    
    def get_hypervisor_list(self):
#        client = self.get_wmi_client("172.30.126.56", "administrator", "passw0rd#!1", r"root\virtualization\v2")
#        vms_obj = client.query("select Name,ElementName,Status,EnabledState from Msvm_ComputerSystem")
#        for vm in vms_obj:
#            print vm
        client = self.get_wmi_client("172.30.126.56", "administrator", "passw0rd#!1")
        cpu = self._get_cpu_info(client)
        print cpu
        memory = self._get_memory_info(client)
        print memory