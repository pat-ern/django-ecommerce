$(document).ready(function(){
    $("#all_subs").show();
    $("#active_subs").hide();

    $("#all-subs").click(function(){
        $("#all_subs").show();
        $("#active_subs").hide();
    });

    $("#on-subs").click(function(){
        $("#all_subs").hide();
        $("#active_subs").show();
    });

});