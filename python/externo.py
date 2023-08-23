import requests

class Chamador():

    def faz_chamada_externa(self):
        res = requests.get('https://swapi.dev/api/people/1')
        return res.json()

if __name__ == '__main__':
    chamador = Chamador()
    res = chamador.faz_chamada_externa()
    print(res)