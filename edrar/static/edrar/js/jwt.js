//Setting JWT Cookie for API Calls
var jwt = null;
var jwt_refresh = null;
var current_time = new Date().getTime() / 1000;

async function get_jwt_token(){
    const token = await fetch('/api/user/token/');
    return token.json();
}

function set_jwt_token_cookie(){
    get_jwt_token().then(function(result){
        jwt = result.access;
        jwt_refresh = result.refresh;
        Cookies.set('aid-user-id', result.user_id,  {expires: 1});
        Cookies.set('aid-user', result.user,  {expires: 1});
        Cookies.set('aid-token-access', jwt,  {expires: 1});
        Cookies.set('aid-token-refresh', jwt_refresh,  {expires: 1});
    }).catch((e) => console.log(e));
}

function decode_jwt(token){
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
};

if (!Cookies.get('aid-token-access') && !Cookies.get('aid-token-refresh')) {
    set_jwt_token_cookie();
}else{
    let logged_user = $('#user-name').attr('data-id') || null;
    jwt = Cookies.get('aid-token-access');
    jwt_refresh = Cookies.get('aid-token-refresh');
    if(Cookies.get('aid-user-id') != logged_user){
        set_jwt_token_cookie();
    }
}

var jwt_decoded = decode_jwt(jwt);
if(current_time > jwt_decoded.exp) { set_jwt_token_cookie() }
console.log(Cookies.get('aid-token-access'));