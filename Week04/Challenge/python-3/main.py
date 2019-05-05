import numpy as np
import datetime

class ManagerDates:
    def date_is_valid(self, date):
        ''' - Faça uma função que receba uma data no formato dd/mm/YYYY e determine se a mesma é válida.
              A data será válida apenas se estiver no formato dd/mm/YYYY.
        '''
        is_valid = True
        try:
            datetime.datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            is_valid = False

        return is_valid

    def date_weekday(self, date):
        ''' Faça uma função que receba uma data e retorne o dia da semana correspondente. Ex: "Saturday" '''
        return datetime.datetime.strptime(str(date)[:10], '%Y-%m-%d').strftime('%A')

    def convert_string_to_date(self, date_str):
        ''' Faça uma função que receba uma data em formato string e retorne em formato datetime.
            Formatos válidos: "dd/mm/YYYY", "dd-mm-YYYY" , "ddmmYYYY", retorna False se a data não esta em um
            desses formatos.
        '''
        for a_format in ['%d/%m/%Y', '%d-%m-%Y', '%d%m%Y']:
            try:
                return datetime.datetime.strptime(date_str[:10], a_format)
            except ValueError:
                pass
        return False

    def get_all_dates(self, month, year):
        ''' Faça uma função que recebe o ano e o mês e retorne todas as datas do mês.
            Obs: utilize o Numpy (arange).
        '''
        start = year + '-' + month
        stop = year + '-' + f'{int(month)+1:02}' if int(month) < 12 else str(int(year) + 1) + '-01'
        return np.arange(start, stop, dtype='datetime64[D]')

    def count_days_mounth(self, month, year):
        ''' Faça uma função que recebe o ano e o mês e retorne a quantidade de dias úteis que ele possui.
            Obs: Utilize o Numpy.
        '''
        return np.count_nonzero(np.is_busday(self.get_all_dates(month=month, year=year)))

    def get_first_monday(self, year):
        ''' Faça uma função que recebe o ano e encontre a primeira segunda-feira de maio.
            O retorno deve ser uma string no formato "dd/mm/YYYY". Obs: Utilize NumPy.
        '''
        first_monday = np.busday_offset(year + '-05', 0, roll='forward', weekmask='Mon')
        return datetime.datetime.strftime(first_monday.tolist(), '%d/%m/%Y')
