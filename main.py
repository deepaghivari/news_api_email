import requests


api_key = "fc178f995abc40909f0ccccea075f732"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-07-22&sortBy=publishedAt&" \
      "apiKey=fc178f995abc40909f0ccccea075f732"

# Make request
request=requests.get(url)

# Get a dictionary with data
content=request.json()


# Access the article titles and description
for article in content["articles"]:
    print(article['title'])
    print(article['description'])


