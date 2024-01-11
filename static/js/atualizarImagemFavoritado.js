$(document).ready(function () {
    function atualizarEstadoFavorito() {
        $.ajax({
            url: '/favoritar/{{ fotografia.id }}/', type: 'GET', success: function (data) {
                if (data.favoritado) {
                    $('#coracao').attr('src', '{% static  "/assets/ícones/1x/favorite.svg" %}');
                } else {
                    $('#coracao').attr('src', '{% static "/assets/ícones/1x/favorite_outline.png" %}');
                }
            }
        });
    }

    atualizarEstadoFavorito();
    setInterval(atualizarEstadoFavorito, 5000);  // Atualiza a cada 5 segundos, por exemplo
});

