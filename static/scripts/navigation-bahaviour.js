
/*document.getElementById("close-navigation").onclick = function(){
    var extend = 0;
    var non_extend = -20;
    var close = true;

    const nav = document.getElementsByClassName("navigation");
    
    
    //if (nav[0].style.right == String(extend)+"%"){
    if (nav[0].style.transform == String(extend)+"%"){
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
*/
document.getElementById("close-navigation").onclick = function(){
    const nav = document.getElementsByClassName("navigation");
    var default_val = '1s'
    locked_val = "999999s"
    console.log(nav[0].style.transitionDuration)
    console.log(locked_val)
    if (nav[0].style.transitionDuration !== locked_val){
        
        this.style.backgroundColor = "grey";
        this.innerHTML = "&#128274;  ";
        nav[0].style.transition = locked_val;
        console.log("0???")
    }
    else{
        console.log("???")

        this.innerHTML = "<";
        
        nav[0].style.transitionDuration = default_val;
        this.style.backgroundColor = "blue";
    }
}














    



    
    
    





