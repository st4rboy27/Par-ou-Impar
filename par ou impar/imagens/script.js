let escolha = '';

function escolher(opcao) {
    escolha = opcao;
    document.getElementById('par').disabled = true;
    document.getElementById('impar').disabled = true;
}

function verificarResultado() {
    const numeroUsuario = parseInt(document.getElementById('numero').value);
    if (isNaN(numeroUsuario) || numeroUsuario < 0 || numeroUsuario > 10) {
        alert('Escolha um número entre 0 e 10.');
        return;
    }

    const numeroComputador = Math.floor(Math.random() * 11);
    const soma = numeroUsuario + numeroComputador;
    const resultadoImg = document.getElementById('resultado-img');

    document.getElementById('computador').textContent = `O computador escolheu: ${numeroComputador}`;
    document.getElementById('soma').textContent = `A soma dos números é: ${soma}`;

    if ((escolha === 'par' && soma % 2 === 0) || (escolha === 'impar' && soma % 2 !== 0)) {
        resultadoImg.src = 'imagens/win.png';
        resultadoImg.alt = 'Vitória';
    } else {
        resultadoImg.src = 'imagens/lose.png';
        resultadoImg.alt = 'Derrota';
    }

    document.getElementById('par').disabled = false;
    document.getElementById('impar').disabled = false;
}
