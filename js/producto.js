$(document).ready(function(){
    $("#div-comentarios").hide();
    $("#cuerpo-comentar").hide();

    $("#btn-toggle").click(function(){
        $("#div-comentarios").slideToggle(800);
      });

    $("#btn-toggle-2").click(function(){
        $("#cuerpo-comentar").slideToggle(400);
    });

    $("#comentario-txt").blur(function() {
        $("#comentario-txt").valid();
      });

    $("#usuario-txt").blur(function() {
        $("#usuario-txt").valid();
    });

});

//Creacion de un arreglo en javascript
const comentarios = []; // permite almacenar objetos

const cargarComentarios = ()=>{
    //selecionar el tbody
    const tbody = document.querySelector("#tabla-tbody");
    tbody.innerHTML = "";
    // recorrer el arreglo
    for(let i=0; i < comentarios.length; ++i){
        let c = comentarios[i];
        // por cada objeto crear una fila
        let fila = document.createElement("tr");
        // por cada atributo generar celda
        let celdaComentario = document.createElement("td");
        celdaComentario.innerText = c.comentario;
        let celdaUsuario = document.createElement("td");
        celdaUsuario.innerText = c.usuario;
        // agregar cada celda a la fila
        fila.appendChild(celdaComentario);
        fila.appendChild(celdaUsuario);
        // agregar la fila al cuerpo de la tabla
        tbody.appendChild(fila);
    }
};

//Agregar un listener para el evento click
document.querySelector("#enviar-btn").addEventListener("click", ()=> {
    if ($("#comentario-txt").valid() && $("#usuario-txt").valid()){
        let comentario = document.querySelector("#comentario-txt").value;
        let usuario = document.querySelector("#usuario-txt").value;
        let entrada = {}; // objeto, permite definir muchas propiedades
        entrada.comentario = comentario;
        entrada.usuario = usuario;
        comentarios.push(entrada);
        cargarComentarios();        
        $("#comentario-txt").val('');
        $("#usuario-txt").val('');
        $("#cuerpo-comentar").hide();
        alert("Comentario enviado.");
    } else {
        alert("Debes ingresar todos los campos.");
    }
});

const commentForm = document.getElementById('commentForm');

commentForm.addEventListener('submit', (e) => {
    e.preventDefault(); //  Previene que se envie
});