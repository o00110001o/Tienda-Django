$(document).ready(function(){
    $("#enviar").click(function(){
        $.get("http://jsonplaceholder.typicode.com/users",
            function(data){
            // En data se capturan todos los datos provenientes desde el servivio
            $.each(data, function(i, item){
            //Por cada elemento agregaremos una nueva fila en la tabla categorias
            $("#Clientes").append("<tr><td>"+item.id+"</td>"+
                                    "<td>"+item.name+"</td>"+
                                  "<td>" +item.email+"</td>"+
                                  "<td>"+item.address.street+"</td></tr>");
                                  
        });
    });
});
})