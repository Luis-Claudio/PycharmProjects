from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%A %B %y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%c'))
    dia_semana=('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(dia_semana[data_atual.weekday()])
    mes=(' ', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    print(mes[data_atual.month])
    data_criada=datetime(2021, 11, 11, 21, 34, 50)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '31/07/1965 18:20:30'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    data_calculada = data_convertida - timedelta(days=365, hours=1, minutes=10)
    print(data_calculada)


def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))
    data_atual_str = data_atual.strftime('%A %B %y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario= time(hour=15, minute=18, second=30)
    print(horario)
    print (type(horario))
    horario_str= horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()