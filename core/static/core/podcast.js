document.addEventListener ('DOMContentLoaded', function(){
    
    const pButton = document.querySelectorAll('#pModule')
    const pButtonFT = document.querySelector('#pButtonFT')
    const audio = document.querySelectorAll('#audio')
    
    window.onload = ()=> {
        pButton.alt="play episode"
        pButton.src="/static/core/media/playnow.png"
        pButton.addEventListener('click', PlayPause)
        pButtonFT.alt="play episode"
        pButtonFT.src = "/static/core/media/play.png"
        pButtonFT.addEventListener('click', PlayPause)
        let audioplaying = False
        console.log("done")
    }

    //Player Controls

    function PlayPause() {
        pButton.forEach((pButton,i) => {

            // If audio already playing (playing=true)
            if(audioplaying ==! True) {

                // Stop all audio
                audio.stop()

                // Reset all images to play icon
                pButton.alt="play episode"
                pButton.src="/static/core/media/playnow.png"
                pButtonFT.alt="play episode"
                pButtonFT.src = "/static/core/media/play.png"

                // Change selected episode icon to pause + main footer icon
                pButton[i].alt="pause episode"
                pButton[i].src="/static/core/media/pausenow.png"
                pButtonFT.alt="pause episode"
                pButtonFT.src = "/static/core/media/pause.png"

                // Start audio for selected episode
                audio[i].play()

                // set (playing=true)
                audioplaying = True
            }

            // else, if (playing=false)
            if(audioplaying === False) {
                // Change selected episode icon to pause + main footer icon
                pButton[i].alt="pause episode"
                pButton[i].src="/static/core/media/pausenow.png"
                pButtonFT.alt="pausey episode"
                pButtonFT.src = "/static/core/media/pause.png"

                // Start audio for selected episode
                audio[i].play()

                // set (playing=true)
                audioplaying = True
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

    /* menu */
    const menuBtn = document.querySelector('.menuBtn')
    let menuOpen = false
    
    menuBtn.addEventListener('click', () => {
        const mobMenu = document.querySelector('.mobile-menu')
        
        if(!menuOpen){
            menuBtn.classList.add('open')
            mobMenu.classList.add('show')
            menuOpen= true
        } else {
            menuBtn.classList.remove('open')
            mobMenu.classList.remove('show')
            menuOpen = false
        }
    })

    /* Dropdown */

    document.querySelector('.dropbtn').onclick = ()=> {
        document.querySelector('#myDropdown').classList.toggle('show')
    }

    // Close the dropdown if the user clicks outside of the Dropdown button

    window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
            var dropdowns = document.getElementsByClassName("dropdown-content")
            var i
            for (i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i]
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show')
                }
            }
        }
    }
    
})