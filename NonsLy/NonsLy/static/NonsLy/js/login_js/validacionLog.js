window.addEventListener("load", ()=>{
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const form = document.getElementById("form");

    form.addEventListener('submit', (e) => {
        e.preventDefault()
        validaCampos()
    })
    const validaCampos = () =>{
        const emailValor = email.value.trim();
        const passwordValor = password.value.trim();

        if(emailValor == ""){
            validaFalla(email, "Campo vacío")
            console.log(email)
        }else if(!validaEmail(emailValor)){
            validaFalla(email, "El e-mail no es válido")
        }else{
            validaOk(email)
        }

        if(passwordValor === ""){
             validaFalla(password, "Campo vacío")
        }else if(passwordValor.length < 8){
            validaFalla(password, "Debe tener como mínimo 8 caracteres")
        }else{
            validaOk(password)
        }
    }
    
    const validaFalla = (input, msj) =>{
        const formControl = input.parentElement     //La propiedad parentElement devuelve el elemento padre del elemento especificado.
        const aviso = formControl.querySelector("p")
        aviso.innerHTML = msj
        formControl.className = "col-12 falla"
    }
    const validaOk = (input) =>{
        const formControl = input.parentElement
        formControl.className = "col-12 ok"
    }

    const validaEmail = (email) => {
        return /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i.test(email);
    } 
})

