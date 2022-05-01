jQuery.extend(jQuery.validator.messages, {
    required: "Este campo é obrigatório",
    email: "Por favor insira um endereço de e-mail válido.",
});


jQuery.validator.addMethod("lettersonly", function(value, element) {
    return this.optional(element) || /^[a-z\s]+$/i.test(value);
    }, "Only alphabetical characters");
    
    
    var valido = $('#MyForm').validate({
            rules: {
                name: {
                    lettersonly: true
                }
            }
    });
    
    console.log(valido);
