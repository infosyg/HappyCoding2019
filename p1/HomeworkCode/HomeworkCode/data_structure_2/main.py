from django_micro import configure, route, run
from django.http import HttpResponse
import csv

setting = {
    "DEBUG": True,
    "LANGUAGE_CODE": 'en-us'
}
configure(setting)

source = "APR 13, PNC ARENA, RALEIGH,NC/APR 7, STATE FARM ARENA, ATLANTA,GA/APR 9, BRIDGESTONE ARENA, NASHVILLE,TN/APR 11, AMALIE ARENA, TAMPA,FL"

table  = []
for e in source.split("/"):
    table.append(e.split(", "))

data = ''
for row in table:
    data += f'''
    <tr style="border-top:1pt solid #555555">
        <td><h3> { row[0] } </h3></td>
        <td><h3> { row[1] } </h3></td>
        <td><h3> { row[2] } </h3></td>
    </tr>'''

for e in source.split("/"):
    table.append(e.split(", "))

@route('', name='home')
def homepage(request):
    html = f'''
    <div style="background-color:#0A0A0E;height:100%">
        <image src="https://file-rctyjgetlr.now.sh" style="height:70%;margin:auto;display:block">
        <table style="width:60%;color:white;border-collapse:collapse" align="center">
            { data }
        </table>
    </div>'''
    return HttpResponse(html)


application = run()