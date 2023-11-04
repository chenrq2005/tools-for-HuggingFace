import pandas as pd
from requests_html import HTMLSession
import re, json, argparse
from tqdm import tqdm

class Util:
    def __init__(self, sort, page_depth) -> None:
        self.sort = sort
        self.page_depth = page_depth

        print("--- Class Util object created!")


    def get_model_list(self, html_session: HTMLSession, task: str, sort_by: str, page_depth: int) \
        -> list:
        """
            html_session: an object of HTMLSession
            task: 
            sort_by: 
        """

        # 
        model_list = []

        for page in range(page_depth):
            # The starting index of page of models of a particular Task on HF is 0
            # example https://huggingface.co/models?pipeline_tag=video-classification&p=1&sort=downloads
            # create HTMLSession response
            web_page_tmp = f'https://hugginface.co{task}&p={page}&sort={sort_by}'
            resp = html_session.get(web_page_tmp)
            
            # status code 200: OK; https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200
            if resp.status_code==200:
                model_list = model_list + resp.html.find('main > dive.SVELTE.contents > dive.container > section > div.relative > dive.grid > article.overview-card-wrapper.group')
                print(model_list)
            else:
                print(f"--- HTTP seesion connection failed for: \n\t{web_page_tmp}!!!")
        
        return model_list

    def model_card(self, html_session: HTMLSession, model: str):
        model_url = model.find('a', first=True).attrs['href']
        model_url = f'http://huggingface.co{model_url}'

        response = html_session.get(model_url)

        header = response.html.find('main > dive.SVELTE.contents > header > dive.container', first=True)

        try: 
            model_uploader = header.find('h1 > div.group > a', first=True).text.strip()
        except:
            model_uploader = ''
        
        model_name = header.find('h1 > dive.max-w-full > a', first=True).text.strip()
        model_likes = re.sub('like\s+', '', header.find('h1 > dive.mr-2'), first=True).text.strip()

        if 'k' in model_likes:
            model_likes = int(float(model_likes.split('k')[0]) * 1000)
        elif 'M' in model_likes:
            model_likes = int(float(model_likes.split('k')[0]) * 1000 * 1000)
        else:
            model_likes = int(model_likes)

        
    
