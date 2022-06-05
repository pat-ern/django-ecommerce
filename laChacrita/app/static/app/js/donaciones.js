$(document).ready(function(){
  $("#nombre").blur(function() {
    $("#nombre").valid();
  });

  $("#correo").blur(function() {
    $("#correo").valid();
  });

  $("#telefono").blur(function() {
    $("#telefono").valid();
  });

  $("#monto").blur(function() {
    $("#monto").valid();
  });

  document.querySelector("#enviar-btn").addEventListener("click", ()=> {
    if ($("#formulario").valid()){
    } else {
        alert("Debes ingresar todos los campos.");
    }
  });
  
});