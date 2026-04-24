function esperarPor(tempo) {
  return new Promise(function (resolve) {
    setTimeout(() => resolve(), tempo);
  });
}

function retornarValorRapido() {
  return 20;
}

esperarPor(2000).then(() => console.log("Executando promise..."));

async function executar() {
  let valor = await retornarValorRapido();

  await esperarPor(2000);
  console.log(`Async/Await ${valor}...`);
  await esperarPor(2000);
  console.log(`Async/Await ${valor + 1}...`);
  await esperarPor(2000);
  console.log(`Async/Await ${valor + 2}...`);
  await esperarPor(2000);
  console.log(`Async/Await ${valor + 3}...`);

  return valor + 3;
}

async function executarDeVerdade() {
  const valor = await executar();
  console.log(valor);
}

executarDeVerdade();
