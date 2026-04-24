function funcionarOuNao(valor, chanceErro) {
  return new Promise((resolve, reject) => {
    try {
      if (Math.random() < chanceErro) {
        reject("Ocorreu um erro!"); // -> rejeita a promessa com uma mensagem de erro
      } else {
        resolve(valor); // -> resolve a promessa com o valor passado como argumento
      }
    } catch (e) {
      // -> captura qualquer erro que possa ocorrer durante a execução do código e rejeita a promessa com o erro capturado
      reject(e);
    }
  });
}

funcionarOuNao("Funcionou!!", 0.5)
  .then((v) => console.log(v))
  .catch((err) => console.log("Erro:", err));
