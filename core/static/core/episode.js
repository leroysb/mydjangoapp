document.addEventListener ('DOMContentLoaded', function(){

    /* PODCAST PLAYER*/

    const audio = document.querySelector('#episodeaudio');
    // const duration = audio.duration; // Duration of audio clip, calculated here for embedding purposes
    const timer = document.querySelector('.timer');
    const pButton = document.querySelector('#pButton');
    const pause = document.querySelector('#pause');
    const play = document.querySelector('#play');
    const rev = document.querySelector('#rev');
    const fwd = document.querySelector('#fwd');

    pButton.addEventListener("click", PausePlayEpisode);
    rev.addEventListener("click", mediaBackward);
    fwd.addEventListener("click", mediaForward);

    // Timer

    function secondsToHms(d) {
        d = Number(d);
        var h = Math.floor(d / 3600);
        var m = Math.floor(d % 3600 / 60);
        var s = Math.floor(d % 3600 % 60);

        // var hDisplay = h > 0 ? h + (h == 1 ? ":" : ":") : "00:";
        // var mDisplay = m > 0 ? m + (m == 1 ? ":" : ":") : "00:";
        // var sDisplay = s > 0 ? s + (s == 1 ? "0" : "") : "00";
        // return hDisplay + mDisplay + sDisplay;

        if (h   < 10) {h   = "0"+h;}
        if (m < 10) {m = "0"+m;}
        if (s < 10) {s = "0"+s;}
        return h+':'+m+':'+s;
    }

    timer.innerHTML = secondsToHms(audio.currentTime);

    audio.ontimeupdate = ()=> {
        timer.innerHTML = secondsToHms(audio.currentTime);
    };

    //Player Controls

    function PausePlayEpisode() {
        // start podcast
        if (audio.paused) {
            audio.play();
            pButton.src="{% static 'core/icons/pause.png' %}";
        } else {
            audio.pause();
            pButton.src="{% static 'core/icons/play.png' %}";
        }
    };

    function mediaBackward() {
        if(audio.currentTime <= 10) {
            stopMedia();
        } else {
            audio.currentTime -= 10;
        }
    };

    function mediaForward() {
        if(audio.currentTime >= audio.duration - 30) {
            stopMedia();
        } else {
            audio.currentTime += 30;
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