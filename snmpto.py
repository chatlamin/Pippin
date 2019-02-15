#!/usr/bin/env python

import ecks3
import os
import yaml

with open(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'snmpto.yml', 'r') as yml_file:
    config = yaml.load(yml_file)

snmp_engine = ecks3.Ecks()

for device_config in config['devices']:
    drv = device_config['driver']
    community = device_config['community']
    ip = device_config['switches_ip']
    result = []
    oid = tuple(map(int, device_config['oid'].split('.')))
    if drv == 'dgs-1210':
        with open(ip) as f:
            for line in f:
                print(line)
                ip = line.strip()
                data = snmp_engine.get_snmp_data(ip, 161, community, oid)
                print(data[1][2])
    if drv == 'dgs-3120':
        with open(ip) as f:
            for line in f:
                print(line)
                ip = line.strip()
                data = snmp_engine.get_snmp_data(ip, 161, community, oid)
                print(data[4][2])

