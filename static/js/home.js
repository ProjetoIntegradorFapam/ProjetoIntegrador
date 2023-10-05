let current_theme = 'light';

let elements = []
let getelements = document.getElementsByClassName('*');

getelements.forEach(element => {
  elements.push(element)
});

function change_theme(theme) {

  if (current_theme == theme) {
    window.alert('O tema escolhido já está em uso!')
  } else {

    for (var i = 0; i < elements.length; i++) {
        // Adiciona ou remove classes conforme necessário
        elements[i].classList.add(`${theme}`);
        elements[i].classList.remove(`${current_theme}`);
    }
  
    current_theme = theme
  }
}