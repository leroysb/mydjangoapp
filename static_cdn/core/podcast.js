document.addEventListener ('DOMContentLoaded', function(){
    
    const pButton3 = document.querySelector('#pButton3');
    const audio = document.querySelectorAll('.episodeaudio');
    var audioplaying = False;
    
    document.addEventListener('load', ()=> {
        document.querySelectorAll('#pButton1').forEach((pButton1) => {
            pButton1.alt="play episode";
            pButton1.src="/static/core/media/playnow.png";
            pButton1.addEventListener('click', PlayPauseEpisode());
        });
        
        pButton3.alt="play episode";
        pButton3.src = "/static/core/media/play.png";
        // pButton3.addEventListener('click', PlayPauseEpisode());
    });

    //Player Controls

    function PlayPauseEpisode() {
        document.querySelectorAll('#pButton1').forEach((pButton1,i) => {

            // If audio already playing (playing=true)
            if(audioplaying == True) {

                // Stop all audio
                document.querySelectorAll('.episodeaudio').forEach((audio) => {
                    audio.stop();
                });

                // Reset all images to play icon
                pButton1.alt="play episode";
                pButton1.src="/static/core/media/playnow.png";
                pButton3.alt="play episode";
                pButton3.src = "/static/core/media/play.png";

                // Change selected episode icon to pause + main footer icon
                pButton1[i].alt="pause episode";
                pButton1[i].src="/static/core/media/pausenow.png";
                pButton3.alt="pausey episode";
                pButton3.src = "/static/core/media/pause.png";

                // Start audio for selected episode
                audio[i].play();

                // set (playing=true)
                audioplaying = True;
            };

            // else, if (playing=false)
            if(audioplaying == False) {
                // Change selected episode icon to pause + main footer icon
                pButton1[i].alt="pause episode";
                pButton1[i].src="/static/core/media/pausenow.png";
                pButton3.alt="pausey episode";
                pButton3.src = "/static/core/media/pause.png";

                // Start audio for selected episode
                audio[i].play();

                // set (playing=true)
                audioplaying = True;
            };
        });
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