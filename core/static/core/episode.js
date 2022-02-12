document.addEventListener ('DOMContentLoaded', function(){

    /* PODCAST PLAYER*/

    const audio = document.querySelector('#episodeaudio');
    var duration = document.querySelector('.duration');
    var timer = document.querySelector('.timer');
    var pButtonFT = document.querySelector('#pButtonFT');

    pButtonFT.addEventListener("click", PausePlay);

    // Timer

    function secondsToHms(d) {
        d = Number(d);
        var h = Math.floor(d / 3600);
        var m = Math.floor(d % 3600 / 60);
        var s = Math.floor(d % 3600 % 60);

        if (h   < 10) {h   = "0"+h;}
        if (m < 10) {m = "0"+m;}
        if (s < 10) {s = "0"+s;}
        return h+':'+m+':'+s;
    }

    duration.innerHTML = secondsToHms(audio.duration);
    timer.innerHTML = secondsToHms(audio.currentTime);

    audio.ontimeupdate = ()=> {
        timer.innerHTML = secondsToHms(audio.currentTime);
    };

    //Player Controls

    function PausePlay() {
        // start podcast
        if (audio.paused) {
            audio.play();
            pButtonFT.src="/static/core/media/pause.png";
        } else {
            audio.pause();
            pButtonFT.src="/static/core/media/play.png";
        }
    };


    // const podcast = document.querySelector('#podcast'); // id for audio element
    // const player = document.getElementsByClassName('player');

    // const playhead = document.getElementById('playhead'); // playhead
    // const timeline = document.getElementById('timeline'); // timeline
    // const timerWrapper = document.querySelector('.timer');
    // const timer = document.querySelector('.timer span');
    // const timerBar = document.querySelector('.timer div');

    // // timeline width adjusted for playhead
    // const timelineWidth = timeline.offsetWidth - playhead.offsetWidth;

});