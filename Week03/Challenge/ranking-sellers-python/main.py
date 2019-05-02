from operator import itemgetter

class SellersRancking:
    def best_seller(self, sellers):
        ''' Mostrar o vendedor com maior valor em vendas. '''
        # return [
        #   max(sellers, key=itemgetter('value'))['name']
        # ] if sellers else []
        return [
            sorted(sellers, key=itemgetter('value'), reverse=True)[0]['name']
        ] if sellers else []

    def rancking_list(self, sellers):
        ''' Listar todos os vendedores ordenados pelo valor vendido, do maior para o menor '''
        return [
            seller['name'] for seller in sorted(sellers, key=itemgetter('value'), reverse=True)
        ]

    def best_seller_store(self, sellers, store):
        ''' Mostrar o melhor vendedor de uma determinada loja. Você receberá a lista de vendedores e deverá fazer um
            filtro nesta lista pela loja e retornar o nome do vendedor com o maior valor em vendas.
        '''
        return self.best_seller([seller for seller in sellers if seller['store'] == store])

    def sales_goals(self, sellers):
        ''' Também é estipulado uma meta para vendas de R$ 500,00. Então é necessário listar os vendedores que não
            atingiram esta meta, em ordem crescente pelo valor de venda.
        '''
        return self.rancking_list([seller for seller in sellers if seller['value'] < 500])
