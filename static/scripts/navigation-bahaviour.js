
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
    console.log(nav[0].style.transitionDuration)
    if (nav[0].style.transitionDuration === default_val){
        this.innerHTML = ">";
        
        nav[0].style.transitionDuration = "9999999999999s";
        this.style.backgroundColor = "black";
        console.log("???!!!!!@@##@#")
    }
    else{
        console.log("??dsada?!!!")
        this.style.backgroundColor = "grey";
        this.innerHTML = "<";
        nav[0].style.transition = default_val;
    }
}














    



    
    
    





