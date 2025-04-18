import os
import subprocess
from typing import Any, Dict


class ZoneHandle:
    def __init__(self, zone: Dict[str, Any] = None) -> None:
        self.zone = zone
        self.path = os.path.abspath(".") + "/ansible/"

    def hosts(self) -> bool:
        # try:
        with open(self.path + "hosts", "w") as fd:
            if self.zone["target"] == "open":
                fd.write("[open]\n")
                self.format_host()
                # fd.write(self.zone["zones"][0]["ip"] + " zone_name=" + self.zone["zones"][0]["name"] + " zone_id=[" + ids +"]")
            elif self.zone["target"] == "bin":
                fd.write("[bin]\n")
                ids = ','.join([zone for zone in self.zone["zones"]])
                fd.write(self.zone["zones"][0]["ip"] + " zone_name=" + self.zone["zones"][0]["name"] + " zone_id=[" + ids +"]")
            elif self.zone["target"] == "con":
                fd.write("[con]\n")
                ids = [zone for zone in self.zone["zones"]]
                fd.write(self.zone["zones"][0]["ip"] + " zone_name=" + self.zone["zones"][0]["name"] + " zone_id=[" + ids +"]")
            else:
                fd.write("[action]\n")
                ids = [zone for zone in self.zone["zones"]]
                fd.write(self.zone["zones"][0]["ip"] + " zone_name=" + self.zone["zones"][0]["name"] + " zone_id=[" + ids +"]")
        return True
        # except Exception as e:
        #     print("create hosts file failed: ", e)
        #     return False

    def format_host(self) -> Any:
        ips = [self.zone["zones"][x].items() & self.zone["zones"][x+1].items() for x in range(len(self.zone["zones"])) if x != len(self.zone["zones"])-1]
        print(ips)

    @property
    def ansible_cmd(self) -> Any:
        if not self.hosts():
            return None
        os.chdir(self.path)
        if self.zone["target"] == "open":
            cmd = "ansible-playbook open.yaml"
        elif self.zone["target"] == "bin":
            cmd = "ansible-playbook bin.yaml"
        elif self.zone["target"] == "con":
            cmd = "ansible-playbook con.yaml"
        else:
            cmd = "ansible-playbook zone.yaml"
        p_cmd = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p_cmd.wait(timeout=360)
