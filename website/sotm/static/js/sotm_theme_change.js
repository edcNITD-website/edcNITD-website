theme_changer();
function theme_changer(){
    var colorCodes = ['f38b36', '4af', '06d6a0', 'A682FF', 'EF5B5B'];
    var lastRandomColor = sessionStorage.getItem('lastRandomColor');
    var randomColor = colorCodes[Math.floor(Math.random() * colorCodes.length)];
    randomColor = '#' + randomColor;
    if (lastRandomColor != null) {
        while (lastRandomColor == randomColor) {
            randomColor = colorCodes[Math.floor(Math.random() * colorCodes.length)];
            randomColor = '#' + randomColor;
        }
    }
    var root = document.querySelector(':root');
    root.style.setProperty('--theme-color', randomColor);
    // console.log(randomColor);
    sessionStorage.setItem('lastRandomColor', randomColor);
    // console.log(getComputedStyle(root).getPropertyValue('--theme-color'));
}