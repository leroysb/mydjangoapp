document.addEventListener ('DOMContentLoaded', function(){

    /* HOME PAGE*/

    document.querySelector('.dropbtn').onclick = ()=> {
        document.querySelector('#myDropdown').classList.toggle('show')
    };

    // Close the dropdown if the user clicks outside of the Dropdown button

    window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            var i;
            for (i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    };

    /* PODCAST PAGE*/

    const audio = document.querySelector('#episodeaudio');
    const pButton = document.querySelector('.pButton');
    const pause = document.querySelector('.pause');
    const play = document.querySelector('.play');
    const duration = audio.duration; // Duration of audio clip, calculated here for embedding purposes
    const rev = document.querySelector('#rev');
    const fwd = document.querySelector('#fwd');

    pButton.addEventListener("click", PausePlayEpisode);
    pause.addEventListener("click", PauseEpisode);
    play.addEventListener("click", PlayEpisode);
    rev.addEventListener("click", mediaBackward);
    fwd.addEventListener("click", mediaForward);

    // audio.addEventListener('load', (event) => {
    //     pButton.src="{% static 'blogapp/icons/pause.png' %}";
    //     pButton.src="pause episode";
    //     pButton.addEventListener('click', PlayPausePodcast);
    // });

    //Player Controls

    function PausePlayEpisode() {
        // start podcast
        if (audio.paused) {
            audio.play();
            pButton.src="{% static 'blogapp/icons/pause.png' %}";
        } else {
            audio.pause();
            pButton.src="{% static 'blogapp/icons/play.png' %}";
        }
    }

    function PauseEpisode() {
        audio.pause();
        pButton.src="{% static 'blogapp/icons/play.png' %}";
    }

    function PlayEpisode() {
        audio.play();
        pButton.src="{% static 'blogapp/icons/pause.png' %}";
    }

    function mediaBackward() {
        if(audio.currentTime <= 10) {
            stopMedia();
        } else {
            audio.currentTime -= 10;
        }
    }

    function mediaForward() {
        if(audio.currentTime >= audio.duration - 30) {
            stopMedia();
        } else {
            audio.currentTime += 30;
        }
    }

    
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