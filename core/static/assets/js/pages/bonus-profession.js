$(document).ready(function(){

    $('#pro-submit').on('click', function(){
        let profession = $('#selectedProfession').find(':selected').val()
        let type = $('#selectedType').find(':selected').val()
        let stringUrl = '';

        if(type == 'individual'){
            stringUrl += '/individual'
        }else if(type == 'legal'){
            stringUrl += '/legal'
        }
        switch(profession){
            case 'data-designer':
                stringUrl += '/data-designer/'
                break;
            case 'data-security-coordinator-design':
                stringUrl += '/data-security-coordinator-design/'
                break;
            case 'data-security-coordinator-execution':
                stringUrl += '/data-security-coordinator-execution/'
                break;
            case 'director-works':
                stringUrl += '/director-works/'
                break;
            case 'thermotechnical':
                stringUrl += '/thermotechnical/'
                break;
            case 'data-energy-expert':
                stringUrl += '/data-energy-expert/'
                break;
            case 'data-responsible':
                stringUrl += '/data-responsible/'
                break;
        }

        var url  = $(location).attr("href")
        window.location.href = url + stringUrl
    })
})