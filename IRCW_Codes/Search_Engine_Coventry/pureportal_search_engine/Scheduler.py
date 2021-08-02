import scrapy
from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler


def Latest():
    print('Checking for any latest data')
    os.system('scrapy crawl Cov_Research_Papers_JSON -o Crawler_bs4/Crawler_Paper/Final_Cov_Research_Paper.json')


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(Latest, 'interval', days=7)
    scheduler.start()
