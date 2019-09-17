#!/usr/bin/env python3

#from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1', port=5020)
client.connect()

di = client.read_discrete_inputs(address=0x000, count=8)
co = client.read_coils(address=0x100, count=8)
hr = client.read_holding_registers(address=0x200, count=4)
ir = client.read_input_registers(address=0x300, count=1)

print(di.bits)

print(co.bits)

#print(hr.registers)
decoder = BinaryPayloadDecoder.fromRegisters(hr.registers)
decoded_string = decoder.decode_string(8)
print(decoded_string)

#print(ir.registers)
decoder = BinaryPayloadDecoder.fromRegisters(ir.registers)
decoded_8bit_int = decoder.decode_8bit_int()
print(decoded_8bit_int)