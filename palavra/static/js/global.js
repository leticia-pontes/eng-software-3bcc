document.addEventListener('DOMContentLoaded', function() {

    let ignorar = ["Control", "Space", "AltGraph", "Alt", "Shift", "CapsLock", "Tab", "Alt", "Escape", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

    let linhas = document.querySelectorAll('.bloco-palavras__fila');
    let indiceLinhaAtiva = 0;

    const alerta = document.getElementById("alerta");
    const botaoConfirmaAlerta = document.getElementById("botaoConfirmaAlerta");

    function handleInput(event, elementos, indice) {
        let entrada = event.currentTarget.value.trim();
        if (entrada.length === 1 && indice < elementos.length - 1) {
            elementos[indice + 1].focus();
        }
    }

    function handleKeydown(event, elementos, indice) {
        if (event.key === 'Enter') {
            let preenchido = Array.from(elementos).every(elemento => elemento.value.trim() !== '');
            if (!preenchido) return;

            let palavra = Array.from(elementos).map(elemento => elemento.value.trim()).join('');
            enviaPalavra(palavra);

            if (indiceLinhaAtiva < linhas.length - 1) {
                indiceLinhaAtiva++;
                desativaLinhasNaoAtivas();
                setTimeout(() => linhas[indiceLinhaAtiva].querySelector('.bloco-palavras__letra').focus(), 100);
            }
        } else if (event.key === 'Backspace') {
            let elementoAtual = elementos[indice];
            let elementoAnterior = elementos[indice - 1];
            if (elementoAtual.value === '' && elementoAnterior) {
                elementoAnterior.focus();
                elementoAnterior.value = '';
            } else if (elementoAtual.value !== '') {
                elementoAtual.value = '';
            }
        } else if (!((event.keyCode >= 65 && event.keyCode <= 90) || (event.keyCode >= 97 && event.keyCode <= 122) || ignorar.includes(event.key))) {
            event.preventDefault();
        }
    }

    function handleFocus(event) {
        let input = event.currentTarget;
        input.setSelectionRange(input.value.length, input.value.length);
    }

    function setupLineHandlers(linha) {
        let elementos = linha.querySelectorAll('.bloco-palavras__letra');
        elementos.forEach((elemento, i) => {
            elemento.addEventListener('input', event => handleInput(event, elementos, i));
            elemento.addEventListener('keydown', event => handleKeydown(event, elementos, i));
            elemento.addEventListener('focus', handleFocus);
        });
    }

    linhas.forEach(setupLineHandlers);

    function desativaLinhasNaoAtivas() {
        linhas.forEach((linha, indice) => {
            linha.querySelectorAll('.bloco-palavras__letra').forEach(input => {
                input.disabled = (indice !== indiceLinhaAtiva);
            });
        });
    }

    desativaLinhasNaoAtivas();

    function atualizaFeedback(feedback, linhaAtiva, ganhou = false) {
        let elementos = linhaAtiva.querySelectorAll('.bloco-palavras__letra');
        feedback.forEach((letra, indice) => {
            let elementoLetra = elementos[indice];
            if (elementoLetra) {
                elementoLetra.value = letra[0];
                elementoLetra.classList.remove('letras-pop__certa', 'letras-pop__errada', 'letras-pop__nao-tem');

                if (letra[1] === 'CORRECT_POSITION') {
                    elementoLetra.classList.add('letras-pop__certa');
                } else if (letra[1] === 'WRONG_POSITION') {
                    elementoLetra.classList.add('letras-pop__errada');
                }

                if (ganhou && letra[1] === 'CORRECT_POSITION') {
                    elementoLetra.classList.add('letras-pop__certa');
                }
            }
        });
    }

    function enviaPalavra(palavra) {

        fetch('/jogo/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ palavra: palavra })
        })
        .then(response => response.json())
        .then(data => {

            let result = data['result'];
            console.log('Pa pum pirulito pão doce:', result);
            
            if (result['win']) {
                atualizaFeedback(result['feedback'], linhas[indiceLinhaAtiva - 1], true);

                setTimeout(() => {
                    mostrarAlerta("Você ganhou!", "Parabéns por acertar a palavra!");
                    limparInputs();

                }, 600);
                indiceLinhaAtiva = 0;
            } else {
                atualizaFeedback(result['feedback'], linhas[indiceLinhaAtiva - 1]);
                if (indiceLinhaAtiva === linhas.length - 1) {
                    desativaLinhasNaoAtivas();
                    setTimeout(() => {
                        mostrarAlerta("Não foi dessa vez...", "Você não acertou a palavra. Tente de novo.");
                        limparInputs();
                        indiceLinhaAtiva = 0;
                    }, 600);
                }
            }
        })
        .catch(error => {
            console.error('Error sending word to backend:', error);
        });
    }

    function limparInputs() {
        linhas.forEach(linha => {
            linha.querySelectorAll('.bloco-palavras__letra').forEach(input => {
                input.value = '';
                input.classList.remove('letras-pop__certa', 'letras-pop__errada', 'letras-pop__nao-tem');
                input.removeAttribute('disabled');
            });
        });
        indiceLinhaAtiva = 0;
        desativaLinhasNaoAtivas();
    }

    function mostrarAlerta(titulo, mensagem) {
        document.getElementById('tituloAlerta').innerText = titulo;
        document.getElementById('mensagemAlerta').innerText = mensagem;
        alerta.style.display = "block";
    }

    if (botaoConfirmaAlerta) {
        botaoConfirmaAlerta.addEventListener('click', () => {
            alerta.style.display = "none";
            limparInputs();
        });
    }

    window.addEventListener('click', (event) => {
        if (event.target == alerta) {
            alerta.style.display = "none";
            limparInputs();
        }
    });
    
});
