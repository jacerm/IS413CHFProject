$(function() {
    $('#loginButton').click(function(){
       $.loadmodal({
        url: '/account/login',
        id: 'login_modal_id',
        title: 'Login Here',
        width: '400px'
       });
    });
});