window.addEventListener("load", ()=>{
    const email = document.getElementById("email");
    const rut = document.getElementById("rut");
    const form = document.getElementById("form");

    form.addEventListener('submit', (e) => {
        e.preventDefault()
        validaCampos()
    
    })
    const validaCampos = () =>{
        const emailValor = email.value.trim();
        const rutValor = rut.value.trim();

        if(emailValor == ""){
            validaFalla(email, "Campo vacío")
            console.log(email)
        }else if(!validaEmail(emailValor)){
            validaFalla(email, "El e-mail no es válido")
        }else{
            validaOk(email)
        }

        if(rutValor === ""){
             validaFalla(rut, "Campo vacío")
        }else if(rutValor.length < 7){
            validaFalla(rut, "Debe tener como mínimo 7 caracteres")
        }else{
            validaOk(rut)
        }
    }
    
    const validaFalla = (input, msj) =>{
        const formControl = input.parentElement     //La propiedad parentElement devuelve el elemento padre del elemento especificado.
        const aviso = formControl.querySelector("p")
        aviso.innerHTML = msj
        formControl.className = "form-group falla"
    }
    const validaOk = (input) =>{
        const formControl = input.parentElement
        formControl.className = "form-group ok"
    }

    const validaEmail = (email) => {
        return /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i.test(email);
    } 
})

