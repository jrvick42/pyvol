$("#submit_button").click(function(){

     var file = $("#file").val();
     var opts = $("#options").val();
     var cmnd = $("#command").val();
     // var outf = $("#outputfile").val();

   $.ajax({
     url: "/execute",
     type: "get",
     data: {memfile: file, options: opts, command: cmnd},
     success: function(response) {
       $("#output").html(response);
     },
     error: function(xhr) {
       console.log("Literally no idea what happened")
     }
   });
});
