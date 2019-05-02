from operator import itemgetter

class SellersRancking:
    def sorted_sellers(self, aList, aKey, isReverse=False):
        ''' Return a sorted list based on a key. It can be reversed or not. '''
        return sorted(aList, key=itemgetter(aKey), reverse=isReverse)

    def best_seller(self, sellers):
        ''' Mostrar o vendedor com maior valor em vendas. '''
        return [self.sorted_sellers(aList=sellers, aKey='value', isReverse=True)[0]['name']] if sellers else []

    def rancking_list(self, sellers):
        ''' Listar todos os vendedores ordenados pelo valor vendido, do maior para o menor '''
        return [
            sellers['name'] for sellers in self.sorted_sellers(aList=sellers, aKey='value', isReverse=True)
        ]

    def best_seller_store(self, sellers, store):
        ''' Mostrar o melhor vendedor de uma determinada loja. Você receberá a lista de vendedores e deverá fazer um filtro nesta lista pela loja e retornar o nome do vendedor com o maior valor em vendas. '''
        return [([sellers['name'] for sellers in self.sorted_sellers(aList=sellers, aKey='value', isReverse=True) if sellers['store'] == store])[0]] if sellers else []

    def sales_goals(self, sellers):
        ''' Também é estipulado uma meta para vendas de R$ 500,00. Então é necessário listar os vendedores que não atigiram esta meta, em ordem crescente pelo valor de venda. '''
        return [sellers['name'] for sellers in self.sorted_sellers(aList=sellers, aKey='value') if sellers['value'] < 500]
