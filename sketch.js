// Constants
const Y_AXIS = 1;
const X_AXIS = 2;
let b1, b2, c1, c2;
var x,y;
var words = [ ['life', 29], ['family', 23], ['people', 18], ['world', 16], ['happiness', 16], ['freedom', 15], ['work', 13], ['tech', 12], ['equality', 12], ['money', 11]];
var categories;
var labels = [ ['family', 0] , ['money', 0] , ['life', 0] , ['equality in the workplace', 0] , ['work', 0] , ['travel', 0], ['education', 0] , ['personal goals', 0], ['retirement', 0], ['emotion', 0] ];
var colours = [];
var begin;

function preload() {
  nouf = loadFont('Taub_Nouf.ttf');
  categories = loadJSON("categories.json");
}

function setup(){
  createCanvas(600,600);

  // Define colors
  b1 = color(255);
  b2 = color(0);
  c1 = color(121, 103, 174);
  c2 = color(242, 99, 93);

  for (let i = 0; i <= width; i++) {
    let inter = map(i, 0, width, 0, 1);
    let c = lerpColor(c1, c2, inter);
    colours.push(c);
  }
}

function draw() {
  background(255);
  begin = 0;
  for (let c=0; c<395;c++){
    let label = categories[c].category;
    for (let l=0; l< labels.length; l++){
      if(labels[l][0] == label){
        labels[l][1] += 1;
      };
    }
  }

  for (let x=0;x<labels.length;x++){
    xPos = random(100,width-100);
    yPos = random(100,height-100);
    push();
    strokeWeight(3);
    fill(colours[begin]);
    ellipse(xPos, yPos, labels[x][1]);
    pop();

    push();
    textFont(nouf);
    textSize(15);
    fill("black");
    text(labels[x][0], xPos, yPos);
    pop();
    begin ++
  }
  noLoop();

  //setGradient(0, 0, width, height, c2, c1, X_AXIS);
  // for (let i=0;i<words.length;i++){
  //   //console.log(words[i]);
  //   fill(random(0,255),random(0,255),random(0,255));
  //   noStroke();
  //   x = random(100,400);
  //   y = random(100,400);
  //   ellipse(x,y,words[i][1]*4)
  //   fill(0);
  //   textFont(nouf);
  //   textSize(20)
  //   text(words[i][0],x,y-10);
  // }
}

function setGradient(x, y, w, h, c1, c2, axis) {
  noFill();

  if (axis === Y_AXIS) {
    // Top to bottom gradient
    for (let i = y; i <= y + h; i++) {
      let inter = map(i, y, y + h, 0, 1);
      let c = lerpColor(c1, c2, inter);
      stroke(c);
      line(x, i, x + w, i);
    }
  } else if (axis === X_AXIS) {
    // Left to right gradient
    for (let i = x; i <= x + w; i++) {
      let inter = map(i, x, x + w, 0, 1);
      let c = lerpColor(c1, c2, inter);
      stroke(c);
      line(i, y, i, y + h);
    }
  }
}
