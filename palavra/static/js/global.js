document.addEventListener('DOMContentLoaded', function() {

    // Define the keys to ignore
    let ignorar = ["Control", "Space", "AltGraph", "Alt", "Shift", "CapsLock", "Tab", "Alt", "Escape", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

    // Seleciona a linha ativa
    var linhas = document.querySelectorAll('.bloco-palavras__fila');
    var activeLineIndex = 0;

    function handleInput(event, elementos, index) {
        var value = event.currentTarget.value.trim();
        if (value.length === 1) {
            if (index < elementos.length - 1) {
                var proximoElemento = elementos[index + 1];
                proximoElemento.focus();
            }
        }
    }

    function handleKeydown(event, elementos, index) {
        if (event.key === 'Enter') {
            // Monta a palavra e mostra no console quando apertar Enter
            var word = '';
            elementos.forEach(function(elemento) {
                word += elemento.value.trim();
            });
            console.clear();
            console.log('Word:', word);

            // Move to the next line
            if (activeLineIndex < linhas.length - 1) {
                activeLineIndex++;
                var nextElementos = linhas[activeLineIndex].querySelectorAll('.bloco-palavras__letra');
                nextElementos[0].focus();
            }
        } else if (event.key === 'Backspace') {
            var elementoAnterior = elementos[index - 1];
            if (elementoAnterior) {
                elementoAnterior.focus();
                elementoAnterior.value = '';
            }
        } else {
            if (!((event.keyCode >= 65 && event.keyCode <= 90) || (event.keyCode >= 97 && event.keyCode <= 122) || ignorar.includes(event.key))) {
                event.preventDefault();
            }
        }
    }

    function handleFocus(event) {
        var input = event.currentTarget;
        input.setSelectionRange(input.value.length, input.value.length);
    }

    function setupLineHandlers(linha, index) {
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

    linhas.forEach(setupLineHandlers);
});
