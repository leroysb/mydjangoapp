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

    // FEEDBACK MODAL
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

    // BLOG PAGE
    document.querySelector('.blogpage').addEventListener('load', ()=> {
    
        const articles = document.querySelectorAll('.articlediv');
        const firstload = 8

        document.querySelectorAll('.articlediv').forEach((article)=>
            article.style.display = 'none'
        );
    
        if(articles.length >= firstload ) {
            document.querySelector('#showbtn').style.display='flex';
        } else {
            document.querySelector('#showbtn').style.display='none';
        };
    
        for(let i = 0; i < firstload; i++){
            articles[i].style.display = 'block';
        };
    });


    const articlediv = document.querySelectorAll('.articlediv');
    var currentindex = 8
    
    document.querySelector('#loadnext').onclick = ()=> {
        
        var next = 8;

        for(var i = 0 ; i < next; i++){
            if(currentindex >= articlediv.length) {
                document.querySelector('#showbtn').style.display='none';
            } else {
                articlediv[i+currentindex].style.display = 'block';
            }
        }

        currentindex += next;
    };

    // ARTICLE PAGE
    const background = document.querySelector('.meta');

    // document.body.addEventListener('load', ()=> {
    //     const choices = ['#86baaf', '#ffca52'];
    //     const randomNumber = Math.floor(Math.random()*2);
    //     const selection = choices[randomNumber];
    //     background.style.backgroundColor = selection;
    // });

    $('.meta').ready(function(){
        const background = document.querySelector('.meta');
        const choices = ['#86baaf', '#ffca52'];
        const randomNumber = Math.floor(Math.random()*2);
        const selection = choices[randomNumber];
        background.style.backgroundColor = selection;
    })
});