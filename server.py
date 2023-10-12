from flask import Flask, render_template

from weather import weather_by_city 
from python_org_news import get_python_news

'''
+ Add weather
# Flask -> Jinja2 {{ }} -> put values from Python to html (rander_template(x, y, ....))

'''

app = Flask(__name__)


@app.route('/')
def index():
    title = "News Python"
    weather = weather_by_city('Kyiv,Ukraine')
    news = get_python_news()
    return render_template('index.html', page_title=title, weather = weather, news_list=news)


if __name__=='__main__':
    # app.run()
    app.run(debug=True)