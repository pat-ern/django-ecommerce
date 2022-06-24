$(document).ready(function(){
    $("#div-comentarios").show();

    $("#btn-toggle").click(function(){
        $("#div-comentarios").slideToggle(800);
      });

});

$(document).on('submit', '#commentForm', function(e){
  e.preventDefault();
  
  $.ajax({
    type: 'POST',
    url:'',
    data: {
      usuario: $('#id_usuario').val(),
      puntuacion: $('#id_puntuacion').val(),
      comentario: $('#comentario-txt').val(),
      csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    },
    success: function(){
     
      Swal.fire({
        "title":"Enviado",
        "text":"Comentario enviado.",
        "icon":"success",
        "confirmButtonColor":"#558F67"
      })
      .then(function(){ 
        location.reload();
      })
    }
  })

});

function eliminarCalificacion(id){
  Swal.fire({
      "title":"¿Estás seguro?",
      "text":"Puedes calificar el producto de nuevo.",
      "icon":"warning",
      "showCancelButton":true,
      "cancelButtonText": "No, cancelar",
      "confirmButtonText": "Si, eliminar",
      "reverseButtons":true,
      "confirmButtonColor":"#558F67",
      "cancelButtonColor":"#dc3545"
  })
  .then(function(result){
      if(result.isConfirmed){
          window.location.href="/eliminarcalificacion/"+id+"/"
      }
  })
}