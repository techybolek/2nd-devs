
class Wave {
   constructor(canvasId) {
     this.canvas = document.getElementById(canvasId);
     this.ctx = this.canvas.getContext('2d');
     this.canvas.width = window.innerWidth;
     this.canvas.height = window.innerHeight;
   }
 
   drawWave() {
     let waveLength = 0.01;
     let amplitude = 100;
     let frequency = 0.01;
     this.ctx.beginPath();
     for(let i = 0; i < this.canvas.width; i++) {
       let y = this.canvas.height / 2 + amplitude * Math.sin(waveLength * i + frequency);
       this.ctx.lineTo(i, y);
     }
     this.ctx.strokeStyle = '#f0f0f0';
     this.ctx.lineWidth = 5;
     this.ctx.stroke();
   }
 }
 
 window.onload = () => {
    console.log('on load')
 };
 document.addEventListener('DOMContentLoaded', function() {
   console.log('loaded')
   const wave = new Wave('wave');
   wave.drawWave();
});