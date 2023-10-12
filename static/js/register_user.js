document.getElementById("register_user_form").addEventListener("submit", function (event) {
    
    const inputs = document.getElementByClass("form-control");

    for(input of inputs) {

        if (!input.value) {
            event.preventDefault();
            return;
        }
    }
});