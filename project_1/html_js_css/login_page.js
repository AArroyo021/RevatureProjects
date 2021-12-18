const url = "http://127.0.0.1:5000/";

let button = document.getElementById("getData");
button.onclick = employeeLogin;

async function employeeLogin(){
    let url_attach = "login/employee";

    let usernameInput = document.getElementById("usernameInput");
    let passwordInput = document.getElementById("passwordInput");

    console.log(url + url_attach);
    console.log(usernameInput.value + " " + passwordInput.value)

    let response = await fetch(url + url_attach, {
        headers: {'Content-Type': 'application/json'},
        method: "POST", 
        body: JSON.stringify({"employeeUsername": usernameInput.value, "employeePassword": passwordInput.value})
    });

    if(response.status === 200){
        let info = await response.json();
        console.log(info);

        if(info === true)
            window.location.href = "employee_page.html";

    }
    else{
        console.log("This ain't working")
    }
}