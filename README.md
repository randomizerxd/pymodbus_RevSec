# HVAC system

Usage:
1. `./hvac_server.py`
2. `./hvac_client.py`
3. `./set_temp.py <temp>`

Inputs:
- temperature

Outputs: 
- heater
- cooler

Logic:
- if heater is on, then increase temp by 1
- elif cooler is on, then decrease temp by 1
- if temp < 70, then turn heater on
- elif temp > 70, then turn cooler on
