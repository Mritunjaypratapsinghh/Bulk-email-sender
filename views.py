from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import smtplib

def homne(request):
    return render(request,'home.html')

def bes(request):
    email=request.POST[file]

    e = pd.read_excel(email)
    emails = e[email].values
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("bulkemailsender2022@gmail.com", "bulkemailsender")
    msg = "Hello this is a email form python"
    subject = "Hello world"
    body = "Subject: {}\n\n{}".format(subject, msg)
    for email in emails:
        server.sendmail("bulkemailsender2022@gmail.com", email, body)
    server.quit()
    return render(request,'result.html')