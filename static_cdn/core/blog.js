document.addEventListener('DOMContentLoaded', ()=> {

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