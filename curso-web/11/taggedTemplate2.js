function real(strings, ...values) {
  const result = [];
  values.forEach((valor, i) => {
    valor = isNaN(valor) ? valor : `R$ ${valor.toFixed(2)}`;
    result.push(strings[i], valor);
  });
  result.push(strings[strings.length - 1]);
  return result.join("");
}

const preco = 29.99;
const precoParcela = 11.99;
console.log(real`1x de ${preco} ou 3x de ${precoParcela}.`);
