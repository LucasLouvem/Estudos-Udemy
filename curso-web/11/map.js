const tecnologias = new Map();

tecnologias.set("react", { framework: false });
tecnologias.set("angular", { framework: true });

console.log(tecnologias.react); // undefined
console.log(tecnologias.get("react").framework); // false

const chavesVariadas = new Map([
  [function () {}, "Função"],
  [{}, "Objeto"],
  [123, "Número"],
]);

chavesVariadas.forEach((valor, chave) => {
  console.log(chave, valor);
});

console.log(chavesVariadas.has(123)); // true
chavesVariadas.delete(123);
console.log(chavesVariadas.has(123)); // false
console.log(chavesVariadas.size); // 2

chavesVariadas.set(123, "1");
chavesVariadas.set(123, "2");
//chavesVariadas.set(123, "3");
console.log(chavesVariadas); // 123 => '3'
