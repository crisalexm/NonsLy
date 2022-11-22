btn.addEventListener('click', showHide)

function showHide(number){
   
    var btn = document.getElementById("btnText_"+number)
    var content = document.getElementById("contents_"+number)
    /* if(content.style.display == "" || content.style.display =="block"){
        content.style.display = "none";
        btn.innerHTML="Mostrar contenido";
    }
    else{
        content.style.display = "block";
        btn.innerHTML="Ocultar contenidos";
    } */
    content.classList.toggle('show');
    if(content.classList.contains('show')){
        btn.innerHTML = "Ocultar contenido";
    }
    else{
        btn.innerHTML = "Mostrar contenido";
    }
}

