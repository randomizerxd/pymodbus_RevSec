#!/usr/bin/env python3

from pymodbus.server.sync import StartTcpServer
#from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

#builder_di = BinaryPayloadBuilder()
#builder_di.add_bits([1,1,1,1,1,1,1,1])

# [heater,cooler,...]
builder_co = BinaryPayloadBuilder()
builder_co.add_bits([0,0,0,0,0,0,0,0])

# temperature
builder_hr = BinaryPayloadBuilder()
builder_hr.add_8bit_int(70)

# wanted to use input registers for temperature, but they are read only
#builder_ir = BinaryPayloadBuilder()
#builder_ir.add_8bit_int(70)

#di_block = ModbusSequentialDataBlock(0x01, builder_di.to_coils())
co_block = ModbusSequentialDataBlock(0x101, builder_co.to_coils())
hr_block = ModbusSequentialDataBlock(0x201, builder_hr.to_registers())
#ir_block = ModbusSequentialDataBlock(0x301, builder_ir.to_registers())

#store = ModbusSlaveContext(di=di_block, co=co_block, hr=hr_block, ir=ir_block)
store = ModbusSlaveContext(co=co_block, hr=hr_block)
context = ModbusServerContext(slaves=store, single=True)

identity = ModbusDeviceIdentification()
identity.VendorName = 'Pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'Pymodbus Server'
identity.ModelName = 'Pymodbus Server'
identity.MajorMinorRevision = '2.2.0'

address = ("localhost", 5020)
print("Server started at {}".format(address))
StartTcpServer(context, identity=identity, address=address)
