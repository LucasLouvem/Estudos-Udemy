//não aceita repetição, não tem index, não tem chave/valor, é iterável
const times = new Set();
times.add("Vasco");
times.add("São Paulo").add("Palmeiras").add("Corinthians");
times.add("Vasco"); // não adiciona

console.log(times);
console.log(times.has("Vasco")); // true
console.log(times.size); // 4
times.delete("Vasco");
console.log(times.has("Vasco")); // false
times.clear();
console.log(times.size); // 0

const nomes = ["Raquel", "Lucas", "Julia", "Lucas"];
const nomesSet = new Set(nomes);
console.log(nomesSet); // { 'Raquel', 'Lucas', 'Julia' }
