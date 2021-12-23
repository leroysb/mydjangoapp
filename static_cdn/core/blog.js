document.addEventListener('DOMContentLoaded', ()=> {

    document.querySelector('.blogpage').addEventListener('load', DivControl());

    function DivControl() {

        document.querySelectorAll('.articlediv').forEach((articlediv)=>
            articlediv.style.display = 'none'
        );

        const articlediv = document.querySelectorAll('.articlediv');
        const firstload = 8

        for( let i = 0; i < firstload; i++){
            articlediv[i].style.display = 'block'
        };

        if(articlediv.length >= firstload ) {
            document.querySelector('#loadnext').style.display='block';
        };
    };

    const articlediv = document.querySelectorAll('.articlediv');
    var currentindex = 8
    
    document.querySelector('#loadnext').onclick = ()=> {
        
        var next = 8;

        for(var i = 0 ; i < next; i++){
            if(currentindex >= articlediv.length) {
                document.querySelector('#loadnext').style.display='none';
                return
            } else {
                articlediv[i+currentindex].style.display = 'block';
            }
        }

        currentindex += next
    };


});