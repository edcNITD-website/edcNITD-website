function closeMsg(element) {
    element.parentElement.parentElement.style.display = 'none';
}

function closeAll() {
    let msgElement = document.getElementById('msg-element');
    if (msgElement) {
        msgElement.style.display = "none";
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const myTimeout = setTimeout(closeAll, 4500);
});
//     // console.log('Set all messages to closed');
//     const faviconTag = document.getElementById("faviconTag");

//     const changeFavicon = () => {
//         const isDark = window.matchMedia("(prefers-color-scheme: dark)");
//         // console.log(isDark);
//         if(isDark.matches){
//             faviconTag.href = "/static/base/images/favicon_dark.ico";
//         }
//         else {

//             faviconTag.href = "/static/base/images/favicon.ico";
//         }
//     };
//     changeFavicon();
//     setInterval(changeFavicon,1000)
// });
