import requests
from datetime import datetime
from json import dumps

URL = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow' #url
#solicitamos la información y guardamos la respuesta en data.
data = requests.get(URL) 
aswered= 0
noaswered= 0
minviews = 0
reputacion=0
fecha= 0
owner = 'user_id'
question_id = 0

json = data.json() #convertimos la respuesta en dict
for element in json['items']:
	#validacion de fechas
	if fecha == 0:
		fechacomp = element['creation_date']
		fecha = element['creation_date']
	if fechacomp < element['creation_date']:
		fecha =element['creation_date']
		fechacomp = fecha
		question_id = element['question_id']
	#validacion de owner
	if reputacion==0:
		repcomp = element['owner']['reputation']
		reputacion =element['owner']['reputation']
	if repcomp < element['owner']['reputation']:
		reputacion =element['owner']['reputation']
		repcomp = reputacion
		owner=element['owner']['user_id']
	#validacion de vistas
	if minviews == 0:
		minviewscomp = element['view_count']
		minviews = element['view_count']
	if minviewscomp > element['view_count']:
		minviews = element['view_count']
		minviewscomp =minviews
	if element['is_answered'] == True:
		aswered = aswered + element['answer_count']
	else:
		noaswered = noaswered + element['answer_count']

print("2-Contestadas:"+ str(aswered))
print("2-No contestadas:" + str(noaswered))
print("3-Respuesta con Menor numero de vistas:" + str(minviews))
print("4 Repuesta mas vieja:"+str(question_id))
print("5-Owner con mayor reputacion:" + str(owner) +" Con un valor de:"+ str(reputacion))

