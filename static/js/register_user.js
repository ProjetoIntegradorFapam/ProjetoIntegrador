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