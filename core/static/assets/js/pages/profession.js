$(document).ready(function(){

    $('#pro-submit').on('click', function(){
        let profession = $('#profession').find(':selected').val()
        let type = $('#type').find(':selected').val()
        let stringUrl = '/prof';
        switch(profession){
            case 'data-designer':
                stringUrl += '/?profession=data-designer'
                break;
            case 'data-security-coordinator-design':
                stringUrl += '/?profession=data-security-coordinator-design'
                break;
            case 'data-security-coordinator-execution':
                stringUrl += '/?profession=data-security-coordinator-execution'
                break;
            case 'director-works':
                stringUrl += '/?profession=director-works'
                break;
            case 'thermotechnical':
                stringUrl += '/?profession=thermotechnical'
                break;
            case 'data-energy-expert':
                stringUrl += '/?profession=data-energy-expert'
                break;
            case 'data-responsible':
                stringUrl += '/?profession=data-responsible'
                break;
        }

        if(type == 'individual'){
            stringUrl += '&type=individual'
        }else if(type == 'legal'){
            stringUrl += '&type=legal'
        }

        window.location.href = window.location.origin + stringUrl
    })
})