# Author: Renzo Mischianti
# Website: www.mischianti.org
#
# Description:
# This script demonstrates how to use the E32 LoRa module with MicroPython.
# It includes examples of sending and receiving dictionary using both transparent and fixed transmission modes.
# The code also configures the module's address and channel for fixed transmission mode.
# Address and channel of this receiver:
# ADDH = 0x00
# ADDL = 0x01
# CHAN = 23
#
# Can be used with the send_fixed_dictionary and send_transparent_dictionary scripts
#
# Note: This code was written and tested using MicroPython on an ESP32 board.
#       It works with other boards, but you may need to change the UART pins.

from lora_e32 import LoRaE32, Configuration
from machine import UART
import utime

from lora_e32_constants import FixedTransmission
from lora_e32_operation_constant import ResponseStatusCode

# Initialize the LoRaE32 module
uart2 = UART(2)
lora = LoRaE32('433T20D', uart2, aux_pin=15, m0_pin=21, m1_pin=19)
code = lora.begin()
print("Initialization: {}", ResponseStatusCode.get_description(code))

# Set the configuration to default values and print the updated configuration to the console
# Not needed if already configured
configuration_to_set = Configuration('433T20D')
configuration_to_set.ADDL = 0x01 # Address of this receive no sender
configuration_to_set.OPTION.fixedTransmission = FixedTransmission.FIXED_TRANSMISSION
code, confSetted = lora.set_configuration(configuration_to_set)
print("Set configuration: {}", ResponseStatusCode.get_description(code))

print("Waiting for messages...")
while True:
    if lora.available() > 0:
        code, value = lora.receive_dict()
        print(ResponseStatusCode.get_description(code))
        print(value)
        print(value['key1'])
        utime.sleep_ms(2000)
