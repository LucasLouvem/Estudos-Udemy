// async/await

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

let obterAlunos = async () => {
  const turmaA = await getTurma("A");
  const turmaB = await getTurma("B");
  const turmaC = await getTurma("C");
  return [].concat(turmaA, turmaB, turmaC);
};

obterAlunos()
  .then((alunos) => alunos.map((a) => a.nome))
  .then((nomes) => console.log(nomes))
  .catch((e) => console.log(e.message));
