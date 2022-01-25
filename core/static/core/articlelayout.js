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
        }
    })

    $(document).ready(function(){
        // Check Radio-box
        $(".rating input:radio").attr("checked", false);
    
        $('.rating input').click(function () {
            $(".rating span").removeClass('checked');
            $(this).parent().addClass('checked');
        });
    
        // $('input:radio').change(
        //   function(){
        //     var userRating = this.value;
        //     alert(userRating);
        // }); 
    });

    const shareBtn = document.querySelector('#sharebtn');
    const shareOptions = document.querySelector('.share-options');

    shareBtn.addEventListener('click', () => {
        shareOptions.classList.toggle('active');
    })
})