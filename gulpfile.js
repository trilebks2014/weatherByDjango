var DEBUG = ((process.env.DEBUG ? process.env.DEBUG.toLowerCase() : null) == 'true');

var OPTIONS ={
	coffee:{
		bare:true,
		bokens:true
	},
	jade:{
		pretty:true,
		self:false
	}
}

var DIST = "./build/";
var GLOBS = {
	jade:[
	"src/weather/**/*.jade"],
	coffee:[
	"src/weather**/*.coffee"],
	copy_file:['src/weather/**/*','!./**/*.jade']
}
var gulp	=	require("gulp"),
	gultil  =	require("gulp-util"),
	jade	=	require("gulp-jade"),
	coffee = require('gulp-coffee'),
	clean = require('gulp-clean');


function display(error){
	gultil.log(gultil.colors.red(error));
	this.emit('end');

}

gulp.task('clean', function(){
	return gulp.src(DIST, {read: false})
		.pipe(clean());
});
function on_jade_compile(evt) {
  gulp.src(evt.path)
  .pipe(jade_deps({basedir: 'src'}))
  .on("error", display)
  .pipe(debug({title: "jade:"}))
  .pipe(jade(OPTIONS.jade))
  .on("error", display)
  .pipe(gulp.dest(DIST))
}
gulp.task("jade",function(done){
	gulp.src(GLOBS.jade)
		.pipe(jade(OPTIONS.jade))
		.on("error",display)
		.pipe(gulp.dest(DIST))
		.on("end",done);
});
function on_copy_static(evt) {
  gulp.src(evt.path)
    .pipe(debug({title: "static:"}))
    .pipe(gulp.dest(DIST))
}
gulp.task("watch",["build"], function(done) {
  gulp.watch(GLOBS.jade, on_jade_compile)
  // gulp.watch(GLOBS.coffee, on_coffee_compile)
  gulp.watch(GLOBS.copy_file, on_copy_static);
  // gulp.watch(GLOBS.less_files, ["less"]);   
});

gulp.task('copy',function () {
	return gulp.src(GLOBS.copy_file)
	.pipe(gulp.dest(DIST));
});

gulp.task("build",["jade","copy"]);

