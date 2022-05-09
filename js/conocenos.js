$(document).ready(function(){
  $("#mision-vision").hide();

  $(".btn-mision").click(function(){
    $("#mision-vision").slideToggle(1000);
    $("#nuestra-historia").slideToggle(1000);
  });

  $(".btn-historia").click(function(){
    $("#nuestra-historia").slideToggle(1000);
    $("#mision-vision").slideToggle(1000);
  });
});