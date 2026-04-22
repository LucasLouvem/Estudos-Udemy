// let e const

let a = 10;
let b = 20;
console.log(b);

// console.log(a); // ReferenceError: a is not defined
{
  var d = 30;
  var e = 40;
  console.log(e);
}

console.log(d);

//template string

const produto = "Ipad";
console.log(`O produto é ${produto} e o preço é R$ 2000,00`);

// Desctructuring

const [l, f, g, ...tras] = "Cod3r";
console.log(l, f, g, tras);

const { idade: i, nome: n } = { nome: "Ana", idade: 9 };
console.log(n, i);
