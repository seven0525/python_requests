import requests

# GETリクエスト
url = 'https://apiv2.twitcasting.tv/internships/2019/games?level=1'
headers = {
    "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjRjYzA1NzI5NzZkYmVmYjUwMGFhNmZhZDYxYTljNTY0Mzk1YjY1ZWJjMDU2OGY1NjY2NjNhYTEwNTI2NmU2YWJlM2FjOGRlZjgyZGY5MTAyIn0.eyJhdWQiOiIxODIyMjQ5MzguMjNhNzJmNDA2NzI4M2I0OWY5NjZmOTMyMzViMTg2NDQzN2VjNWY2YTlmY2M5NjVlOGIzOTM5MGRmNWQ2YWE5NCIsImp0aSI6IjRjYzA1NzI5NzZkYmVmYjUwMGFhNmZhZDYxYTljNTY0Mzk1YjY1ZWJjMDU2OGY1NjY2NjNhYTEwNTI2NmU2YWJlM2FjOGRlZjgyZGY5MTAyIiwiaWF0IjoxNTYyMzkxNjI2LCJuYmYiOjE1NjIzOTE2MjYsImV4cCI6MTU3Nzk0MzYyNiwic3ViIjoiOTkxMTc4MDIxMDI0MzE3NDQwIiwic2NvcGVzIjpbInJlYWQiXX0.RBTtwqnDLHrtv1sJzaAzvoJ82xhfSVXOjeR-LgWNyuY77jDE6LfsgSZDY2261eZ4vkG7JyOTxDRHBga-0ES5Yd6P2DHa05DCwZgsm_ZvDRcxx24SPe-y_8yTvvvfoKn15OJ0NfZRZAhnv6x2o0IobAKEp7oElLkaclqq1QH8zYi_Ob1UcOB4z0uZs6_2TsYCrTTfx26gCjs1-MgYPBI1_-zDKWHfMBDtZso1P8cTLhTPUCc_7ESc0aAAT1zeI2qHMYc124lf3WWSCicV0pxNZ4BeaUcuxzFLmIdmy8wVZ15h-2YTRHOcM2tkgDVJfLnoYjh6Izx_UpVYfiZ7kzdAZw"}
response = requests.get(url, headers=headers)

question_results = response.content
aaa = question_results.decode('utf-8')

#idとquestion部分の抽出 
table = aaa.maketrans({
    '"': '', #左が置換したい文字、右が新しい文字。
    "'": '', #左が置換したい文字、右が新しい文字。
    "{": '',
    "}": '',
})
aaa = question_results.decode('utf-8')
b = aaa.translate(table)
bb = b.split(",")
id_number = bb[0].split(":")[1]
question = bb[1].split(":")[1]


# 四則演算のパターンを考える
newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in question)
listOfNumbers = [float(i) for i in newstr.split()]

if listOfNumbers[0] + listOfNumbers[1] + listOfNumbers[2] == listOfNumbers[-1]:
    answer = "++"
elif listOfNumbers[0] + listOfNumbers[1] - listOfNumbers[2] == listOfNumbers[-1]:
    answer = "+-"
elif listOfNumbers[0] + listOfNumbers[1] * listOfNumbers[2] == listOfNumbers[-1]:
    answer = "+*"
elif listOfNumbers[0] + listOfNumbers[1] / listOfNumbers[2] == listOfNumbers[-1]:
    answer = "+/"
    
elif listOfNumbers[0] - listOfNumbers[1] - listOfNumbers[2] == listOfNumbers[-1]:
    answer = "--"
elif listOfNumbers[0] - listOfNumbers[1] + listOfNumbers[2] == listOfNumbers[-1]:
    answer = "-+"
elif listOfNumbers[0] - listOfNumbers[1] * listOfNumbers[2] == listOfNumbers[-1]:
    answer = "-*"
elif listOfNumbers[0] - listOfNumbers[1] / listOfNumbers[2] == listOfNumbers[-1]:
    answer = "-/"

elif listOfNumbers[0] * listOfNumbers[1] - listOfNumbers[2] == listOfNumbers[-1]:
    answer = "*-"
elif listOfNumbers[0] * listOfNumbers[1] + listOfNumbers[2] == listOfNumbers[-1]:
    answer = "*+"
elif listOfNumbers[0] * listOfNumbers[1] * listOfNumbers[2] == listOfNumbers[-1]:
    answer = "**"
elif listOfNumbers[0] * listOfNumbers[1] / listOfNumbers[2] == listOfNumbers[-1]:
    answer = "*/"
    
elif listOfNumbers[0] / listOfNumbers[1] - listOfNumbers[2] == listOfNumbers[-1]:
    answer = "/-"
elif listOfNumbers[0] / listOfNumbers[1] + listOfNumbers[2] == listOfNumbers[-1]:
    answer = "/+"
elif listOfNumbers[0] / listOfNumbers[1] * listOfNumbers[2] == listOfNumbers[-1]:
    answer = "/*"
elif listOfNumbers[0] / listOfNumbers[1] / listOfNumbers[2] == listOfNumbers[-1]:
    answer = "//"


# POSTする
import json
import urllib.request

url = f'https://apiv2.twitcasting.tv/internships/2019/games/{id_number}'
data = {
    "answer":f"{answer}",
}
headers = {
    'Content-Type': 'application/json',
    "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjRjYzA1NzI5NzZkYmVmYjUwMGFhNmZhZDYxYTljNTY0Mzk1YjY1ZWJjMDU2OGY1NjY2NjNhYTEwNTI2NmU2YWJlM2FjOGRlZjgyZGY5MTAyIn0.eyJhdWQiOiIxODIyMjQ5MzguMjNhNzJmNDA2NzI4M2I0OWY5NjZmOTMyMzViMTg2NDQzN2VjNWY2YTlmY2M5NjVlOGIzOTM5MGRmNWQ2YWE5NCIsImp0aSI6IjRjYzA1NzI5NzZkYmVmYjUwMGFhNmZhZDYxYTljNTY0Mzk1YjY1ZWJjMDU2OGY1NjY2NjNhYTEwNTI2NmU2YWJlM2FjOGRlZjgyZGY5MTAyIiwiaWF0IjoxNTYyMzkxNjI2LCJuYmYiOjE1NjIzOTE2MjYsImV4cCI6MTU3Nzk0MzYyNiwic3ViIjoiOTkxMTc4MDIxMDI0MzE3NDQwIiwic2NvcGVzIjpbInJlYWQiXX0.RBTtwqnDLHrtv1sJzaAzvoJ82xhfSVXOjeR-LgWNyuY77jDE6LfsgSZDY2261eZ4vkG7JyOTxDRHBga-0ES5Yd6P2DHa05DCwZgsm_ZvDRcxx24SPe-y_8yTvvvfoKn15OJ0NfZRZAhnv6x2o0IobAKEp7oElLkaclqq1QH8zYi_Ob1UcOB4z0uZs6_2TsYCrTTfx26gCjs1-MgYPBI1_-zDKWHfMBDtZso1P8cTLhTPUCc_7ESc0aAAT1zeI2qHMYc124lf3WWSCicV0pxNZ4BeaUcuxzFLmIdmy8wVZ15h-2YTRHOcM2tkgDVJfLnoYjh6Izx_UpVYfiZ7kzdAZw"
}
result = requests.post(url, json.dumps(data).encode(), headers=headers)
print(result.content.decode('utf-8'))
