var Bird = function(options){
    this.x = 80;
    this.y = 250;
    this.width = 40;
    this.gameboardHeight = 30;

    this.alive = true;
    this.gravity = 0;
    this.velocity = 0.3;
    this.jump = -6;

    this.init(options);
}

Bird.prototype.init = function(options){
    for(var i in options){
        this[i] = options[i];
    }
}

Bird.prototype.flap = function(){
    this.gravity = this.jump;
}

Bird.prototype.update = function(){
    this.gravity += this.velocity;
    this.y += this.gravity;
}

Bird.prototype.isDead = function(gameboardHeight, pipes){
    if(this.y >= gameboardHeight || this.y + this.gameboardHeight <= 0){
        return true;
    }
    for(var i in pipes){
        if(!(
            this.x > pipes[i].x + pipes[i].width ||
            this.x + this.width < pipes[i].x ||
            this.y > pipes[i].y + pipes[i].gameboardHeight ||
            this.y + this.gameboardHeight < pipes[i].y
        )){
            return true;
        }
    }
}

