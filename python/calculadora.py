import sqlite3

class CalculadoraAbstrata:

    def __init__(self):
        self.__operacoes = {
            'mais': self.__somar,
            'menos': self.__subtrair,
            'vezes': self.__multiplicar,
            'dividido por': self.__dividir,
            'elevado a': self.__potenciar,
        }

    def calcular(self, frase):
        a, b, operacao = self.__parse(frase)
        metodo = self.__operacoes[operacao]
        return metodo(a, b)

    def __parse(self, frase):
        ar = frase.split(' ')
        a = int(ar.pop(0))
        b = int(ar.pop())
        operacao = ' '.join(ar)
        return (a, b, operacao)

    def __somar(self, a, b):
        return a + b

    def __subtrair(self, a, b):
        return a - b

    def __multiplicar(self, a, b):
        return a * b
    
    def __dividir(self, a, b):
        return a / b
    
    def __potenciar(self, a, b):
        return a ** b


class CalculadoraConsole(CalculadoraAbstrata):

    def main(self):
        print('Bem-vindo/a à calculadora console!\n')
        print('2 mais 22 menos 4')
        print('3 vezes 2')
        print('6 dividido por 2')
        print('4 elevado a 2')
        
        while (True):
            print('Escreva o seu cálculo com algum dos formatos acima:')
            frase = input()
            resultado = self.calcular(frase)
            print(resultado)


class CalculadoraArquivo(CalculadoraConsole):

    def __init__(self, arquivo, substituir_conteudo=False):
        super().__init__()
        self.__arquivo = arquivo
        self.__substituir_conteudo = substituir_conteudo

    def calcular(self, frase):
        resultado = super().calcular(frase)
        modo = 'w' if self.__substituir_conteudo else 'a+'
        with open(self.__arquivo, modo) as arquivo:
            arquivo.write('%s\n%s\n' % (frase, resultado))
        return resultado


class CalculadoraBD(CalculadoraConsole):

    def __init__(self, arquivo):
        super().__init__()
        self.__arquivo = arquivo

    def criar_tabela(self, conexao):
        cursor = conexao.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS calculadora (
                frase VARCHAR(50) NOT NULL, 
                resultado FLOAT NOT NULL
            )
            """
        cursor.execute(sql)
        conexao.commit()

    def persistir_resultado(self, frase, resultado):
        conexao = sqlite3.connect(self.__arquivo)
        self.criar_tabela(conexao=conexao)
        cursor = conexao.cursor()
        sql = """
            INSERT INTO calculadora 
                (frase, resultado) 
            VALUES 
                (?, ?)
            """
        cursor.execute(sql, (frase, resultado))
        conexao.commit()
        conexao.close()

    def calcular(self, frase):
        resultado = super().calcular(frase)
        self.persistir_resultado(frase, resultado)
        return resultado

if __name__ == '__main__':
    calculadora = CalculadoraConsole()
    calculadora = CalculadoraArquivo(arquivo='/tmp/foo.txt', substituir_conteudo=False)
    calculadora = CalculadoraBD(arquivo='/tmp/banco.db')
    calculadora.main()