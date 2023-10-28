//Receber 0 ou 1 do checkbox para a coluna permissao_id no bd...
document.addEventListener('DOMContentLoaded', function () {
    const permissao_id_checkbox = document.getElementById('permissao_id_checkbox');
    const permissao_id = document.getElementById('permissao_id');
    
    //acionando campo senha
    const password_field = document.getElementById('password-field')

    permissao_id_checkbox.addEventListener('change', function () {
      if (permissao_id_checkbox.checked) {
        permissao_id.value = '1';
        password_field.classList.remove('hidden')
        password_field.classList.add('show')
      } else {
        permissao_id.value = '0';
        password_field.classList.remove('show')
        password_field.classList.add('hidden')
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

  //Máscara de telefone para input 
  const handlePhone = (event) => {
    let input = event.target
    input.value = phoneMask(input.value)
  }
  
  const phoneMask = (value) => {
    if (!value) return ""
    value = value.replace(/\D/g,'')
    value = value.replace(/(\d{2})(\d)/,"($1) $2")
    value = value.replace(/(\d)(\d{4})$/,"$1-$2")
    return value
  }

const toastLiveExample = document.getElementById('liveToast')

if (toastLiveExample) {
  setTimeout(() => {
    toastLiveExample.style.display = 'none';
  },5000)
}

// Fetch all the forms we want to apply custom Bootstrap validation styles to
const forms = document.querySelectorAll('.needs-validation')

// Loop over them and prevent submission
Array.from(forms).forEach(form => {
  form.addEventListener('submit', event => {
    if (!form.checkValidity()) {
      event.preventDefault()
      event.stopPropagation()
    }

    form.classList.add('was-validated')
  }, false)
})