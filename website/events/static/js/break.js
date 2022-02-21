setInterval(widthChecker, 200);
setInterval(backButton, 200);
setInterval(header, 200);

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

function backButton() {
    let container = document.getElementById("upper-head");
    let screenWidth = screen.width;
    if (screenWidth < 1150){
        container.style.marginTop = "6rem";
    } else {
        container.style.marginTop = "5rem";
    }
}

function header(){
    let head = document.getElementById("team-header-text");
    let screenWidth = screen.width;
    if (screenWidth <= 500){
        head.style.marginRight = "2px";
    } else {
        head.style.marginRight = "0";
    }
}

