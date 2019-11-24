$('document').ready(function(){
    console.log(window.location);

    $('#submit').click(function() {
        var url = "./#catalog/";
        url += $('#ek').val();
        window.location = url;
    });

    $('#ek').keypress(function(e){
      if(e.which == 13){ //Enter key pressed
        var url = "./?#catalog/";
        url += $('#ek').val();
        window.location = url;
      }
  	});
});
