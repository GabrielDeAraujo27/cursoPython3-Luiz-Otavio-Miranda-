import datetime
import pytz

def e275():
    data = str(datetime.datetime.strptime('20/04/2022', '%d/%m/%Y'))
    for c in range(10):
        print(data[c],end='')
def e276():
    data = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    datab = str(datetime.datetime.now(pytz.timezone('Asia/Seoul')))
    datac = datab[0:10]
    print(datac)
    print(data.timestamp())
    data = str(data)
    print(datetime.datetime.fromtimestamp(1690574739))
    for c in range(19):
        print(data[c], end='')

#e275()
#e276()

