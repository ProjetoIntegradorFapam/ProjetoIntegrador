document.getElementById("register_user_form").addEventListener("submit", function (event) {
    
    const inputs = document.getElementByClass("form-control");

    for(input of inputs) {

        if (!input.value) {
            event.preventDefault();
            return;
        }
    }
});

//Receber 0 ou 1 do checkbox para a coluna permissao_id no bd...
document.addEventListener('DOMContentLoaded', function () {
    const permissao_id_checkbox = document.getElementById('permissao_id_checkbox');
    const permissao_id = document.getElementById('permissao_id');

    permissao_id_checkbox.addEventListener('change', function () {
      if (permissao_id_checkbox.checked) {
        permissao_id.value = '1';
      } else {
        permissao_id.value = '0';
      }
    });
    permissao_id.value = permissao_id_checkbox.checked ? '1' : '0';
  });

//Função para criar mascara em cpf e celular
  function formatar(mascara, documento){
    var i = documento.value.length;
    var saida = mascara.substring(0,1);
    var texto = mascara.substring(i)
    
    if (texto.substring(0,1) != saida){
              documento.value += texto.substring(0,1);
    }
    
  }