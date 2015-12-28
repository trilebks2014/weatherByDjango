var YQL = require('yql');
int result
function takeJson(city){
	yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"";
	yql_query += city +",il\") ";
	return yql_query;
}
var query = new YQL(takeJson(city));

query.exec(function(err, data) {
  var location = data.query.results.channel.location;
  var condition = data.query.results.channel.item.condition;
  // console.log('The current weather in ' + location.city + ', ' + location.region + ' is ' + condition.temp + ' degrees.');
  result='The current weather in ' + location.city + ', ' + location.region + ' is ' + condition.temp + ' degrees.'
});