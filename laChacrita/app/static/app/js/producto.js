$(document).ready(function(){
    $("#div-comentarios").show();

    $("#btn-toggle").click(function(){
        $("#div-comentarios").slideToggle(800);
      });

    $("#comentario-txt").blur(function() {
        $("#comentario-txt").valid();
      });

    document.querySelector("#enviar-btn").addEventListener("click", ()=> {
      $("#commentForm").valid();
    });
});