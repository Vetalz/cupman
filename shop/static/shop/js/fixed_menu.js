window.onscroll = function() {
  let scrolled = window.window.pageYOffset;
  if (scrolled > 0){
    document.getElementById('menu').classList.add('bg_color');
  }
  else {
    document.getElementById('menu').classList.remove('bg_color');
  }
}

document.getElementById("navbar-toggler").addEventListener("click", function() {
  document.getElementById('menu').classList.add('bg_color');
});