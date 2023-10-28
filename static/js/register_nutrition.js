function search_user() {

    const cpf = $('#cpf').val();

    $.ajax({
        url: '/search_nutrition/' + cpf,
        type: 'GET',
        success: function(data) {
            $('#username_response').text(data.nome);
        },
        error: function(data) {
            $('#username_reponse').text(data.nome);
        }
    });
}