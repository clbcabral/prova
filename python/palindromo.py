
def palindromo(palavra):
    
  if len(palavra) < 3:
      return '?'
  
  return 'S' if palavra == palavra[::-1] else 'N'


print(palindromo('cleber'));
print(palindromo('oi'));
print(palindromo('radar'));
print(palindromo('arara'));
print(palindromo('ffddfff'));