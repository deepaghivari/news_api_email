import requests
from send_mail import send_mail




api_key = "enter api_key"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-07-22&sortBy=publishedAt&" \
      "apiKey=fc178f995abc40909f0ccccea075f732"

# Make request
request=requests.get(url)

# Get a dictionary with data
content=request.json()


message = ""                                                                         #message should be str bcz only string type is sent via mail
# Access the article titles and description
for article in content["articles"]:
    if article['title'] is not None:
        message=message+article['title']+"\n"+article['description']+"2*\n"


message=message.encode("utf-8")

send_mail(message)


