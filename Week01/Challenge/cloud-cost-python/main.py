from decimal import *

''' The Weekly challenge of Acceleration Python for Web '''
class CloudCost():
    ''' https://www.codenation.dev/acceleration/aceleradev-python-1/challenge/cloud-cost-python '''
    def lambda_execution(self):
        ''' Returns the cost of one function execution '''

        VALUE_BY_EXECUTION = 0.0000002  # Valor por execução da função: U$ 0.0000002
        VALUE_BY_TIME_EXECUTION = 0.0002080  # Valor por tempo de execução: U$ 0.0002080 por segundo executado
        return VALUE_BY_EXECUTION + VALUE_BY_TIME_EXECUTION * self.time_execution()

    def app_execution(self, execution_times):
        ''' Returns the total cost of all executions '''

        VALUE_BY_MESSAGE = 0.00000040  # Valor por mensagem recebida na fila: U$ 0.00000040
        return execution_times * ((self.lambda_execution() * 2) + VALUE_BY_MESSAGE)

    def month(self, execution_times, month_of_year):
        ''' This method should:
            - Calculate how many executions was made in a specific month
              NOTE: The execution times is about how many executions was made per day
        '''
        month_with_31_days = [1, 3, 5, 7, 8, 10, 12]

        days = 0  # number of days in a month
        if month_of_year == 2:
            days = 28
        elif month_of_year in month_with_31_days:
            days = 31
        else:
            days = 30

        return self.app_execution(execution_times * days)

    def year(self, execution_times):
        ''' Returns a list with all total costs per month by a year '''
        total_executions = []
        for i in range(1, 13):
            total_executions.append(self.month(execution_times, i))

        return total_executions

    def time_execution(self):
        ''' Para fins de cálculo vamos considerar que o tempo de execução de cada função é de 3 segundos '''
        return 3

if __name__ == '__main__':
    cc = CloudCost()
    print(cc.year(1))
    print(cc.year(50))
    print(cc.year(100))
    print(cc.year(1000))
    print(cc.year(5000))
