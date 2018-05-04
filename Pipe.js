var Pipe = function(options){
    this.x = 0;
    this.y = 0;
    this.width = 50;
    this.height = 40;
    this.speed = 3;

    this.init(options);
}

Pipe.prototype.init = function(options){
    for(var i in options){
        this[i] = options[i];
    }
}

Pipe.prototype.update = function(){
    this.x -= this.speed;
}

Pipe.prototype.isOut = function(){
    if(this.x + this.width < 0){
        return true;
    }
}

