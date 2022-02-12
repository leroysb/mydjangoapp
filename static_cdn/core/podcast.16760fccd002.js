document.addEventListener ('DOMContentLoaded', function(){

    // var element = document.createElement('div');
    // element.classList.add('epi-play');
    // document.querySelector('.podcast-epi').appendChild(element);

    const pgSetup = (function() {
        var pButton = new Image();
        pButton.src = "/static/core/media/playnow.png";
        pButton.height = "100%";
        pButton.width = "100%";
        document.querySelector('.epi-play').appendChild(pButton);
        pButton.addEventListener('click', PlayPause());
    
        // var pButtonFT = new Image();
        // pButtonFT.src = "/static/core/media/play.png";
        // pButtonFT.height = "100%";
        // pButtonFT.width = "100%";
        // document.querySelector('.footerimage').appendChild(pButtonFT);
        // pButtonFT.addEventListener('click', PlayPause());
    }());

    pgSetup()

    const audio = document.querySelectorAll('#audio');
    let audioplaying = false;

    //Player Controls

    function PlayPause() {
        pButton.forEach((pButton,i) => {

            // If audio already playing (playing=true)
            if(audioplaying !== true) {

                // Stop all audio
                audio.stop()

                // Reset all images to play icon
                pButton.src="/static/core/media/playnow.png"
                pButtonFT.src = "/static/core/media/play.png"

                // Change selected episode icon to pause + main footer icon
                pButton[i].src="/static/core/media/pausenow.png"
                pButtonFT.src = "/static/core/media/pause.png"

                // Start audio for selected episode
                audio[i].play()

                // set (playing=true)
                audioplaying = true
            }

            // else, if (playing=false)
            if(audioplaying == false) {
                // Change selected episode icon to pause + main footer icon
                pButton[i].src="/static/core/media/pausenow.png"
                pButtonFT.src = "/static/core/media/pause.png"

                // Start audio for selected episode
                audio[i].play()

                // set (playing=true)
                audioplaying = true
            }
        })
    }

    
    // const podcast = document.querySelector('#podcast') // id for audio element
    // const player = document.getElementsByClassName('player')

    // const playhead = document.getElementById('playhead') // playhead
    // const timeline = document.getElementById('timeline') // timeline
    // const timerWrapper = document.querySelector('.timer')
    // const timer = document.querySelector('.timer span')
    // const timerBar = document.querySelector('.timer div')

    // // timeline width adjusted for playhead
    // const timelineWidth = timeline.offsetWidth - playhead.offsetWidth
    
})