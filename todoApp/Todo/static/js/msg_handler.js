
var messages = document.getElementsByClassName('messages');
        setTimeout(function(){
            for(var i=0; i<messages.length; i++){
                messages[i].style.display = 'none';
            }
        }, 3000);