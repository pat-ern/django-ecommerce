$(document).ready(function(){
    $("#div-comentarios").hide();

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