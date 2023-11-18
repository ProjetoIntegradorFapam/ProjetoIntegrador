document.querySelector('#search_button').addEventListener('click', function() {
    location.href = "/users?cpf="+$('#search_input').val();
});

document.querySelectorAll('.delete_user_button').forEach((el) =>
  el.addEventListener('click', function() {
    location.href = "/delete_user?cpf="+$('#user_cpf').val();
  })
);

document.querySelectorAll('.edit_user_button').forEach((el) =>
  el.addEventListener('click', function() {
    location.href = "/edit_user/"+$('#user_cpf').val();
  })
);

document.querySelectorAll('.alimentar_plan_button').forEach((el) =>
  el.addEventListener('click', function() {
    location.href = "/alimentar_plan/"+$('#user_cpf').val();
  })
);
