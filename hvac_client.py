#!/usr/bin/env python3

from time import sleep
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1', port=5020)
client.connect()

while True:
	co = client.read_coils(address=0x100, count=8)
	hr = client.read_holding_registers(address=0x200, count=1)
	decoder = BinaryPayloadDecoder.fromRegisters(hr.registers)

	temperature = decoder.decode_8bit_int()
	heater = co.bits[0]
	cooler = co.bits[1]

	print("heater: {} | cooler: {} | temperature: {}".format(heater,cooler,temperature), end='  \r')

	if heater:
		temperature += 1
		client.write_register(0x200, (temperature)*256)
	elif cooler:
		temperature -= 1
		client.write_register(0x200, (temperature)*256)
	
	if temperature < 70:
		client.write_coil(0x100, True)
		client.write_coil(0x101, False)
	elif temperature > 70:
		client.write_coil(0x100, False)
		client.write_coil(0x101, True)
	elif temperature == 70:
		client.write_coil(0x100, False)
		client.write_coil(0x101, False)

	sleep(2)
