window.addEventListener('load', ()=>{
    const form = document.getElementById("form");
    const nombre = document.getElementById("nombre");
    const apellido = document.getElementById("apellido");
    const email = document.getElementById("email");
    const telefono = document.getElementById("telefono");
    const comentario = document.getElementById("comentario");

    form.addEventListener('submit', (e) => {
        e.preventDefault()
        validaCampos()
    })

    const validaCampos = () =>{
        const nombreValor = nombre.value.trim() //trim elimana espacios en blanco antes del primer carácter
        const apellidoValor = apellido.value.trim() //trim elimana espacios en blanco antes del primer carácter
        const emailValor = email.value.trim() //trim elimana espacios en blanco antes del primer carácter
        const telefonoValor = telefono.value.trim() //trim elimana espacios en blanco antes del primer carácter
        const comentarioValor = comentario.value.trim() //trim elimana espacios en blanco antes del primer carácter

        //validando campos nombre
        if(nombreValor === ""){
            
            validaFalla(nombre, "Campo vacío")
        } else{
            
            validaOk(nombre)
        }

        //validando campos apellido

        if(apellidoValor === ""){
            
            validaFalla(apellido, "Campo vacío")
        } else{
            
            validaOk(apellido)
        }

        //validando campos email
        if(emailValor ==""){
            validaFalla(email, "Campo vacío")
        }else if(!validaEmail(emailValor)){
            validaFalla(email, "El e-mail no es válido")
        }else{
            validaOk(email)
        }

        //validando campos telefono
        if(telefonoValor ===""){
            
            validaFalla(telefono, "Campo vacío")
        }else if(telefonoValor.length < 9 ||telefonoValor.length > 9 ){
            validaFalla(telefono, "No debe ser menor a 9 ni mayor a 9")
        }

        else{
    
            validaOk(telefono)
            }

        //validando campos apellido
        if(comentarioValor ===""){
            
            validaFalla(comentario, "Campo vacío")
        } else{
            
            validaOk(comentario)
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

