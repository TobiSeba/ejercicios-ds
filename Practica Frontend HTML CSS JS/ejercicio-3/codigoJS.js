const inputNombre = document.getElementById("input-nombre")
const inputCorreo = document.getElementById("input-correo")
const botonEnviar = document.getElementById("boton-enviar")
const mensaje = document.getElementById("mensaje")

botonEnviar.addEventListener("click", function(){
    if(inputNombre.value === "" || inputCorreo.value === ""){
        mensaje.textContent = "ERROR: Debe rellenar el formulario para poder enviar.";
        mensaje.className = "error"
    } else{
        mensaje.textContent = "Se ha enviado el formulario correctamente.";
        mensaje.className = "exito"
    }
    inputNombre.value = "";
    inputCorreo.value = "";
})