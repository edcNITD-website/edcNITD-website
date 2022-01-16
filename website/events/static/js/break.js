setInterval(widthChecker, 200);

function widthChecker() {
    let width = screen.width;
    
    if(width <= 585){
        document.getElementById("break1").innerHTML = '<br>';
        document.getElementById("break2").innerHTML = '<br>';
    } else {
        document.getElementById("break1").innerHTML = '';
        document.getElementById("break2").innerHTML = '';
    }
}


