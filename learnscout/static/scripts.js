function responsive_NavBar() {
  var x = document.getElementById("navBar");
  if (x.className === "nav") {
    x.className += " responsive";
  } else {
    x.className = "nav";
  }
}

function responsive_welcome() {
  var res = document.querySelectorAll("#welcome_hide");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="none";
  }

  document.getElementById("change_bg").style="background-image: url(/static/background_blank.jpg)";
  document.getElementById("login_outer").style.backgroundColor= "#49859b";

  var res = document.querySelectorAll("#register_visible");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="none";
  }
  var res = document.querySelectorAll("#login_visible");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="block";
  }
  var res = document.querySelectorAll("#terms_visible");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="none";
  }
}

function responsive_login() {
  var res = document.querySelectorAll("#welcome_hide");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="none";
  }
  var res = document.querySelectorAll("#login_visible");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="none";
  }
  var res = document.querySelectorAll("#register_visible");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="block";
  }
  var res = document.querySelectorAll("#terms_visible");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="none";
  }
}

function responsive_register() {
  var res = document.querySelectorAll("#welcome_hide");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="none";
  }
  var res = document.querySelectorAll("#login_visible");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="none";
  }
  var res = document.querySelectorAll("#register_visible");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="none";
  }
  var res = document.querySelectorAll("#terms_visible");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="block";
  }
}
/*
function highlight_footer() {
  document.getElementById("terms").style.display = "block";
}

function highlight_footer() {
  var x = document.getElementById("terms");
  if (x.className === "footer") {
    x.className += " fade";
  } else {
    x.className = "footer";
  }
}*/

//SCRIPT FOR T&C FRAME
function openFrame() {
  var x = document.getElementById("conditions");
  if (x.className === "aside") {
    x.className += " post";
  } else {
    x.className = "aside";
  }
}
function closeFrame() {
  var x = document.getElementById("conditions");
  if (x.className === "aside") {
    x.className -= " post";
  } else {
    x.className = "aside";
  }
}
