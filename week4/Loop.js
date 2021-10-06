//declare and initialize a value for a background color variable
var backgroundColor = 0;

function setup() {
  createCanvas(500, 500);
  noLoop ()
  
  stepx = width / 50;
  stepy = height / 50;
  strokeWeight(20);
  colorMode(RGB);
}




function draw() {
  
  background(random(255),random(255),random(255),60);
  stroke(random(255), random(255), random(255));
  strokeWeight(4);

  for (let x = 0; x < width; x += stepx) {
    for (let y = 0; y < height; y += stepy) {
      let rand = random(1); //give it a float between range 0 - 1 
      if (rand < 0.5) {
        point(x, y, x + stepx);
      } else {
        line(x + stepx, y, x, y + stepy);
        line(x, y, x + stepx, y + stepy);
       }
     }
   }
}


