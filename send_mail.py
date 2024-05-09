import smtplib,ssl


def send_mail(message):
    global username, password, host, port

    username = "pythonwebapp2023@gmail.com"
    password = "4567ujbcr5678ujhe678-----"

    receiver = "pythonwebapp2023@gmail.com"
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    #message = "title"

    with smtplib.SMTP_SSL(host, port, context=context)as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


