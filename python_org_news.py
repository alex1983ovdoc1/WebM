import requests
from bs4 import BeautifulSoup


def get_html(url):
	try:
		result = requests.get(url)
		result.raise_for_status() # answer server
		return result.text
	# requests.RequestException 	- network problem
	# ValueError 					- server problem
	except(requests.RequestException, ValueError):
		print('-- NETWORK ERROR -- (python_org_new.py)')
		return False

def get_python_news():
	html = get_html('https://www.python.org/blogs/')

	if html:
		soup = BeautifulSoup(html, 'html.parser')
		all_news = soup.find('ul', class_="list-recent-posts menu").findAll('li')
		# print(all_news)	
		result_news =[]
		for news in all_news:
			title = news.find('a').text
			# print(title)
			url = news.find('a')['href']
			published = news.find('time').text
			# print(title)
			# print(url)
			# print(published)
			result_news.append({
					'title': title,
					'url': url,
					'published': published
					})
		return result_news
	return False


# if __name__ == '__main__':
	
# 	if html:
# 		# with open("python.org.html", "w", encoding='utf8') as f:
# 		# 	f.write(html)
# 		news = get_python_news()
# 		print(news)
