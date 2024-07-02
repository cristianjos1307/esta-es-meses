let mes_Nascimento = 11;

mes_Nascimento = parseInt(mes_Nascimento);

if (mes_Nascimento < 1 || mes_Nascimento > 12) {
    console.log("Esse Mês não existe! Por favor digite um mês existente");
} else {
    console.log("Os meses antes do seu aniversário são:");


    const meses_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

    for (let i = 0; i < mes_Nascimento - 1; i++) {
        console.log(meses_ano[i]);
    }
}