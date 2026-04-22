const port = 3000;
const express = require("express");
const app = express();
const database = require("./database.js");
app.use(express.json());

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/produtos", (req, res) => {
  res.send(database.getProdutos());
});

app.get("/produtos/:id", (req, res) => {
  const produto = database.getProduto(req.params.id);
  if (produto.id) {
    res.send(produto);
  } else {
    res.status(404).send({ error: "Produto não encontrado" });
  }
});

app.post("/produtos", (req, res) => {
  if (!req.body.nome || !req.body.preco) {
    res.status(400).send({ error: "Nome e preço são obrigatórios" });
    return;
  }
  try {
    const produto = database.salvarProduto({
      nome: req.body.nome,
      preco: req.body.preco,
    });
    res.status(201).send(produto);
  } catch (error) {
    res.status(400).send({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Escutando na porta: ${port}!`);
});
