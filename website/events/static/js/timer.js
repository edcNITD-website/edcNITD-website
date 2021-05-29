(function () {
  const second = 1000,
    minute = second * 60,
    hour = minute * 60,
    day = hour * 24;

  let eventday1 = "july 17, 2021 00:05:30",
    eventday2 = "sept 7, 2021 00:00:00",
    countDown1 = new Date(eventday1).getTime(),
    countDown2 = new Date(eventday2).getTime(),
    x = setInterval(function () {
      let now = new Date().getTime(),
        distance1 = countDown1 - now;
      distance2 = countDown2 - now;

      (document.getElementById("uedays").innerText = Math.floor(
        distance1 / day
      )),
        (document.getElementById("uehours").innerText = Math.floor(
          (distance1 % day) / hour
        )),
        (document.getElementById("ueminutes").innerText = Math.floor(
          (distance1 % hour) / minute
        )),
        (document.getElementById("ueseconds").innerText = Math.floor(
          (distance1 % minute) / second
        ));

      (document.getElementById("oedays").innerText = Math.floor(
        distance2 / day
      )),
        (document.getElementById("oehours").innerText = Math.floor(
          (distance2 % day) / hour
        )),
        (document.getElementById("oeminutes").innerText = Math.floor(
          (distance2 % hour) / minute
        )),
        (document.getElementById("oeseconds").innerText = Math.floor(
          (distance2 % minute) / second
        ));

      function setCounter(id, value, max) {
        var elem = document.getElementById(id);
        var radius = elem.r.baseVal.value;
        var circumference = radius * 2 * Math.PI;
        var barLength = Math.floor((value * circumference) / max);

        elem.setAttribute("stroke-dasharray", barLength + " " + circumference);
      }

      setCounter("uesecondss", Math.floor((distance1 % minute) / second), 60);
      setCounter("ueminutess", Math.floor((distance1 % hour) / minute), 60);
      setCounter("uehourss", Math.floor((distance1 % day) / hour), 24);
      setCounter("uedayss", Math.floor(distance1 / day), 365);

      setCounter("oesecondss", Math.floor((distance2 % minute) / second), 60);
      setCounter("oeminutess", Math.floor((distance2 % hour) / minute), 60);
      setCounter("oehourss", Math.floor((distance2 % day) / hour), 24);
      setCounter("oedayss", Math.floor(distance2 / day), 365);
    }, 0);
})();
