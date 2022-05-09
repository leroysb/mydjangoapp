document.addEventListener('DOMContentLoaded', function(){

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

});