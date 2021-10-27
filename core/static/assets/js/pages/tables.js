document.getElementById('total_amt_of_work').addEventListener("keyup", function() {
console.log(this.value)
 $('#taxable_ta_of_work_span').text(this.value)
});

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
        sendToServer(td.data("id"),value,type,table);
    });
    $(document).on("keypress",".input-data",function(e){
        var key=e.which;
        if(key==13){
            var value=$(this).val();
            var td=$(this).parent("td");
            $(this).remove();
            td.html(value);
            td.addClass("editable");
            var type=td.data("type");
            var table=td.data('table')
            sendToServer(td.data("id"),value,type, table);
        }
    });

    function sendToServer(id,value,type, table){
        console.log(id);
        console.log(value);
        console.log(type);
        console.log.log(table)
        let url;
        switch(table){
            case 'condo':
                url = 'edit-cond'
                break;
            case 'cat':
                url = 'edit-catastal'
                break;
            case 'legal':
                url = 'edit-legal-admin'
                break;
            case 'individual':
                url = 'edit-individual-admin'
        }

        $.ajax({
            url:`http://localhost:8000/${url}`,
            type:"POST",
            data:{id:id,type:type,value:value},
        })
        .done(function(response){
            console.log(response);
        })
        .fail(function(){
           console.log("Error Occured");
        });

    }
});