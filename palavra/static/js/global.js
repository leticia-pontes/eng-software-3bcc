document.addEventListener('DOMContentLoaded', function() {

    // Ignora as teclas
    let ignorar = ["Control", "Space", "AltGraph", "Alt", "Shift", "CapsLock", "Tab", "Alt", "Escape", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

    // Seleciona a linha ativa
    var linhas = document.querySelectorAll('.bloco-palavras__fila');
    var indiceLinhaAtiva = 0;

    // Ações de entrada
    function handleInput(event, elementos, indice) {
        var entrada = event.currentTarget.value.trim();
        if (entrada.length === 1) {
            if (indice < elementos.length - 1) {
                var proximoElemento = elementos[indice + 1];
                proximoElemento.focus();
            }
        }
    }

    // Ações de teclas
    function handleKeydown(event, elementos, indice) {
        if (event.key === 'Enter') {

            // Verifica se as letras foram preenchidas
            var preenchido = Array.from(elementos).every(function(elemento) {
                return elemento.value.trim() !== '';
            });

            // Se não foram preenchidas, continua aguardando o preenchimento
            if (!preenchido) {
                return;
            }

            // Monta a palavra
            var palavra = '';
            elementos.forEach(function(elemento) {
                palavra += elemento.value.trim();
            });
            console.clear();
            console.log(palavra);

            enviaPalavra(palavra);

            // Vai pra próxima linha
            if (indiceLinhaAtiva < linhas.length - 1) {

                indiceLinhaAtiva++;
                var nextElementos = linhas[indiceLinhaAtiva].querySelectorAll('.bloco-palavras__letra');
                nextElementos[0].focus();

                desativaLinhasNaoAtivas();

                setTimeout(function() {
                    nextElementos[0].focus();
                }, 100);
            }
        } else if (event.key === 'Backspace') {
            var elementoAtual = elementos[indice];
            var elementoAnterior = elementos[indice - 1];
            if (elementoAtual.value === '' && elementoAnterior) {
                elementoAnterior.focus();
                elementoAnterior.value = '';
            } else if (elementoAtual.value !== '') {
                elementoAtual.value = '';
            }
        } else {
            if (!((event.keyCode >= 65 && event.keyCode <= 90) || (event.keyCode >= 97 && event.keyCode <= 122) || ignorar.includes(event.key))) {
                event.preventDefault();
            }
        }
    }

    // Ações de foco
    function handleFocus(event) {
        var input = event.currentTarget;
        input.setSelectionRange(input.value.length, input.value.length);
    }

    // Define as ações para as linhas
    function setupLineHandlers(linha) {
        var elementos = linha.querySelectorAll('.bloco-palavras__letra');

        elementos.forEach(function(elemento, i) {
            elemento.addEventListener('input', function(event) {
                handleInput(event, elementos, i);
            });

            elemento.addEventListener('keydown', function(event) {
                handleKeydown(event, elementos, i);
            });

            elemento.addEventListener('focus', handleFocus);
        });
    }

    // Define as ações para cada linha
    linhas.forEach(setupLineHandlers);

    
    function desativaLinhasNaoAtivas() {        
        linhas.forEach((linha, indice) => {            
            if (indice !== indiceLinhaAtiva) {
                linha.querySelectorAll('.bloco-palavras__letra').forEach(input => {
                    input.disabled = true;
                });
            } else {
                linha.querySelectorAll('.bloco-palavras__letra').forEach(input => {
                    input.disabled = false;
                });
            }
        });
    }

    desativaLinhasNaoAtivas();

    function enviaPalavra(palavra) {
        fetch('/palavra/jogo/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ palavra: palavra })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response from backend:', data);
            // Handle response from backend
        })
        .catch(error => {
            console.error('Error sending word to backend:', error);
            // Handle error
        });
    }

});
