const url = "http://127.0.0.1:5000/";
let loginPersonType = "";

let button = document.getElementById("getData");
let radio1 = document.getElementById("employeeRadio");
let radio2 = document.getElementById("managerRadio")
button.onclick = loginType;

function loginType(){
    if(radio1.checked){
        loginPersonType = radio1.value;
        login(loginPersonType);
    }
    else if(radio2.checked){
        loginPersonType = radio2.value;
        login(loginPersonType);

    }
}

async function login(loginPT){
    let url_attach = "login/" + loginPT;
    const currentUsername = loginPT + "Username";
    const currentPassword = loginPT + "Password";

    let usernameInput = document.getElementById("usernameInput");
    let passwordInput = document.getElementById("passwordInput");

    console.log(url + url_attach);
    console.log(usernameInput.value + " " + passwordInput.value);
    console.log(currentUsername + " " + currentPassword);

    let response = await fetch(url + url_attach, {
        headers: {'Content-Type': 'application/json'},
        method: "POST", 
        body: JSON.stringify({[currentUsername]: usernameInput.value, [currentPassword]: passwordInput.value})
    });

    if(response.status === 200){
        let info = await response.json();
        console.log(info);
        console.log(info[1]); 
        //keeps the state of the alert based on the first run
        if(info === "Login Failed: Username or Password is incorrect"){
            alert(info);
        }

        if(info[0] === true){
            sessionStorage.setItem("currentId", info[1]);
            window.location.href = loginPT +"_page.html";
        }
    }
    else{
        console.log("This ain't working");
    }
}