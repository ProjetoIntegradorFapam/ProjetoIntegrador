document.querySelector("#search_button").addEventListener('click', function() {
    location.href = "/users?cpf="+$('#search_input').val();
})