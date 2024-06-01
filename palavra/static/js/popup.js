function showPopUp() {
    const popup = document.querySelector('.container-layout');
    const icone_popup = document.querySelector(".suporte");

    popup.style.display = 'flex';
    document.querySelector("body").classList.add("stop-scroll");
    
    icone_popup.addEventListener('click', function() {
        popup.style.display = 'flex';
        document.querySelector("body").classList.add("stop-scroll");
    });

    document.getElementById('fechar-popup').addEventListener('click', function() {
        popup.style.display = 'none';
        document.querySelector("body").classList.remove("stop-scroll");
    });
    popup.addEventListener('click', function(){
        popup.style.display = 'none';
        document.querySelector("body").classList.remove("stop-scroll");
    });
}

document.addEventListener('DOMContentLoaded', showPopUp);