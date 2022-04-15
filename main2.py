import os
import argparse
from configparser import ConfigParser
from dataclasses import dataclass

config = ConfigParser()

config["data"] = {}
data = config["data"]
data["user"] = "username"
data["pass"] = "password"
data["ip"] = "127.0.0.1"

with open("config.ini", "w+") as c:
    config.write(c)

@dataclass
class Config:
    id =