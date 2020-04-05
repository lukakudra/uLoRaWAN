
"""
This is a port of library LoRaWAN to MicroPython using library crypto.

"""
from .PhyPayload import PhyPayload


def new(nwkey=[], appkey=[]):
    return PhyPayload(nwkey, appkey)
