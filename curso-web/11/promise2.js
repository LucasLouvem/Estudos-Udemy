// setTimeout(function () {
//   console.log("Executando callback...");

//   setTimeout(function () {
//     console.log("Executando callback de callback...");
//     setTimeout(function () {
//       console.log("Executando callback de callback de callback...");
//     }, 2000);
//   }, 2000);
// }, 2000);

function esperarPor(tempo) {
  return new Promise(function (resolve) {
    setTimeout(function () {
      console.log("Executando promise...");
      resolve("Executando promise depois de " + tempo / 1000 + " segundos...");
    }, tempo);
  });
}

esperarPor(2000)
  .then((mensagem) => {
    console.log((mensagem = "Trocando mensagem 1..."));
    return esperarPor(2000);
  })
  .then((mensagem) => {
    console.log((mensagem = "Voltando a trocar de mensagem..."));
    return esperarPor(2000);
  })
  .then((mensagem) => {
    console.log(mensagem);
  });
