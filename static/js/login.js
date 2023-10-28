function validate() {

    const cpf = document.getElementById("cpf_input");
        const password = document.getElementById("password_input");
    let valid = true;

    if (!cpf.value) {
        const nameError = document.getElementById("nameError");
        nameError.classList.add("visible");
        cpf.classList.add("invalid");
        nameError.setAttribute("aria-hidden", false);
        nameError.setAttribute("aria-invalid", true);
    }

    if (!password.value) {
        const nameError = document.getElementById("nameError");
    nameError.classList.add("visible");
    password.classList.add("invalid");
    nameError.setAttribute("aria-hidden", false);
    nameError.setAttribute("aria-invalid", true);
    }

    setTimeout(() => {
        const nameError = document.getElementById("nameError");
        nameError.classList.remove("visible");
        cpf.classList.remove("invalid");
        password.classList.remove("invalid");
        nameError.setAttribute("aria-hidden", true);
        nameError.setAttribute("aria-invalid", false);
    }, 5000);

    if (cpf.value && password.value) {
        return valid
    } else {
        return false
    }
}