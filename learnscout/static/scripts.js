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
  var res = document.querySelectorAll("#login_visible");
  for (var i = 0; i < res.length; i++){
    res[i].style.display="block";
  }
  document.getElementById("login_outer").style.backgroundColor= "#49859b";
  document.getElementById("change_bg").style="background-image: url(/static/background_blank.jpg)";
}
  
