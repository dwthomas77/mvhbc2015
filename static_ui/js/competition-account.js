$(document).ready(function(){

$('.submission-form select').change(function(e){
    if(!$(e.target).val()){
        $('#submissionAddNew').prop("disabled", true);
    }else{
        $('#submissionAddNew').prop("disabled", false);
    }

})



});