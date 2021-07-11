$(document).ready(function() {
    
    $("button#generateKey").click(function(){
        alert('Hello World!');
        $.ajax({
            type: 'POST',
            url: 'http://10.150.20.102:8000/api/token/',
            success: function(response, status, xhr){
                if(status){
                    $("#id_apiusertoken_set-0-access_token").val(response.access_token);
                    $("#id_apiusertoken_set-0-refresh_token").val(response.refresh_token);
                }else{
                    alert(status);
                }
            },
            error: function(xhr, status, errStr){
                alert(errStr);
            },
            cache: false
        });
    });

});
