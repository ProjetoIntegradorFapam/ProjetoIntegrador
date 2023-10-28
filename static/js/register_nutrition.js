document.getElementById("register_nutrition_form").addEventListener("submit", function (event) {
    
    const inputs = document.getElementByClass("form-control");

    for(input of inputs) {

        if (!input.value) {
            event.preventDefault();
            return;
        }
    }
});

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