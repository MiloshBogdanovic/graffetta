
  $(document).ready(function(){
      $('.row-link').click(function(){
        window.location = $(this).data('href');
        return false;
      });
    });