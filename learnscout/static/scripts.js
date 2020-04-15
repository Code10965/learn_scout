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
}
  
