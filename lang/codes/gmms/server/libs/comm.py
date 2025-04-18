import os
import hashlib
import subprocess
from libs.config import sev_con


class Utils:
    def __init__(self) -> None:
        pass

    def _execute_cmd(self, cmd):
        try:
            p_cmd = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p_cmd.wait()
            cmd_e = str(p_cmd.stderr.read().strip(), encoding="utf-8")
            cmd_o = str(p_cmd.stdout.read().strip(), encoding="utf-8")
            return cmd_e, cmd_o
        except:
            return False, False

    def _get_md5(self, fileDir):
        md5_file = fileDir + "/md5.txt"
        if not os.path.exists(md5_file):
            return False
        with open(md5_file, "r") as fd:
            for line in fd.readlines():
                line = line.replace("\n", "").split(" ")
                remote_md5 = line[1]
                file_name = fileDir + line[0]
                if not os.path.exists(file_name):
                    continue
                if file_name == md5_file:
                    continue
                with open(file_name, "rb") as md:
                    m = hashlib.md5()
                    m.update(md.read())
                    local_md5 = m.hexdigest()
                    if remote_md5 != local_md5:
                        return False
        return True

    def _file_cp(self, src, dst):
        cmd = f"cp -rf {src}/* {dst}"
        return self._execute_cmd(cmd)

    def _svn_up(self):
        if not os.path.exists(sev_con.SVNDIR):
            self._mk_dir(sev_con.SVNDIR)
        if not os.path.exists(sev_con.SVNDIR + '/.svn'):
            cmd = f"svn --username {sev_con.SVNUSER} --password {sev_con.SVNPASS} \
                checkout {sev_con.SVNURL} {sev_con.SVNDIR} --force 1>/dev/null"
        else:
            cmd = f"svn --username {sev_con.SVNUSER} --password {sev_con.SVNPASS} \
                update {sev_con.SVNDIR} --force 1>/dev/null"
        return self._execute_cmd(cmd)

    def _svn_info(self):
        cmd =  f"svn info {sev_con.SVNDIR}"
        return self._execute_cmd(cmd)
    
    def _mk_dir(self, mkDir):
        try:
            if not os.path.exists(mkDir):
                os.makedirs(mkDir, 0o744)
            return True
        except:
            return False