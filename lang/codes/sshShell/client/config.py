#!/usr/bin/python2.7
import sys
import json
import codecs

def modify_key(dictionary, chan_name, server_id):
    if dictionary.has_key('ServerName'):
        dictionary['ServerName'] = chan_name
        return dictionary
    for k, v in dictionary.items():
        if isinstance(v, dict) and v.has_key('ServerId'):
            v['ServerId'] = server_id
            return modify_key(v, chan_name, server_id), v, k


def modify_config(filename, agent, server_id):
    with codecs.open(filename, 'r', encoding='utf8') as fd:
        file_dict = json.load(fd)
    
    result = modify_key(file_dict, agent, server_id)
    if isinstance(result, tuple):
        file_dict[result[2]] = result[1]
    file_dict = file_dict
    
    with codecs.open(filename, 'w', encoding='utf8') as fd:
        json_str = json.dumps(file_dict, indent=2, ensure_ascii=False)
        fd.write(json_str)


if __name__ == '__main__':
    agent = sys.argv[1]
    server_id = sys.argv[2]
    config_file = './config.json'
    server_file = './conf/ServerSetup.json'
    modify_config(config_file, agent, server_id)

