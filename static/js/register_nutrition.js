function search_user(cpf) {
    
    $.ajax({
        url: `/search_nutrition`,
        type: 'GET',
        //data: JSON.stringify(usuario),
        //data: {'id': '7', 'nome': 'BRUNO'},
        //data: post_cpf,
        data: {'cpf': cpf},
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        sucess: function (result, status, request) {
            return console.log(result);
        },
        error: function (event, jqxhr, settings, thrownError) {
            console.log('event: ' + JSON.stringify(event));
            console.log('jqxhr: ' + jqxhr);
            console.log('settings: ' + settings);
            console.log('thrownError: ' + thrownError);
            //alert('Error');
        }
    });
}