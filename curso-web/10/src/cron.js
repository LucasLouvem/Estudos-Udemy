const scredule = require("node-schedule");

const task1 = scredule.scheduleJob("*/5 34 15 * * 3", function () {
  console.log("Executando a tarefa 1", new Date().toLocaleTimeString());
  // executa tarefa 1 de 5 em 5 segundos às 15h32 de toda quarta-feira
});

setTimeout(function () {
  task1.cancel();
  console.log("Tarefa 1 cancelada");
}, 20000);

const rule = new scredule.RecurrenceRule();
rule.dayOfWeek = [new scredule.Range(1, 5)]; // Segunda a sexta-feira
rule.hour = 15; // 15h
rule.second = 35; // 35 segundos

const task2 = scredule.scheduleJob(rule, function () {
  console.log("Executando a tarefa 2", new Date().toLocaleTimeString());
  // executa tarefa 2 às 15h35 de segunda a sexta-feira
});
