function register() {
    var emailInput = document.getElementById("register-email");
    var passwordInput = document.getElementById("register-password");
    var registerMsg = document.getElementById("register-msg");
  
    var email = emailInput.value.trim();
    var password = passwordInput.value.trim();
  
    if (email !== "" && password !== "") {
      window.location.href = "index.html";
      return false;
    } else {
      registerMsg.innerHTML = "Por favor, preencha todos os campos.";
      registerMsg.style.display = "block";
      emailInput.value = "";
      passwordInput.value = "";
      return false;
    }
  }
  function login() {
    var usernameInput = document.getElementById("login-username");
    var passwordInput = document.getElementById("login-password");
    var loginMsg = document.getElementById("login-msg");
  
    var username = usernameInput.value.trim();
    var password = passwordInput.value.trim();
  
    if (username !== "" && password !== "") {
      window.location.href = "index.html";
      return false;
    } else {
      loginMsg.innerHTML = "Credenciais inválidas. Por favor, tente novamente.";
      loginMsg.style.display = "block";
      usernameInput.value = "";
      passwordInput.value = "";
      return false;
    }
  }