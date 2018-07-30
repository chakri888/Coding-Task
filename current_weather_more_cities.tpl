<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <center><h1><strong>More than one location was found</strong></h1></center>
    <center><h2><strong>Please select one from the list below</strong></h2></center>
    <br/>
    %for city in many_cities:
        <center><p style="font-size:20px">{{city[2]}}, {{city[-1]}}</p></center>
        <center>
    <iframe
  		width="600"
  		height="450"
  		frameborder="0" style="border:0"
  		src="https://www.google.com/maps/embed/v1/place?key={{city[1]}}
    		&q={{city[3]}}, {{city[4]}}" allowfullscreen>
	</iframe>
	</center>
	<center>
	<form action="/selected">
	    <button style="height:40px; width:150px"; type="submit"; name="id"; value="{{(city[0], city[2])}}">Select THIS Location</button>
	</form>
    </center>
    %end
</body>
</html>
