import pandas as pd
from requests_html import HTMLSession
import re, json, argparse
from tqdm import tqdm

class Util():
    def __init__(self) -> None:
        pass
        
    @classmethod
    def get_model_list(html_session, task_dictionary: dict, sort_by: str) \
        -> list:
        """
            html_session: an object of HTMLSession
            task_dirctionary: 
            sort_by: 

        """

        # create HTMLSession response
        resp = html_session.get(f'https://hugginface.co{task_dictionary["href"]}&sort={sort_by}')

        # 
        model_list = []

        if resp.status_code==200:
            model_list = resp.html.find()
            print(model_list)
            return model_list
        else:
            print("--- HTTP seesion connection failed!!!")
    
