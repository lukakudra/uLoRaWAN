# LoRaWAN
This is a LoRaWAN v1.0 re-implementation in MicroPython.

Replaces original use of library Crypto on Raspberry PI by ucryptolib available in MicroPython.

Updated code will come anytime soon, currently tested on ESP32 and ESP8266 will follow.

# LoRa
TODO test also LoRa library...

## Example
```
import uLoRaWAN
from uLoRaWAN.MHDR import MHDR

# Init
devaddr = [0x26, 0x01, 0x11, 0x5F]
nwskey = [0xC3, 0x24, 0x64, 0x98, 0xDE, 0x56, 0x5D, 0x8C, 0x55, 0x88, 0x7C, 0x05, 0x86, 0xF9, 0x82, 0x26]
appskey = [0x15, 0xF6, 0xF4, 0xD4, 0x2A, 0x95, 0xB0, 0x97, 0x53, 0x27, 0xB7, 0xC1, 0x45, 0x6E, 0xC5, 0x45]

lorawan = uLoRaWAN.new(nwskey, appskey)

# Create LoRaWAN packet
lorawan.create(MHDR.UNCONF_DATA_UP, {'devaddr': devaddr, 'fcnt': 1, 'data': list(map(ord, 'Python rules!')) })

payload = lorawan.to_raw()
print(payload)

# Read LoRaWAN packet
lorawan.read(payload)
print(lorawan.valid_mic())
print("".join(list(map(chr, lorawan.get_payload()))))

```


It uses https://github.com/mayeranalytics/pySX127x and it's currently being tested with a RFM95 attached to a Raspberry PI.
See: https://www.lora-alliance.org/portals/0/specs/LoRaWAN%20Specification%201R0.pdf

# Special thanks
Thanks for nice implementation of LoRaWAN stack by jeroennijhof, which was more or less straightforward to reimplement to pure MicroPython.
