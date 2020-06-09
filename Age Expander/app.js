function inputAge() {
  ipAge = prompt('Enter Your Age : ');
}

function months() {
  document.querySelector("button.disbtn1").disabled = true;
  let calMonth = ipAge * 12;
  let output = document.createElement('h2');
  let res = document.createTextNode("YOU ARE  " + calMonth + " MONTHS OLD");
  output.setAttribute('id', 'ageinMonths');
  output.appendChild(res);
  document.getElementById('result').appendChild(output);
  document.getElementById('result').style.textAlign = "center";
  document.getElementById('ageinMonths').style.fontWeight = "bold";
  document.getElementById('ageinMonths').style.fontSize = "3rem";
}

function weeks() {
  document.querySelector("button.disbtn2").disabled = true;
  let calWeeks = Math.round(ipAge * 52.1429);
  let output = document.createElement('h2');
  let res = document.createTextNode("YOU ARE  " + calWeeks + " WEEKS OLD");
  output.setAttribute('id', 'ageinWeeks');
  output.appendChild(res);
  document.getElementById('result').appendChild(output);
  document.getElementById('result').style.textAlign = "center";
  document.getElementById('ageinWeeks').style.fontWeight = "bold";
  document.getElementById('ageinWeeks').style.fontSize = "3rem";
}

function days() {
  document.querySelector("button.disbtn3").disabled = true;
  let calDays = ipAge * 365;
  let output = document.createElement('h2');
  let res = document.createTextNode("YOU ARE  " + calDays + " DAYS OLD");
  output.setAttribute('id', 'ageinDays');
  output.appendChild(res);
  document.getElementById('result').appendChild(output);
  document.getElementById('result').style.textAlign = "center";
  document.getElementById('ageinDays').style.fontWeight = "bold";
  document.getElementById('ageinDays').style.fontSize = "3rem";
}

function minutes() {
  document.querySelector("button.disbtn4").disabled = true;
  let calMinutes = ipAge * 525600;
  let output = document.createElement('h2');
  let res = document.createTextNode("YOU ARE  " + calMinutes + " MINUTES OLD");
  output.setAttribute('id', 'ageinMinutes');
  output.appendChild(res);
  document.getElementById('result').appendChild(output);
  document.getElementById('result').style.textAlign = "center";
  document.getElementById('ageinMinutes').style.fontWeight = "bold";
  document.getElementById('ageinMinutes').style.fontSize = "3rem";
}

function seconds() {
  document.querySelector("button.disbtn5").disabled = true;
  let calSeconds = ipAge * 3.154e+7;
  let output = document.createElement('h2');
  let res = document.createTextNode("YOU ARE  " + calSeconds + " SECONDS OLD");
  output.setAttribute('id', 'ageinSeconds');
  output.appendChild(res);
  document.getElementById('result').appendChild(output);
  document.getElementById('result').style.textAlign = "center";
  document.getElementById('ageinSeconds').style.fontWeight = "bold";
  document.getElementById('ageinSeconds').style.fontSize = "3rem";
}

function clearing() {
  location.reload();
}
