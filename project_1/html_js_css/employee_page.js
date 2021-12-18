const header = document.createElement("h1");
header.textContent = `you logged in successfully`;
document.body.appendChild(header);

const url = "http://127.0.0.1:5000/";

function logout(){
    sessionStorage.clear();
    window.location.href = "login_page.html";
}

async function employeeReimbursement(){
}