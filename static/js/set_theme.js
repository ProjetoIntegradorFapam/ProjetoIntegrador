const themes = {
    light: {
      background: '#EAECEE',
      background2: '#f2f2ff',
      text: '#313d49',
      favicon: 'url(../img/favicon.png)'
    },
    dark: {
      background: '#2b3641',
      background2: '#313d49',
      text: '#f2f2ff',
      favicon: 'url(../img/favicon_dark.png)'
    }
};

const darkModeToggle = document.querySelector('input[name=theme]');

darkModeToggle.addEventListener('change', function({ target }) {
  setTheme(target.checked ? 'dark' : 'light');
});

function setTheme(newTheme) {
    const themeColors = themes[newTheme]; // Seleciona o tema para aplicar
  
    Object.keys(themeColors).map(function(key) {
        document.querySelector('html').style.setProperty(`--${key}`, themeColors[key]); // Altera as variáveis no css
        document.querySelector('#logo').style.setProperty(`background-image: ${key};)`, themeColors[key]);
    });
  
    localStorage.setItem('theme', newTheme); //Salva o tema escolhido no localStorage
}

  const theme = localStorage.getItem('theme');
  if( theme ) {
    setTheme(theme)
  }
