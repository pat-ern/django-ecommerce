/**/
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input')

const expresiones = {
    nombre: /^[a-zA-ZÁ-ÿ\s]{2,40}$/, //letras y espacios
    email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/, //letras y espacios puede llevar acentos
    celular: /^\d{9,11}$/ // 9 a 11 digitos
};

const donacion = document.getElementById("donativo");

const campos = {
    nombre: false,
    email: false,
    celular: false
}

const validarFormulario = (e) => {
    switch (e.target.name){
        case "nombre":
            validarCampo(expresiones.nombre, e.target, e.target.name);
        break;
        case "email":
            validarCampo(expresiones.email, e.target, e.target.name);
        break;
        case "celular":
            validarCampo(expresiones.celular, e.target, e.target.name);
        break;
        case "donativo":
            if(donacion.value>=1000){
                document.getElementById("donativo").classList.remove("borde_error_simple");
            }else{
                document.getElementById("donativo").classList.add("borde_error_simple");
            }
        break;
    }
}

const validarCampo =(expresion, input, campo) => {
    if(expresion.test(input.value)){
        document.getElementById(`grupo_${campo}`).classList.remove("formulario_grupo_incorrecto");
        campos[campo] = true;
    }else{
        document.getElementById(`grupo_${campo}`).classList.add("formulario_grupo_incorrecto");
        campos[campo] = false;
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});


formulario.addEventListener('submit', (e) => {
    e.preventDefault(); //  Previene que se envie


    if(campos.nombre && campos.email && campos.celular && donacion.value>=1000){
        formulario.reset();
        alert("Se envio correctamente");
    }
});
