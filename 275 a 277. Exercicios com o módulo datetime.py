import datetime
import pytz
from dateutil.relativedelta import relativedelta

def e274():
    data = str(datetime.datetime.strptime('20/04/2022', '%d/%m/%Y'))
    for c in range(10):
        print(data[c],end='')
def e275():
    data = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    datab = str(datetime.datetime.now(pytz.timezone('Asia/Seoul')))
    datac = datab[0:10]
    print(datac)
    print(data.timestamp())
    data = str(data)
    print(datetime.datetime.fromtimestamp(1690574739))
    for c in range(19):
        print(data[c], end='')
def e276():
    fmt = '%d/%m/%Y %H:%M:%S'
    data_inicio = datetime.datetime.strptime('20/04/1987 09:30:30', fmt)
    data_fim = datetime.datetime.strptime('12/12/2022 08:20:20', fmt)
    delta = data_fim - data_inicio
    print(delta.days, delta.seconds)
    print(delta.total_seconds())
    print(data_fim + relativedelta(seconds=60, minutes=10))
def e277():
    print(datetime.datetime.now())
    data = datetime.datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
    print(data)
    data = datetime.datetime.strftime(data, '%d/%m/%Y')
    print(data)
    data = datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('Mexico/BajaNorte')), '%H:%M:%S')
    print(data)


#e274()
#e275()
#e276()
#e277()