$(document).ready(function(){

    $('#pro-submit').on('click', function(){
        let profession = $('#profession').find(':selected').val()
        let type = $('#type').find(':selected').val()
        let stringUrl = '/prof';
        console.log(profession, type)
        switch(profession){
            case 'data-designer':
                stringUrl += '/dd'
                break;
            case 'data-security-coordinator-design':
                stringUrl += '/dscd'
                break;
            case 'data-security-coordinator-execution':
                stringUrl += '/dsce'
                break;
            case 'directory-works':
                stringUrl += '/dw'
                break;
            case 'thermotechnical':
                stringUrl += '/tt'
                break;
            case 'data-energy-expert':
                stringUrl += '/dee'
                break;
            case 'data-responsible':
                stringUrl += '/dr'
                break;
        }

        if(type == 'individual'){
            stringUrl += 'i/'
        }else if(type == 'legal'){
            stringUrl += 'l/'
        }
        console.log(stringUrl)
        window.location.href = window.location.origin + stringUrl
    })
})