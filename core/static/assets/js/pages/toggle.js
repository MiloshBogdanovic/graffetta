
$(document).ready(function() {
     var sPageURL = window.location.href;
     if (sPageURL.includes('cond')){
     $("#pills-cond-tab").trigger("click");
     }else if (sPageURL.includes('individ')){
     $("#pills-individ-tab").trigger("click")
     }else if (sPageURL.includes('flegal')){
     $("#pills-flegal-tab").trigger("click")
     }else if (sPageURL.includes('catast')){
     $("#pills-catast-tab").trigger("click")
     }

     }
);












