const fs = require("fs");
const path = require("path");

const caminho = path.join(__dirname, "dados.txt");

const lerArquivo = (caminho) => {
  return new Promise((resolve, reject) => {
    fs.readFile(caminho, "utf-8", (err, conteudo) => {
      if (err) {
        reject(err);
      } else {
        resolve(conteudo);
      }
    });
  });
};

lerArquivo(caminho)
  .then(console.log("Lendo arquivo..."))
  .then((conteudo) => conteudo.split("\n"))
  .then((linhas) => linhas.join(", "))
  .then(console.log)
  .catch(console.error);
