/* Raphaël Gauge 
 * Author: Renato Albano (renatoalbano.com) ~ http://github.com/renatoalbano 
 * Licensed under the MIT (http://www.opensource.org/licenses/mit-license.php) license.
 * Version: 1.0 (Jul 06 2010)
 */

(function (Raphael) {
  Raphael.fn.gauge = function(minAngle, maxAngle) {
    var minAngle = minAngle || 0;
    var maxAngle = maxAngle || 360;
    var actualAngle = minAngle;
    var bgCenter, pointerCenter = null;
    var bg = this.set();
    var pointer = this.set();

    this.animateMS = 1000;
    this.animateEasing = "elastic";
    
    this.bg = function(el, center) {
      bgCenter = center;
      if(pointerCenter != null) {
        pointer.toFront();
        pointer.attr({
          x: bgCenter[0]-pointerCenter[0],
          y: bgCenter[1]-pointerCenter[1]
        });
        this.moveToAngle(actualAngle);
      }
      bg.push(el);
    };
    
    this.pointer = function(el, center) {
      // if bg not exists use center point
      bgCenter = bgCenter || [parseInt(this.width/2), parseInt(this.height/2)];
      pointerCenter = center;
      el.attr({
           x: bgCenter[0]-center[0],
           y: bgCenter[1]-center[1],
           rotation: minAngle + " " + bgCenter[0] + " " + bgCenter[1]
         });
      pointer.push(el);
    };
    
    this.moveToAngle = function(angle) {
      pointer.animate({rotation: angle + " " + bgCenter[0] + " " + bgCenter[1]}, 0);
    };
    
    this.animateToAngle = function(angle) {
      actualAngle = angle;
      pointer.animate(
        {rotation: angle + " " + bgCenter[0] + " " + bgCenter[1]},
        this.animateMS,
        this.animateEasing);
    };
    
    this.move = function(percent, animate) {
      animate = animate == null ? true : animate;
      if(percent < 0) {
        percent = 0
      } else if(percent > 100) {
        percent = 100
      }
    
      var angle = (percent * ((maxAngle-minAngle)/100)) + minAngle;
      if(animate) {
        this.animateToAngle(angle)
      } else {
        this.moveToAngle(angle);
      }
    };
    
    this.minAngle = function(angle) { minAngle = angle; }
    this.maxAngle = function(angle) { maxAngle = angle; }
    
    return this;
  };
})(window.Raphael);