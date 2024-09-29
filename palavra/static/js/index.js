document.addEventListener("DOMContentLoaded", function() {

    const elemento = document.getElementById("texto-animado");
    const texto = elemento.textContent.trim();
    elemento.textContent = "";

    let indice = 0;

    function typingEffect() {
        if (indice < texto.length) {
            elemento.textContent += texto.charAt(indice);
            indice++;
            setTimeout(typingEffect, 38);
        } else {
            setTimeout(() => {
                elemento.textContent = "";
                indice = 0;
                setTimeout(typingEffect, 1500);
            }, 1500);
        }
    }

    typingEffect();
});