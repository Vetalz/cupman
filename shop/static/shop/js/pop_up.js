let el_pop_up = document.getElementById('pop-up');

function close_pop_up(){
    el_pop_up.classList.remove('pop-up-active')
}

let updateTime=function(){
    el_pop_up.classList.add('pop-up-active')
}

setTimeout(updateTime,15000);
clearTimeout(updateTime);