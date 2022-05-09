$(document).ready(function(){
  $("#efecto_mision_vision").click(function(){
    $("#mision_vision").slideToggle(1000);
    $("#nuestra_historia").slideToggle(1000);
  });

  $(".efecto_nuestra_historia").click(function(){
    $("#nuestra_historia").slideToggle(1000);
    $("#mision_vision").slideToggle(1000);
  });
});