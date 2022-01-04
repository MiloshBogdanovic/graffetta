  $(document).ready(function(){
      $('.trclick').click(function(){
        window.location = $(this).data('href');
        return false;
      });
    });