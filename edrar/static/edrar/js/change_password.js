/** 
 * JS for changing password
 **/

 $(document).ready(function(){
    old_password = $('#old-password');
    new_password = $('#old-password');
    confirm_password = $('#old-password');
    passwords = {'old': old_password, 'new': new_password, 'confirm': confirm_password}

    function validate(){
        for([key, obj] of Object.entries(passwords)){
            if(!obj.val()){
                return {'valid': false, 'message': `${obj.attr('name')} can not be empty.`};
            }
        }

        if(new_password.val() != confirm_password.val()){
            return {'valid': false, 'message': 'New password did not match.'};
        }

        return {'valid': true, 'message': 'Passed.'};
    }

    $('#submit-new-pwd').click(function(e){
        e.preventDefault();
        validate();
    });
 });

