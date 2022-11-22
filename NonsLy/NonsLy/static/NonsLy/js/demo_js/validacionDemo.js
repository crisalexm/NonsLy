window.addEventListener('load', ()=> {
    const form = document.getElementById("form");
    const nombre = document.getElementById("nombre");
    const apellido = document.getElementById("apellido");
    const email = document.getElementById("email");
    const nombre_colegio = document.getElementById("nombre_colegio");
    const cargo = document.getElementById("cargo");
    const telefono = document.getElementById("telefono");
    const comuna = document.getElementById("comuna");
    const direccion = document.getElementById("direccion");

    form.addEventListener('submit', (e) => {
        e.preventDefault()
        validaCampos()
    }) //uso de parámetro la letra "e" para la función

    const validaCampos = () => {
        //capturo los valores ingresados por el usuario
        const nombreValor = nombre.value.trim() //trim elimana espacios en blanco antes del primer carácter
        const apellidoValor = apellido.value.trim() //trim elimana espacios en blanco antes del primer carácter
        const emailValor = email.value.trim() //trim elimana espacios en blanco antes del primer carácter
        const n_colegioValor = nombre_colegio.value.trim() //trim elimana espacios en blanco antes del primer carácter
        const cargoValor = cargo.value.trim() //trim elimana espacios en blanco antes del primer carácter
        const comunaValor = comuna.value.trim() //trim elimana espacios en blanco antes del primer carácter
        const direccionValor = direccion.value.trim() //trim elimana espacios en blanco antes del primer carácter
        const telefonoValor = telefono.value.trim() //trim elimana espacios en blanco antes del primer carácter

        //validando campos nombre
        if(nombreValor ===""){
            
            validaFalla(nombre, "Campo vacío")
        } else{
            
            validaOk(nombre)
        }
        //validando campos apellido

        if(apellidoValor ===""){
            
            validaFalla(apellido, "Campo vacío")
        } else{
            
            validaOk(apellido)
        }
        //validando campos nombre Colegio

        if(n_colegioValor ===""){
            
            validaFalla(nombre_colegio, "Campo vacío")
        } else{
            
            validaOk(nombre_colegio)
        }
        //validando campos Cargo

        if(cargoValor ===""){
            
            validaFalla(cargo, "Campo vacío")
        } else{
            
            validaOk(cargo)
        }

        //validando campos email
        if(emailValor ==""){
            validaFalla(email, "Campo vacío")
        }else if(!validaEmail(emailValor)){
            validaFalla(email, "El e-mail no es válido")
        }else{
            validaOk(email)
        }

        //validando campos comuna
        if(comunaValor ===""){
            
            validaFalla(comuna, "Campo vacío")
        } else{
    
        validaOk(comuna)
        }

        //validando campos direccion
        if(direccionValor ===""){
            
            validaFalla(direccion, "Campo vacío")
        } else{
    
        validaOk(direccion)
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
    }
    const validaFalla = (input, msj) =>{
            const formControl = input.parentElement     //La propiedad parentElement devuelve el elemento padre del elemento especificado.
            const aviso = formControl.querySelector("p")
            aviso.innerHTML = msj
            formControl.className = "col-md-6 falla"
        }

    const validaOk = (input, msj) =>{
            const formControl = input.parentElement
            formControl.className = "col-md-6 ok"

        }

    const validaEmail = (email) => {
        return /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i.test(email);
    }  
})