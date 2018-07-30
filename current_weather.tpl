<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast for {{city_name}}</title>
</head>
<body>
    <center><h1><strong>Current Weather Forecast</strong></h1></center>
    <center><h2><strong>{{city_name}}, {{country_iso_code}}</strong></h2></center>
    <div style="font-size:20px">
        <center><p>Max temp: {{weather_max_temp}}&degC</p></center>
        <center><p>Min temp: {{weather_min_temp}}&degC</p></center>
        <center><p>Wind: {{weather_wind}} km/h</p></center>
        <center><p>Humidity: {{humidity}}%</p></center>
    </div>
    <br/>
    <center>
    <iframe
  		width="600"
  		height="450"
  		frameborder="0" style="border:0"
  		src="https://www.google.com/maps/embed/v1/place?key={{google_map_api_key}}
    		&q={{latitude}}, {{longitude}}" allowfullscreen>
	</iframe>
	</center>
	<br/>
	<center>
	<form form action="/" method="GET">
	    <button style="height:40px; width:150px"; type="submit">Search Another Location</button>
	</form>
	</center>
</body>
</html>
