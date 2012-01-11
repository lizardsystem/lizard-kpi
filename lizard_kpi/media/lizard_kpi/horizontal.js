
function initialize_horizontal_gauges() {
  $(".horizontal-gauge").each(function() {
    // Configuration.
    var number_of_ticks = 40;
    var max_value = 10;
    // Initialization.
    var $bar = $(this);
    var value = $bar.attr('data-value');
    var tick_value = value / max_value * number_of_ticks;
    console.log(tick_value);
    var height = $bar.innerHeight();
    var middle = height / 2;
    var width = $bar.innerWidth();
    var total_tick_width = width / number_of_ticks;
    var tick_width = 0.75 * total_tick_width;
    var canvas = Raphael(this, width, height);
    console.log(canvas);
    // Demo draw;
    for (var i = 0; i < number_of_ticks; i++) {
      var from = (i * total_tick_width) + ' ' + middle;
      var to = (i * total_tick_width + tick_width) + ' ' + middle;
      var path_string = 'M' + from + 'L' + to;
      var hue;
      if (i < number_of_ticks * 0.5) {
        hue = 90 / 360;  // green
      } else if (i < number_of_ticks * 0.75) {
        hue = 60 / 360;  // yellow
      } else {
        hue = 0;  // red
      }
      var saturation;
      var brightness;
      if (i < tick_value) {
        brightness = 1;
        saturation = 1;
      } else {
        brightness = 1;
        saturation = 0.1;
      }
      var color = "hsb(".concat(hue, ",", saturation, ",", brightness, ")");
      var path_params = {"stroke": color,
                         "stroke-width": height};
      canvas.path(path_string).attr(path_params);
    }
  });
}




$(document).ready(function () {
  initialize_horizontal_gauges();
});
