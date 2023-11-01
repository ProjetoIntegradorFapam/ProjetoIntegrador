//altera opacidade de itens ul
ul = document.getElementById('message')
  
if (ul) {
    setTimeout(() => {
    ul.style.opacity = '0'
    },3000)
}

//Função para criar mascara em cpf e celular
function formatar(mascara, documento){
  let i = documento.value.length;
  let saida = mascara.substring(0,1);
  let texto = mascara.substring(i)
  
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

//alterando display dos toasts
const toast = document.getElementById('toast')

if (toast) {
  setTimeout(() => {
    toast.style.display = 'none';
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


//alterando tema
const themeButton = document.getElementById("theme-button")

themeButton.addEventListener("change", function() {
  //Alterando tema com checkbox
  let element = document.documentElement;
  let logo_dark = document.getElementById("theme-logo-dark")
  let logo_light = document.getElementById("theme-logo-light")

  // Acesse o atributo data-bs-theme usando dataset
  let dataTheme = element.dataset.bsTheme;

  // Verifique se o valor do atributo é "dark"
  if (dataTheme === 'light' && themeButton.checked) {
    element.dataset.bsTheme = 'dark';
    logo_dark.style.display = "block";
    logo_light.style.display = "none";
  } else {
    element.dataset.bsTheme = 'light';
    logo_light.style.display = "block";
    logo_dark.style.display = "none";
  }
}) 
