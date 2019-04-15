function getTimeRemaining() {
  deadlineTKP = deadlineTKP-1000;
  deadlineBL = deadlineBL - 1000;
  var tTKP = deadlineTKP;
  var secondsTKP = Math.floor((tTKP / 1000) % 60);
  var minutesTKP = Math.floor((tTKP / (1000 * 60)) % 60);
  var hoursTKP = Math.floor((tTKP / (1000 * 3600)) % 24);

  var tBL = deadlineBL;
  var secondsBL = Math.floor((tBL / 1000) % 60);
  var minutesBL = Math.floor((tBL / (1000 * 60)) % 60);
  var hoursBL = Math.floor((tBL / (1000 * 3600)) % 24);

  //var days = Math.floor(t / (1000 * 60 * 60 * 24));
  return {
    'total': [tTKP, tBL],
    //'days': days,
    'hours': [hoursTKP, hoursBL],
    'minutes': [minutesTKP, minutesBL],
    'seconds': [secondsTKP, secondsBL]
  };
}

function initializeClock(cls) {
  var clock = document.getElementsByClassName(cls);
  console.log(clock)
 
  var hoursSpanTKP = clock[0].querySelector('#hoursTokped');
  var minutesSpanTKP = clock[0].querySelector('#minutesTokped');
  var secondsSpanTKP = clock[0].querySelector('#secondsTokped');

  var hoursSpanBL = clock[1].querySelector('#hoursBL');
  var minutesSpanBL = clock[1].querySelector('#minutesBL');
  var secondsSpanBL = clock[1].querySelector('#secondsBL');

  function updateClock() {
    var t = getTimeRemaining();
    //daysSpan.innerHTML = t.days;
    // console.log(t.hours)
    // console.log(t.minutes)
    // console.log(t.seconds)
    hoursSpanTKP.innerHTML = ('0' + t.hours[0]).slice(-2);
    minutesSpanTKP.innerHTML = ('0' + t.minutes[0]).slice(-2);
    secondsSpanTKP.innerHTML = ('0' + t.seconds[0]).slice(-2);

    hoursSpanBL.innerHTML = ('0' + t.hours[1]).slice(-2);
    minutesSpanBL.innerHTML = ('0' + t.minutes[1]).slice(-2);
    secondsSpanBL.innerHTML = ('0' + t.seconds[1]).slice(-2);

    if (t.total <= 0) {
      clearInterval(timeinterval);
    }
  }

  updateClock();
  var timeinterval = setInterval(updateClock, 1000);
}
var secHTMLTKP = document.getElementById('secondsTokped');
var secTKP = parseInt(secHTMLTKP.textContent);

var minHTMLTKP = document.getElementById('minutesTokped');
var minTKP = parseInt(minHTMLTKP.textContent)*60;

var hourHTMLTKP = document.getElementById('hoursTokped');
var hourTKP = parseInt(hourHTMLTKP.textContent)*3600;

var deadlineTKP = (hourTKP+minTKP+secTKP)*1000;

var secHTMLBL = document.getElementById('secondsBL');
var secBL = parseInt(secHTMLBL.textContent);

var minHTMLBL = document.getElementById('minutesBL');
var minBL = parseInt(minHTMLBL.textContent)*60;

var hourHTMLBL = document.getElementById('hoursBL');
var hourBL = parseInt(hourHTMLBL.textContent)*3600;

var deadlineBL = (hourBL+minBL+secBL)*1000;


initializeClock('clockdiv');