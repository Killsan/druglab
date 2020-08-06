let auth_butt = document.getElementById('auth');
let reg_butt = document.getElementById('reg');
let auth_div = document.getElementById('auth_div');
let reg_div = document.getElementById('reg_div');

auth_div.style.visibility = 'hidden';
reg_div.style.visibility = 'hidden';

function auth_windows(){
    if(auth_div.style.visibility === 'hidden'){
        if(reg_div.style.visibility === 'hidden'){
            auth_div.style.visibility = 'visible';
        }else{
            reg_div.style.visibility = "hidden";
            auth_div.style.visibility = "visible";
        }
    }else{
        auth_div.style.visibility = "hidden";
    }
}

function reg_windows(){
    if(reg_div.style.visibility === 'hidden'){
        if(auth_div.style.visibility === 'hidden'){
            reg_div.style.visibility = 'visible';
        }else{
            auth_div.style.visibility = "hidden";
            reg_div.style.visibility = "visible";
        }
    }else{
        reg_div.style.visibility = "hidden";
    }
}

auth_butt.addEventListener("click", auth_windows);
reg_butt.addEventListener("click", reg_windows);