//com Promise

const http = require("http");

const getTurma = (letra) => {
  return new Promise((resolve, reject) => {
    const url = `http://files.cod3r.com.br/curso-js/turma${letra}.json`;
    http.get(url, (res) => {
      let resultado = "";
      res.on("data", (dados) => {
        resultado += dados;
      });
      res.on("end", () => {
        try {
          resolve(JSON.parse(resultado));
        } catch (e) {
          reject(e);
        }
      });
    });
  });
};

let nomes = [];

// getTurma("A")
//   .then((alunos) => {
//     nomes = nomes.concat(alunos.map((a) => `A: ${a.nome}`));
//     return getTurma("B");
//   })
//   .then((alunos) => {
//     nomes = nomes.concat(alunos.map((a) => `B: ${a.nome}`));
//     return getTurma("C");
//   })
//   .then((alunos) => {
//     nomes = nomes.concat(alunos.map((a) => `C: ${a.nome}`));
//     console.log(nomes);
//   });

Promise.all([getTurma("A"), getTurma("B"), getTurma("C")])
  .then((turmas) => [].concat(...turmas))
  .then((alunos) => alunos.map((a) => a.nome))
  .then((nomes) => console.log(nomes))
  .catch((e) => console.log(e.message));

getTurma("D").catch((e) => console.log(e.message));
