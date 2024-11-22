const addTaskButton = document.getElementById("addTaskBtn");
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");
const completedList = document.getElementById("completedList");

addTaskButton.addEventListener("click", function(){
    const taskText = taskInput.value;
    if (taskText === ""){
        alert("you should enter a task!!!!")
        return;
    }
    const li = document.createElement("li");
    li.textContent = taskText;

    const completeButton = document.createElement("button");
    completeButton.textContent = "Complete";

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";

    completeButton.addEventListener("click", function(){
        li.classList.add("completed");
        completedList.appendChild(li);
        completeButton.disabled = true;
    });
    deleteButton.addEventListener("click", function(){
        taskList.removeChild(li);
    });
    li.appendChild(completeButton);
    li.appendChild(deleteButton);
    taskList.appendChild(li)
    taskInput.value = "";
});

taskInput.addEventListener("keypress", function (e){
    if (e.key === "Enter"){
        addTaskButton.click()
    }
})