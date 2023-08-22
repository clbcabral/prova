
function palindromo(palavra) {

  if (palavra.length < 3) {
    return "?";
  }

  for (let inicio = 0; inicio < palavra.length / 2; inicio++) {
    let fim = palavra.length - 1;
    if (palavra[inicio] != palavra[fim - inicio]) {
      return "N";
    }
  }
  
  return "S";
}

console.log(palindromo('cleber'));
console.log(palindromo('oi'));
console.log(palindromo('radar'));
console.log(palindromo('arara'));
console.log(palindromo('ffddfff'));