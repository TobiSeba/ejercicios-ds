const contador = document.getElementById("contador");
const botonSumar = document.getElementById("boton-sumar")
const botonRestar = document.getElementById("boton-restar")
let cuenta = 0;

botonSumar.addEventListener("click", function(){
    cuenta = cuenta + 1;
    contador.textContent = cuenta;
})

botonRestar.addEventListener("click", function(){
    cuenta = cuenta - 1;
    contador.textContent = cuenta;
})