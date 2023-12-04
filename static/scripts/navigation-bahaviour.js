
document.getElementById("close-navigation").onclick = function(){
    let extend = 0;
    let non_extend = -20;
    let close = true;

    
    const nav = document.getElementsByClassName("navigation");
    
    if (nav[0].style.right == String(extend)+"%"){
        close = false;
        
    }
    if (nav[0].style.right == String(non_extend)+"%"){
        close = true;
    }


    
    if (close == true){
        
        

        nav[0].style.right = String(extend)+"%";
        this.style.backgroundColor = "grey";
        this.innerHTML = ">";
        return;
    }

    if (close == false){
        
        this.style.backgroundColor = "black";
        this.innerHTML = "<";
        nav[0].style.right = String(non_extend)+"%";

        
        return;
    }



    
    
    



}

