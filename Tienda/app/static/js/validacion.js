$(document).ready(function(){
    $("#error").hide();
    $("#formulario").submit(function(){
        var mensaje = "";
        if($("#nombre").val().trim().length == 0) {
            mensaje = "El campo de nombre no puede quedar en blanco";
        }
        if($("#apellido").val().trim().length == 0) {
            mensaje = "El campo de apellido no puede quedar en blanco";
        }
        if($("#email").val().trim().length == 0) {
            mensaje = "El campo del correo no puede quedar en blanco";
        }
        // Evitamos que se envien los datos del formulario
        if(mensaje != "") {
            $("#error").html(mensaje);
            $("#error").show();
            event.preventDefault();
        }

    });
})