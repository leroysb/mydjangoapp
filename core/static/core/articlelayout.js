document.addEventListener('DOMContentLoaded', function(){
    const background = document.querySelector('.meta');

    document.body.querySelector('.meta').addEventListener('load', getBGcolor());

    function getBGcolor() {
        const choices = ['#86baaf', '#ffca52']
        const randomNumber = Math.floor(Math.random()*2);
        const selection = choices[randomNumber];
        background.style.backgroundColor = selection;
    };

    document.addEventListener('click', (event)=> {
        if(event.target.id=="id01"){
            document.querySelector('#id01').style.display='none';
        };
        if(event.target.id=="sharebtn"){
            document.querySelector('.share-options').classList.toggle('active');
        };
    })
   
    $(document).ready(function(){
        // Check Radio-box
        $(".rating input:radio").attr("checked", false);
    
        $('.rating input').click(function () {
            $(".rating span").removeClass('checked');
            $(this).parent().addClass('checked');
        });
    });
})