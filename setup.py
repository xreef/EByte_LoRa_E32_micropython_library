import sys
sys.path.pop(0)
from setuptools import setup

setup(
    name="micropython-lora-e32",
    py_modules=["lora_e32", "lora_e32_constants", "lora_e32_operation_constant"],
    version="0.0.1",
    description="Ebyte E32 LoRa micropython library device very cheap and very long range (from 3Km to 8Km). Arduino LoRa EBYTE E32 device library complete and tested with Arduino, esp8266, esp32, STM32 and Raspberry Pi Pico. sx1278/sx1276.",
    long_description="Ebyte E32 LoRa micropython library device very cheap and very long range (from 3Km to 8Km). Arduino LoRa EBYTE E32 device library complete and tested with Arduino, esp8266, esp32, STM32 and Raspberry Pi Pico. sx1278/sx1276.",
    keywords="LoRa, UART, EByte, e32, esp32, esp8266, stm32, SAMD, Arduino, Raspberry Pi Pico, MicroPython",
    url="https://github.com/xreef/EByte_LoRa_E32_micropython_library",
    author="Renzo Mischianti",
    author_email="renzo.mischianti@gmail.com",
    maintainer="Renzo Mischianti",
    maintainer_email="renzo.mischianti@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: Stable",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)