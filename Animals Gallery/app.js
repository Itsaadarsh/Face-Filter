function cats() {
  let img = new Image();
  let div = document.getElementById('gen');
  img.src = "img/cat/cat" + (Math.floor(Math.random() * 5) + 1) + ".jpg";
  div.appendChild(img);
}

function dogs() {
  let img = new Image();
  let div = document.getElementById('gen');
  img.src = "img/dog/dog" + (Math.floor(Math.random() * 5) + 1) + ".jpg";
  div.appendChild(img);
}

function tiger() {
  let img = new Image();
  let div = document.getElementById('gen');
  img.src = "img/tiger/tig" + (Math.floor(Math.random() * 5) + 1) + ".jpg";
  img.id = "tig-id";
  div.appendChild(img);
  console.log(document.getElementById('tig-id'));
}

function elephant() {
  let img = new Image();
  let div = document.getElementById('gen');
  img.src = "img/elephant/ele" + (Math.floor(Math.random() * 5) + 1) + ".jpg";
  div.appendChild(img);
}

function clearing() {
  location.reload();
}
