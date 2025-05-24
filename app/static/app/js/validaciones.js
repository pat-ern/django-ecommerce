const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input')

const expresiones = {
    nombre: /^[a-zA-ZÁ-ÿ\s]{2,40}$/, //  letras y espacios
    email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/, //  formato correo
    celular: /^\d{9}$/, // 9 digitos
    frases: /^[a-zA-ZÁ-ÿ\s]{4,400}$/, //  letras y espacios 
};

const donacion = document.getElementById("donativo");
const asunto = document.getElementById("asunto");
const escribenos = document.getElementById("escribenos");

const campos = {
    nombre: false,
    email: false,
    celular: false,
    asunto: false,
    escribenos: false
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
                document.getElementById(e.target.name).classList.remove("borde_error_simple");
            }else{
                document.getElementById(e.target.name).classList.add("borde_error_simple");
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

const validacionVacio = (e) => {
    switch (e.target.name){
        case "asunto":
            if(e.target.value>=1 && e.target.value<=4){
                document.getElementById('asunto').classList.remove("borde_error_simple");
                campos[e.target.name] = true;
            }else{
                document.getElementById('asunto').classList.add("borde_error_simple");
                campos[e.target.name] = false;
            }
        break;
        case "escribenos":
            if(expresiones.frases.test(e.target.value)){
                document.getElementById("escribenos").classList.remove("borde_error_simple");
            }else{
                document.getElementById("escribenos").classList.add("borde_error_simple");
            }
        break;
    }
}

asunto.addEventListener('change', validacionVacio);
asunto.addEventListener('blur', validacionVacio);
escribenos.addEventListener('blur', validacionVacio);
escribenos.addEventListener('keyup', validacionVacio);

formulario.addEventListener('submit', (e) => {
    e.preventDefault(); //  Previene que se envie

    if((campos.nombre && campos.email && campos.celular && donacion.value>=1000)||(campos.email && campos.asunto)){
        formulario.reset();
        alert("Se envio correctamente");
    }
});