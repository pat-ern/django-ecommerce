/**/
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
                console.log("valor valido");
                document.getElementById("grupo_nombre").classList.remove("error-activo");
                document.getElementById("grupo_nombre").classList.remove("error-icon");
            }else{
                console.log("valor invalido");
                document.getElementById("grupo_nombre").classList.add("error-activo");
                document.getElementById("grupo_nombre").classList.add("error-icon");
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

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
});


$("#enviar").click(function() {
    alert("Enviado");
});