document.addEventListener ('DOMContentLoaded', function(){
    
    const pButton = document.querySelectorAll('#pButton');
    const pButtonPT = document.querySelector('#pButtonPT');
    const audio = document.querySelectorAll('#episodeaudio');
    var audioplaying = False;
    
    document.addEventListener('load', ()=> {
        document.querySelectorAll('#pButton').forEach((pButton,i) => {
            pButton.alt="play episode";
            pButton.src="/static/core/media/playnow.png";
            pButton.addEventListener('click', PlayPauseEpisode());
        });
        
        pButtonPT.alt="play episode";
        pButtonPT.src = "/static/core/media/play.png";
        pButtonPT.addEventListener('click', PlayPauseEpisode());
    });

    //Player Controls

    function PlayPauseEpisode() {
        // document.querySelectorAll('#pButton').forEach((pButton,i) => {

            // If audio already playing (playing=true)
            if(audioplaying == True) {

                // Stop all audio
                audio.stop();

                // Reset all images to play icon
                pButton.alt="play episode";
                pButton.src="/static/core/media/playnow.png";
                pButtonFT.alt="play episode";
                pButtonFT.src = "/static/core/media/play.png";

                // Change selected episode icon to pause + main footer icon
                pButton[i].alt="pause episode";
                pButton[i].src="/static/core/media/pausenow.png";
                pButtonPT.alt="pause episode";
                pButtonPT.src = "/static/core/media/pause.png";

                // Start audio for selected episode
                audio[i].play();

                // set (playing=true)
                audioplaying = True;
            };

            // else, if (playing=false)
            if(audioplaying == False) {
                // Change selected episode icon to pause + main footer icon
                pButton[i].alt="pause episode";
                pButton[i].src="/static/core/media/pausenow.png";
                pButtonPT.alt="pausey episode";
                pButtonPT.src = "/static/core/media/pause.png";

                // Start audio for selected episode
                audio[i].play();

                // set (playing=true)
                audioplaying = True;
            };
        // });
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

    /* menu */
    
    const menuBtn = document.querySelector('.menu-btn');
    let menuOpen = false;
    
    menuBtn.addEventListener('click', () => {
        const mobMenu = document.querySelector('.mobile-menu');
        
        if(!menuOpen){
            menuBtn.classList.add('open');
            mobMenu.classList.add('show');
            menuOpen= true;
        } else {
            menuBtn.classList.remove('open');
            mobMenu.classList.remove('show');
            menuOpen = false;
        }
    });

    /* Dropdown */

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
    
});