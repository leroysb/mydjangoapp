document.addEventListener('DOMContentLoaded', function(){
    // MENU
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

    // MODAL
    document.addEventListener('click', (event)=> {
        if(event.target.id=="id01"){
            document.querySelector('#id01').style.display='none';
        };
        // if(event.target.id=="id02"){
        //     document.querySelector('#id02').style.display='none';
        // };
        // if(event.target.id=="sharebtn"){
        //     document.querySelector('.share-options').classList.toggle('active');
        // };
    })
   
    $(document).ready(function(){
        // Check Radio-box
        $(".rating input:radio").attr("checked", false);
    
        $('.rating input').click(function () {
            $(".rating span").removeClass('checked');
            $(this).parent().addClass('checked');
        });
    });
});