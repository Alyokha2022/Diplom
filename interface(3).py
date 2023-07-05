import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from config import comunity_token, access_token, db_url_object
from core import VkTools
from data_store import add_user, check_user
from sqlalchemy import create_engine

class BotInterface:
    def __init__(self, comunity_token, acces_token):
        self.interface = vk_api.VkApi(token=comunity_token)
        self.vk_tools = VkTools(access_token)
        self.api = VkTools(acces_token)
        self.params = None
        self.worksheets = []
        self.offset = 0
      
