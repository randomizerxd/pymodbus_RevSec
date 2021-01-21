#!/usr/bin/env python3

from pymodbus.client.sync import ModbusTcpClient
from sys import argv

temperature = int(argv[1])

client = ModbusTcpClient('127.0.0.1', port=5020)
client.connect()

hr = client.read_holding_registers(address=0x200, count=1)

client.write_register(0x200, temperature*256)
