function handleCoords(){
    window.location.href = "/coords";
}

function handleCity(){
    window.location.href = '/city';
}

function handlecty(){
    let city = document.getElementById("cty").value;
    let url = '/city?cty=';
    let builtURL = (url + encodeURIComponent(city));
    window.location.href = builtURL;
}

function handlecoords(){
    let lat = document.getElementById("latitude").value;
    let lon = document.getElementById("longitude").value;
    if (!lat || !lon) {
        alert("Both lat & lon are required.");
        return;
    }
    let url = '/coords?lat=' + encodeURIComponent(lat) + '&lon=' + encodeURIComponent(lon);
    window.location.href = url;
}