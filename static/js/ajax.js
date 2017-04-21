/**
 * Created by yujian on 17/4/19.
 */
$(function(){
    $("#select_type").change(function(){
    $.post("ajax/", $("#form_id").serialize(), function(data, status){
        if(status == "success"){
              $("#select_re").empty();
            var count = data.count;
                 for (var i=0;i<count;i++){
                    $("#select_re").append('<option>'+data.content[i]+'</option>');
                 }
       }
    });
    })
})


