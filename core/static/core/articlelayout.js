document.addEventListener('DOMContentLoaded', function(){
    const background = document.querySelector('.meta');

    document.body.querySelector('.meta').addEventListener('load', getBGcolor());

    function getBGcolor() {
        const choices = ['#86baaf', '#ffca52']
        const randomNumber = Math.floor(Math.random()*2);
        const selection = choices[randomNumber];
        background.style.backgroundColor = selection;
    }
})