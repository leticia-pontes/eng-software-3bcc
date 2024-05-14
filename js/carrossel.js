

    $(document).ready(function(){
        $('.carrossel-conquista-lista').slick({
            slidesToShow: 4,
            slidesToScroll: 1,
            autoplaySpeed: 2000,
            dots: false,
            arrows: true,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
                // Adicione mais breakpoints conforme necessário
            ]
        });
    });

