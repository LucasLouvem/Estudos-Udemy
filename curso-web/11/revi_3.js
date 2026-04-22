// ES8: Object.values/Object.entries
const obj = {
  username0: "Santa",
  username1: "Rudolf",
  username2: "Mr. Grinch",
};
console.log(Object.keys(obj));
console.log(Object.values(obj));
console.log(Object.entries(obj));

// melhorias de notação literal
const nome = "santa";
const pessoa = {
  nome,
  ola() {
    return `: Oi gente`;
  },
};
console.log(pessoa.nome, pessoa.ola());

// Class
class humano {
  constructor(nome) {
    this.nome = nome;
  }
  apresentar() {
    return `Olá, meu nome é ${this.nome}`;
  }
  lutar() {
    return "Lutando...";
  }
}

class guerreiro extends humano {
  lutar() {
    return "Força total!";
  }
}

console.log(new humano("Santa").nome);
console.log(new humano("Santa").apresentar());
console.log(new guerreiro("Rudolf").apresentar());
console.log(new guerreiro("Rudolf").lutar());
