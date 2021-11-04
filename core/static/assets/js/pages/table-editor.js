$(document).ready(function(){
    $(document).on("dblclick",".editable",function(){
        var value=$(this).text();
        var data_type=$(this).data("type");
        var input_type="text";
        if(data_type=="created_at")
        {
            input_type="datetime-local";
        }
        var input="<input type='"+input_type+"' class='input-data' value='"+value+"' class='form-control'>";
        $(this).html(input);
        $(this).removeClass("editable")
    });

    $(document).on("blur",".input-data",function(){
        var value=$(this).val();
        var td=$(this).parent("td");
        $(this).remove();
        td.html(value);
        td.addClass("editable");
        var type=td.data("type");
        var table=td.parent('tr').data('table')
        console.log(table)
        sendToServer(td.parent('tr').data('id'),value,type,table);
    });
    $(document).on("keypress",".input-data",function(e){
        var key=e.which;
        if(key==13){
            var value=$(this).val();
            var td=$(this).parent("td");
            $(this).remove();
            td.html(value);
            td.addClass("editable");
            var id = td.parent('tr').data('id')
            var type=td.data("type");
            var table=td.parent('tr').data('table')

            sendToServer(id,value,type, table);
        }
    });

    function sendToServer(id,value,type, table){
        console.log(id);
        console.log(value);
        console.log(type);
        console.log(table)
        let url = 'edit-table-data';
        let token = $('[name="csrfmiddlewaretoken"]').val()
        

        $.ajax({
            url:`http://localhost:8000/${url}`,
            type:"POST",
            data:{id:id,type:type,value:value, table: table, csrfmiddlewaretoken: token},
            dataType: 'json'
        })
        .done(function(response){
            console.log(response);
        })
        .fail(function(){
           console.log("Error Occured");
        });

    }
});