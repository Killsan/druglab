let shop_butt = document.getElementById('shop_main_div_button');
let shop_div = document.getElementById('shop_main_div');
let videos_butt = document.getElementById('videos_main_button');
let videos_div = document.getElementById('videos_main_div');
let news_butt = document.getElementById('news_main_button');
let news_div = document.getElementById('news_main_div');

shop_div.style.visibility = 'visible';
videos_div.style.visibility = 'hidden';
news_div.style.visibility = 'hidden';
shop_div.hidden = false;
news_div.hidden = true;
news_div.hidden = true;


function shop_func(){
    videos_div.style.visibility = 'hidden';
    videos_div.hidden = true;
    news_div.style.visibility = 'hidden';
    news_div.hidden = true;
    shop_div.style.visibility = 'visible';
    shop_div.hidden = false;
}

function videos_func(){
    videos_div.style.visibility = 'visible';
    videos_div.hidden = false;
    news_div.style.visibility = 'hidden';
    news_div.hidden = true;
    shop_div.style.visibility = 'hidden';
    shop_div.hidden = true;
}

function news_func(){
    videos_div.style.visibility = 'hidden';
    videos_div.hidden = true;
    news_div.style.visibility = 'visible';
    news_div.hidden = false;
    shop_div.style.visibility = 'hidden';
    shop_div.hidden = true;
}

shop_butt.addEventListener('click', shop_func);
videos_butt.addEventListener('click', videos_func);
news_butt.addEventListener('click', news_func);