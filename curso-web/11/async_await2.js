function gerarNumeroEntre(min, max, proibidos = []) {
  if (min > max) [max, min] = [min, max];

  return new Promise((resolve, reject) => {
    const fator = max - min + 1;
    const aleatorio = parseInt(Math.random() * fator) + min;
    if (proibidos.includes(aleatorio)) {
      reject(`O número gerado foi ${aleatorio} e está na lista de proibidos.`);
    } else {
      resolve(aleatorio);
    }
  });
}

async function gerarMegaSena(qtdeNumeros, tentativas = 1) {
  try {
    const numeros = [];
    for (let _ of Array(qtdeNumeros).fill()) {
      numeros.push(await gerarNumeroEntre(1, 60, numeros));
    }
    return Promise.all(numeros);
  } catch (error) {
    if (tentativas > 5) {
      throw "Que chato... " + error;
    }
    return gerarMegaSena(qtdeNumeros, tentativas + 1);
  }
}

//gerarNumeroEntre(1, 10, [2, 3, 4, 5]).then(console.log).catch(console.log);
gerarMegaSena(15).then(console.log).catch(console.log);
