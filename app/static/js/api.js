$(document).ready(function(){
    $("#enviar").click(function(){
    $.get("https://www.el-tiempo.net/api/json/v2/home",
    function(data){
        // En data sse captura todos los datos provenientes del servicio
        $.each(data.ciudades, function(i, item){
            // Por cada element agregaremos una nueva fila en la tablña categorias
            $("#ciudad").append("<tr><td>"+item.idProvince+"</td>"+
                                    "<td>"+item.name+"</td>"+
                                    "<td>"+item.nameProvince + "</td>" +
                                    "<td>"+item.temperatures.max+"</td>" +
                                    "<td>"+item.temperatures.min+"</td></tr>" );
            });

        });
    });
})