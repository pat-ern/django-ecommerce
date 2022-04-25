/*
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input')

const expresiones = {
    nombre: /^[a-zA-ZÁ-ÿ\s]{2,40}$/, //letras y espacios
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\[a-zA-Z0-9-.]+$/, //letras y espacios puede llevar acentos
    telefono: /^\d{8,11}$/ // 8 a 11 numeros
};

const validarFormulario = (e) => {
    switch (e.target.name){
        case "nombre":
            if(expresiones.nombre.test(e.target.value)){
                document.getElementsByClassName("error_formulario").classList.remove("error-activo");
                document.getElementsByClassName("img_error").classList.remove("error-icon");
            }else{
                document.getElementsById("grupo_nombre").classList.add("error-activo");
            }
        break;
        case "email":

        break;
        case "celular":

        break;
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});
*/

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
});


$("#enviar").click(function() {
    alert("Enviado");
});