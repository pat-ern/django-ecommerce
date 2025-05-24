$(document).ready(function(){

    $("#btn-all").click(function(){

        $("#on-subs").show();
        $("#off-subs").show();
    });

    $("#btn-on").click(function(){

        $("#on-subs").show();
        $("#off-subs").hide();
    });

    $("#btn-off").click(function(){

        $("#on-subs").hide();
        $("#off-subs").show();
    });

});