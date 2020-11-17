import os
from pprint import pprint

from dotenv import load_dotenv
from geoip2.database import Reader

load_dotenv()

IP = os.getenv("IP", "216.58.212.142")

with Reader("data/GeoLite2-ASN.mmdb") as reader:
    res = reader.asn(IP)
    pprint(res.autonomous_system_organization)
