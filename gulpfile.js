
var gulp = require("gulp");

require("./gulp/js");
require("./gulp/css");
require("./gulp/icons");
// require("./gulp/content");
require("./gulp/clean");
require("./gulp/watch");


gulp.task('build', ['js', 'css', 'icon'], function(done) {
    done();
});

gulp.task('default', ['build']);
