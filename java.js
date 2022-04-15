 $.ajax({
        url: 'user/sing-up/',
        type: 'GET',
        dataType: 'json',
        success: function(result){
                $('#image-id').attr('src', result.image);
        },
        error: function(xhr){
               alert(xhr.responseText); //Remove this when all is fine.
        }
 });