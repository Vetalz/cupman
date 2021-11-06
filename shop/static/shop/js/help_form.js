let help_form = {
    name: '',
    phone: ''
}

let phoneMask = IMask(
  document.getElementById('phone'), {
    mask: '+{38}(000)000-00-00',
    lazy: false,
    placeholderChar: '_'
  });

function validate_phone(phone){
    let result = phone.match(/^\+38\(\d{3}\)\d{3}-\d{2}-\d{2}$/);
    if (result){
        return true;
    }
}

function send_help_form (el){
    let token =  $('input[name="csrfmiddlewaretoken"]').attr('value');
    let el_name = document.getElementById('name');
    let el_phone = document.getElementById('phone');
    let el_error = document.getElementById('error');
    let el_success = document.getElementById('success');
    let el_spinner = document.getElementById('spinner');
    let result = validate_phone(el_phone.value)
    if (result){
        help_form['name'] = el_name.value;
        help_form['phone'] = el_phone.value;
        el_error.classList.add('hidden');
        el_spinner.classList.toggle('hidden')
        $.ajax({
            type: "POST",
            headers: {'X-CSRFToken': token},
            url: "/help-form/",
            data: {
                'name': help_form['name'],
                'phone': help_form['phone']
            },
            success: function (response) {
                if(response.status === 'OK'){
                    el_spinner.classList.toggle('hidden');
                    el_success.classList.remove('hidden');
                    el.classList.add('hidden');
                }
            }
        });
    }
    else{
        el_error.classList.remove('hidden');
    }
}