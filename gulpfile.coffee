gulp  = require('gulp')
gultil = require('gulp-util')
jade = require('gulp-jade')
coffee = require('gulp-coffee')

DIST = "./build/"
GROBS = {
	jade:[
		"src/weather/weather/**/*.jade"
	]
}

OPTIONS = {
	coffee:{
		bare: true,
		bokens: true
	},
	jade:{
		pretty: true,
		self: false
	}
}
display = (error) ->
	gultil.log(gultil.color.red(error));
	@emit 'end';
	return
gulp.task 'jade', (done) ->
  gulp.src(GROBS.jade).pipe(jade(OPTIONS.jade)).on('error', display).pipe(gulp.dest(DIST)).on 'end', done
  return

gulp.task 'build', [ 'jade' ]