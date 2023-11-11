document.querySelector("#search_button").addEventListener('click', function() {
    location.href = "/users?cpf="+$('#search_input').val();
});

document.querySelector("#delete_user_button").addEventListener('click', function() {
    location.href = "/delete_user?cpf="+$('#user_cpf').val();
});

document.querySelector("#edit_user_button").addEventListener('click', function() {
    location.href = "/edit_user/"+$('#user_cpf').val();
})

document.querySelector("#alimentar_plan_button").addEventListener('click', function() {
    location.href = "/alimentar_plan/"+$('#user_cpf').val();
})
