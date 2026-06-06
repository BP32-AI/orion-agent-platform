# app/common/enums.py
from enum import Enum


class ChannelType(str, Enum):
    TELEGRAM = "telegram"
    WEB = "web"
    API = "api"