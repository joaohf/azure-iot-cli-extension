# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class X509Thumbprint(Model):
    """If the device is using X.509 client certificates for authentication, at
    least one of primaryThumbprint or secondaryThumbprint must be specified.
    They can be identical.

    :param primary_thumbprint: Represents the SHA-1 hash of the X.509 client
     certificate used by the device when connecting to an IoT hub. Thumbprint
     values other than 40 hex chars are not accepted.
    :type primary_thumbprint: str
    :param secondary_thumbprint: Represents the SHA-1 hash of the X.509 client
     certificate used by the device when connecting to an IoT hub. Thumbprint
     values other than 40 hex chars are not accepted.
    :type secondary_thumbprint: str
    """

    _validation = {
        'primary_thumbprint': {'pattern': r'^([A-Fa-f0-9]{2}){20}$'},
    }

    _attribute_map = {
        'primary_thumbprint': {'key': 'primaryThumbprint', 'type': 'str'},
        'secondary_thumbprint': {'key': 'secondaryThumbprint', 'type': 'str'},
    }

    def __init__(self, primary_thumbprint=None, secondary_thumbprint=None):
        self.primary_thumbprint = primary_thumbprint
        self.secondary_thumbprint = secondary_thumbprint
