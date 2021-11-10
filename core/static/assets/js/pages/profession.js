$(document).ready(function(){

    $('#pro-submit').on('click', function(){
        let profession = $('#profession').find(':selected').val()
        let type = $('#type').find(':selected').val()
        let stringUrl = '/prof';
        switch(profession){
            case 'data-designer':
                stringUrl += '/prof=data-designer'
                break;
            case 'data-security-coordinator-design':
                stringUrl += '/prof=data-security-coordinator-design'
                break;
            case 'data-security-coordinator-execution':
                stringUrl += '/prof=data-security-coordinator-execution'
                break;
            case 'director-works':
                stringUrl += '/prof=director-works'
                break;
            case 'thermotechnical':
                stringUrl += '/prof=thermotechnical'
                break;
            case 'data-energy-expert':
                stringUrl += '/prof=data-energy-expert'
                break;
            case 'data-responsible':
                stringUrl += '/prof=data-responsible'
                break;
        }

        if(type == 'individual'){
            stringUrl += '/type=individual'
        }else if(type == 'legal'){
            stringUrl += '/type=legal'
        }
        var fff  = $(location).attr("href").split('/').pop();
        console.log(fff)
        stringUrl += `/fff=${fff}`


        window.location.href = window.location.origin + stringUrl
    })
})