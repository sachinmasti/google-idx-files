import requests 
while True:
    query = input('enter what you want to read : ')
    if not query:
        print('enter something')
        continue
    api = '16b97ae774d34dcc9208cb956c5ae275'

    url = f'https://newsapi.org/v2/top-headlines?country=us&category={query}&apiKey={api}'

    r = requests.get(url)
    print(r)

    data = r.json()

    articles  = data['articles']

    for index, article in enumerate(articles):
        print(index +1,article['title'])
        print(article['url'])
        print("⭐"*15)