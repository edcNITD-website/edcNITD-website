theme_changer();
function theme_changer(){
    var colorCodes = ['f38b36', '44aaff','06d6a0','A682FF','EF5B5B'];
    var randomColor = colorCodes[Math.floor(Math.random() * colorCodes.length)];
    randomColor = '#' + randomColor;
    // console.log(randomColor);
    var root = document.querySelector(':root');
    root.style.setProperty('--theme-color', randomColor);
    // console.log(getComputedStyle(root).getPropertyValue('--theme-color'));
}