const menuButton = document.getElementById("menuBars");
const menuIcon = document.getElementById("menuIcon");
const menuList = document.getElementById("menuList");
const main = document.querySelector('main');

// Function toggles classes on menBars click
function mobileMenu() {
  menuIcon.classList.toggle("fa-x");
  menuIcon.classList.toggle("rotate");
  menuList.classList.toggle("inactive");
  main.classList.toggle('main-filter')
}

var qoutes = [
  "“Cyber-Security is much more than a matter of IT.” ― Stephane Nappo",
  "“Passwords are like underwear: do’t let people see it, change it very often, and you shouldn’t share it with strangers.” – Chris Pirillo",
  "“I really think that if we change our own approach and thinking about what we have available to us, that is what will unlock our ability to truly excel in security. It’s a perspectives exercise. What would it look like if abundance were the reality and not resource constraint?”  — Greg York",
  "“It takes 20 years to build a reputation and few minutes of cyber-incident to ruin it.” – Stephane Nappo",
  "“As we’ve come to realize, the idea that security starts and ends with the purchase of a prepackaged firewall is simply misguided.” – Art Wittmann",
  "“As cybersecurity leaders, we have to create our message of influence because security is a culture and you need the business to take place and be part of that security culture.”  — Britney Hommertzheim",
  "“We discovered in our research that insider threats are not viewed as seriously as external threats, like a cyberattack. But when companies had an insider threat, in general, they were much more costly than external incidents. This was largely because the insider that is smart has the skills to hide the crime, for months, for years, sometimes forever.”  — Dr. Larry Ponemon",
  "“The knock-on effect of a data breach can be devastating for a company. When customers start taking their business—and their money—elsewhere, that can be a real body blow.” – Christopher Graham"
]


  var randomNumber = Math.floor(Math.random() * qoutes.length);
  document.getElementById('quotesdisplay').innerHTML = qoutes[randomNumber];

  function todayDate(){
    var d = new Date();
    var n = d.getFullYear() + "  ";
    return document.getElementById("date").innerHTML = n;
  }

$(document).ready(function() {
    $('#bookModal').modal({
      show: false,
      backdrop: 'static'
    });
  });