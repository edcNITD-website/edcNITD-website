// const handler = () => {
    
// };

// // Listen for `DOMContentLoaded` event
// document.addEventListener('DOMContentLoaded', handler);
var x = setInterval(function () {
    if (document.getElementById('secs-left') == null) {
        clearInterval(x);
        return 0;
    }
    var totalseconds = document.getElementById('secs-left').innerHTML;

    if (totalseconds > 0) {
        var day = 86400;
        var hour = 3600;
        var minute = 60;
        var daysout = Math.floor(totalseconds / day);
        var hoursout = Math.floor((totalseconds - daysout * day)/hour);
        var minutesout = Math.floor((totalseconds - daysout * day - hoursout * hour)/minute);
        var secondsout = Math.floor(totalseconds - daysout * day - hoursout * hour - minutesout * minute);
        var hours_out = document.getElementById('out_hrs');
        var mins_out = document.getElementById('out_mins');
        var secs_out = document.getElementById('out_secs');
        var days_out = document.getElementById('out_days');
        hours_out.innerHTML = hoursout;
        mins_out.innerHTML = minutesout;
        secs_out.innerHTML = secondsout;
        days_out.innerHTML = daysout;
        document.getElementById('secs-left').innerHTML = totalseconds - 1;
    }
    else {
        subtask_links = document.getElementsByClassName('subtask-submit-link');
        for (const key in subtask_links) {
            const link = subtask_links[key];
            link.classList.add('hidden');
            clearInterval(x);
        }
    }
},1000);