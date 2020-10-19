from flask import render_template
from app import main

#Views 
@main.route('/')
def index():
    '''
    Views thats renders news sources to the home page and its data
    '''
    daily_news = get_sources('general')
    business_news = get_sources('business')
    sport_news = get_sources('sports')
    
    return render_template('index.html',general = daily_news,business=business_news,sports=sport_news)
