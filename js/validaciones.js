/**/
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input')

const expresiones = {
    nombre: /^[a-zA-ZÁ-ÿ\s]{2,40}$/, //letras y espacios
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/, //letras y espacios puede llevar acentos
    telefono: /^\d{9,11}$/ // 9 a 11 digitos
};

const campos = {
    nombre: false,
    correo: false,
    telefono: false
}

const validarFormulario = (e) => {
    switch (e.target.name){
        case "nombre":
            validarCampo(expresiones.nombre, e.target, e.target.name);
        break;
        case "email":
            validarCampo(expresiones.correo, e.target, e.target.name);
        break;
        case "celular":
            validarCampo(expresiones.telefono, e.target, e.target.name);
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


    console.log(campos.nombre);
    
    console.log(campos.correo); // Es falso incluso cuando esta correcto, hay que mejorarlo o nunca entrará al if 
    
    console.log(campos.telefono);
    


    if(campos.nombre && campos.correo && campos.telefono){
        formulario.reset();
        alert("Se envio correctamente");
    }
});
