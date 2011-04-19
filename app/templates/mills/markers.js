
var markers=[]

{% for mill in mills %}


m=new google.maps.Marker({
        position: new google.maps.LatLng({{ mill.location.lat }},{{ mill.location.lon }}), 
        title:"{{mill.name|e}}",
        permalink:"{{ url_for('mills/single', mill_no=mill.key().name(), slug=mill.slug)}}"
    });

 markers.push(m);
 {% endfor %}