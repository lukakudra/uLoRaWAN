"""
This is a port of original library LoRaWAN from jeroennijhof to use pycryptodome library which is easier to install.

"""
from .PhyPayload import PhyPayload


def new(nwkey=[], appkey=[]):
    return PhyPayload(nwkey, appkey)
