const inputTarea = document.getElementById("input-tarea")
const botonAgregar = document.getElementById("boton-agregar")
const listaTareas = document.getElementById("lista-tareas")

function agregarTarea(){
    if (inputTarea.value === ""){
        return;
    }

    const tarea = document.createElement("li");
    tarea.textContent = inputTarea.value;

    tarea.addEventListener("click", function(){tarea.remove()});

    listaTareas.append(tarea);

    inputTarea.value = "";
}

botonAgregar.addEventListener("click", agregarTarea)