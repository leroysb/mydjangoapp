document.addEventListener ('DOMContentLoaded', function(){

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
    
    /* PODCAST PAGE*/
    
    const pButton3 = document.querySelector('#pButton3');
    const audio = document.querySelectorAll('.episodeaudio');
    // const audiostatus = '';
    
    document.querySelector('.podpage').addEventListener('load', ()=> 
        document.querySelectorAll('#pButton1').forEach((pButton1) => {
            pButton1.alt="play episode";
            pButton1.src="/static/core/media/playnow.png";
            pButton1.addEventListener('click', PlayPodcast());
            pButton3.alt="play episode";
            pButton3.src = "/static/core/media/play.png";
            pButton3.addEventListener('click', PlayPauseEpisode());
            // audiostatus = 'stop';
        })
    );
    // function setLoad() {
    //     document.querySelectorAll('#pButton1').forEach((pButton1) => {
    //         pButton1.alt="play episode";
    //         pButton1.src="/static/core/media/playnow.png";
    //         pButton1.addEventListener('click', PlayPodcast());
    //         pButton3.alt="play episode";
    //         pButton3.src = "/static/core/media/play.png";
    //         pButton3.addEventListener('click', PlayPauseEpisode());
    //         // audiostatus = 'stop';
    //     })
    // };

    //Player Controls

    function PlayPauseEpisode() {
        document.querySelectorAll('#pButton1').forEach((pButton1,i) => {
            audio[i].play();
            pButton1[i].alt="pause episode";
            pButton1[i].src="/static/core/media/pausenow.png";
            pButton1[i].addEventListener('click', PausePodcast());
            pButton3.alt="pause episode";
            pButton3.src = "/static/core/media/pause.png";
        })

        // if (audiostatus == stop) {
        //     document.querySelectorAll('#pButton1').forEach((pButton1,i) => {
        //         document.querySelectorAll('.episodeaudio').forEach((audio));
        //         audio[i].play();
        //         pButton1[i].alt="pause episode";
        //         pButton1[i].src="/static/core/media/pausenow.png";
        //         pButton1[i].addEventListener('click', PausePodcast());
        //     })
    
        //     const pButton3 = document.querySelector('#pButton3');
        //     pButton3.alt="pause episode";
        //     pButton3.src = "/static/core/media/pause.png";
        //     audiostatus = 'playing';
        // }

        // if (audiostatus=='playing') {
            
        //     document.querySelectorAll('.episodeaudio').forEach((audio)=>{
        //         audio.pause();
        //     });

        //     document.querySelectorAll('#pButton1').forEach((pButton1) => {
        //         pButton1.alt="play episode";
        //         pButton1.src="/static/core/media/playnow.png";
        //     })

        //     document.querySelectorAll('#pButton1').forEach((pButton1,i) => {
        //         document.querySelectorAll('.episodeaudio').forEach((audio));
        //         audio[i].play();
        //         pButton1[i].alt="pause episode";
        //         pButton1[i].src="/static/core/media/pausenow.png";
        //         pButton1[i].addEventListener('click', PausePodcast());
        //     })

        //     const pButton3 = document.querySelector('#pButton3');
        //     pButton3.alt="pause episode";
        //     pButton3.src = "/static/core/media/pause.png";
        //     audiostatus = 'playing';
        // }

    };
    
    // function PausePodcast() {

    //     document.querySelectorAll('#pButton1').forEach((pButton1,i) => {
    //         document.querySelectorAll('.episodeaudio').forEach((audio));
    //         audio[i].pause()
    //         pButton1[i].alt="lay episode";
    //         pButton1[i].src="/static/core/media/playnow.png";
    //         pButton1[i].addEventListener('click', PlayPodcast());
    //     })

    //     const pButton3 = document.querySelector('#pButton3');
    //     pButton3.alt="play episode";
    //     pButton3.src = "/static/core/media/play.png";
    // };

    
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