# -*- coding: utf-8 -*-
"""
进程管理模块
"""
import os
import re
import stat
import json
import hashlib
import subprocess

from gmcom.config import gmdcon
from gmcom.log import gmdlog

class GmProcess:
    def zone_open(self, data):
        gm_dir = gmdcon.game_dir + gmdcon.game_alias + '_' + data['serverName'] + '_' + str(data['serverId'])
        if not os.path.exists(gm_dir):
            os.makedirs(gm_dir, stat.S_IRWXU)
        ccmd = f"find {gmdcon.svn_dir} -type d |xargs chmod 700 && find {gmdcon.svn_dir} -type f |xargs chmod 600"
        if not self.execute_cmd(ccmd):
            data['status'] = 'ChmodError'
            return {'code': 201, 'message': 'chmod error!'}
        if not self.copy_file(gmdcon.svn_dir, gm_dir):
            return {'code': 201, 'message': 'copy file error!'}
        try:
            with open(gm_dir + '/config.json', 'r+') as fd:
                content = fd.read()
                fd.seek(0)
                fd.write(re.sub('zone', str(data['serverId']), content))
        except:
            return {'code': 201, 'message': 'init config error!'}
        return {'code': 200, 'message': 'open success!', 'serverName': f"{data['serverName']}", 'serverId': f"{data['serverId']}"}
        
    def zone_handle(self, data):
        gm_dir = gmdcon.game_dir + gmdcon.game_alias + '_' + data['serverName'] + '_' + str(data['serverId'])
        if data['cmd'] == 'update':
            if not self.copy_file(gmdcon.svn_dir, gm_dir):
                return {'code': 201, 'message': 'copy file error!'}
            return {'code': 200, 'message': f"update success!", 'serverName': f"{data['serverName']}", 'serverId': data['serverId']}
        else:
            cmd = f"cd {gm_dir} && sh {gmdcon.game_script} {data['cmd']} 2>/dev/null"
            result = self.execute_cmd(cmd)
            if not result:
                return {'code': 201, 'message': "操作失败", 'serverName': f"{data['serverName']}", 'serverId': data['serverId']}
            return {'code': 200, 'message': f"{result['msg']}", 'serverName': f"{data['serverName']}", 'serverId': data['serverId']}

    def execute_cmd(self, cmd):
        if cmd.find(gmdcon.game_script) < 0:
            # linux cmd
            gmdlog.writelog("执行命令:")
            try:
                p_cmd = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                p_cmd.wait(timeout=240)
                cmd_error = str(p_cmd.stderr.read().strip(), encoding='utf-8')
                # cmd_suces = str(p_cmd.stdout.read().strip(), encoding='utf-8')
                gmdlog.writelog(cmd_error)
                if cmd_error:
                    return False
                return True
            except Exception:
                return False
        if cmd.find(gmdcon.game_script) > 0:
            # linux script
            gmdlog.writelog("执行进程操作脚本")
            try:
                p_cmd = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                p_cmd.wait(timeout=240)
                cmd_suces = str(p_cmd.stdout.read().strip(), encoding='utf-8')
                if cmd_suces:
                    sct_suces = json.loads(cmd_suces)
                    gmdlog.writelog(sct_suces)
                    return sct_suces
                return False
            except Exception:
                return False

    def copy_file(self, src, dst):
        cmd = f"cp -rfuP {src}/. {dst}"
        result = self.execute_cmd(cmd)
        return result

    def check_md5(self, fileDir):
        if not os.path.exists(fileDir + '/md5.txt'): return False
        with open(fileDir + '/md5.txt') as fd:
            for line in fd.readlines():
                line = line.replace('\n', '').split(' ')
                remotemd5 = line[1]
                filename = fileDir + line[0]
                if not os.path.exists(filename): continue
                if filename == fileDir + '/md5.txt': continue
                with open(filename, 'rb') as md:
                    m = hashlib.md5()
                    m.update(md.read())
                    localmd5 = m.hexdigest()
                if remotemd5 != localmd5:
                    return False
        return True

    def bin_rsync(self, data):
        rcmd = f"sshpass -p {gmdcon.yw_pass} rsync -az {gmdcon.yw_user}@{gmdcon.yw_host}:{gmdcon.bin_path} {gmdcon.gmd_path + '/bincpp'}"
        if not self.execute_cmd(rcmd):
            return {'code': 201, 'message': 'bin rsyn to host error!'}
        if not self.check_md5(gmdcon.gmd_path + '/bincpp'):
            return {'code': 201, 'message': 'bin md5 check error!'}
        return {'code': 200, 'message': 'bin update success!'}
        
    def con_update(self, data):
        # 判断本地仓库是否存在
        if not os.path.exists(gmdcon.svn_dir + '/.svn'):
            cmd = f"svn --username {gmdcon.svn_user} --password {gmdcon.svn_pass} checkout {gmdcon.svn_url} {gmdcon.svn_dir} --force 1>/dev/null"
        else:
            cmd = f"svn --username {gmdcon.svn_user} --password {gmdcon.svn_pass} update {gmdcon.svn_dir} --force 1>/dev/null"
        if not self.execute_cmd(cmd):
            return {'code': 201, 'message': 'svn pull error!'}
        if not self.check_md5(gmdcon.svn_dir):
            return {'code': 201, 'message': 'check conf md5 error!'}
        icmd = f"svn info {gmdcon.svn_dir}"
        pcmd = subprocess.Popen(icmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pcmd.wait(180)
        cmd_suces = str(pcmd.stdout.read().strip(), encoding='utf-8')
        cmd_error = str(pcmd.stderr.read().strip(), encoding='utf-8')
        if cmd_error:
            return {'code': 201, 'msg': 'svn version check error!'}
        ret = re.findall(r"最后修改的版本: (.*)", cmd_suces)
        return {'code': 200, 'message': f"svn update success, current version:{ret[0]}"}

    def bin_update(self, data):
        gm_dir = gmdcon.game_dir + gmdcon.game_alias + '_' + data['serverName'] + '_' + str(data['serverId'])
        if not self.check_md5(gmdcon.gmd_path + '/bincpp'):
            return {'code': 201, 'message': 'check bin md5 error!'}
        if not self.copy_file(gmdcon.gmd_path + '/bincpp', gm_dir):
            data['status'] = 'CopyBinError'
            return {'code': 201, 'message': 'copy bin error!'}
        return {'code': 200, 'message': 'update bin success!', 'serverName': f"{data['serverName']}", 'serverId': data['serverId']}

gmdzon = GmProcess()
__all__ = [  gmdzon ]