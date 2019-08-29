from django_micro import configure, route, run
from django.http import HttpResponse
from django.http import HttpRequest
import csv

setting = {
    'DEBUG': True,
    'ALLOWED_HOSTS': ["127.0.0.1"],
    'LANGUAGE_CODE': 'en-us'

}
configure(setting)

buffer = open("d:/Dev/HappyCoding/L02/source.csv", "r")
r = list(csv.reader(buffer))
data = ''

for row in r:
    data += f'''
    <tr style="border-top:1pt solid #555555">
        <td><h3> {row[0]} </h3></td>
        <td><h3> {row[1]} </h3></td>
        <td><h3> {row[2]} </h3></td>
    </tr>'''




male_ad = '<image src="https://file-fsouxucwbs.now.sh" style="height:10%;margin:auto;display:block">'
female_ad = '<image src="https://file-crccldcpvg.now.sh" style="height:10%;margin:auto;display:block">'


@route('', name='home')
def homepage(request:HttpRequest):
    print(request.COOKIES)
    gender = request.COOKIES.get("gender")
    print(gender)
    if gender == "female":
        ad = female_ad
    elif gender == "male":
        ad = male_ad
    else:
        ad = 'unknown'
    html = f'''
    <div style="background-color:#0A0A0E;height:150%">
        <image src="https://file-rctyjgetlr.now.sh" style="height:70%;margin:auto;display:block">
        { ad}
        <table style="width:70%;color:white;border-collapse:collapse" align="center">
            {data}
        </table>
    </div>
    '''
    return HttpResponse(html)


application = run()
