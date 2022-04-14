function validate() {
    let uname = document.getElementById('username').value;
    let fname = document.getElementById('fname').value;
    let lname = document.getElementById('lname').value;
    let email = document.getElementById('email').value;
    let pass = document.getElementById('password1').value;
    let conpass = document.getElementById('password2').value;
    let mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    let unameError = 1;
    let fnameError = 1;
    let lnameError = 1;
    let emailError = 1;
    let passError = 1;
    let conpassError = 1;

    if(uname == "" || uname == null){
        document.getElementById('error-uname').innerHTML = '**Please enter your username...';
        unameError = 0;
    }else if(!isNaN(uname[0])){
        document.getElementById('error-uname').innerHTML = '**Username must be start with character...';
        unameError = 0;
    }else{
        document.getElementById('error-uname').innerHTML = '';
        unameError = 1;
    }

    if(fname == "" || fname == null){
        document.getElementById('error-fname').innerHTML = '**Please enter your first name...';
        fnameError = 0;
    }else if(!isNaN(fname[0])){
        document.getElementById('error-fname').innerHTML = '**First name must be start with character...';
        fnameError = 0;
    }else{
        document.getElementById('error-fname').innerHTML = '';
        fnameError = 1;
    }

    if(lname == "" || lname == null){
        document.getElementById('error-lname').innerHTML = '**Please enter your last name...';
        lnameError = 0;
    }else if(!isNaN(lname[0])){
        document.getElementById('error-lname').innerHTML = '**Last name must be start with character...';
        lnameError = 0;
    }else{
        document.getElementById('error-lname').innerHTML = '';
        lnameError = 1;
    }

    if(email == "" || email == null){
        document.getElementById("error-email").innerHTML = "**Please enter your email...";
        emailError = 0;
    }else if(mailformat.test(email) == false){
        document.getElementById("error-email").innerHTML = "Please enter valid email...";
        emailError = 0;
    }else{
        document.getElementById("error-email").innerHTML = "";
        emailError = 1;
    }

    if(pass == "" || pass == null){
        document.getElementById("error-pass").innerHTML = "**Please enter your password...";
        passError = 0;
    }else{
        document.getElementById("error-pass").innerHTML = "";
        passError = 1;
    }  
    
    if(conpass != pass){
        document.getElementById("error-conpass").innerHTML = "**Password are not same. Please check...";
        conpassError = 0;
    }else{
        document.getElementById("error-conpass").innerHTML = "";
        conpassError = 1;
    }

    if((unameError === 1) && (fnameError === 1) && (lnameError === 1) && (emailError === 1) && (passError === 1) && (conpassError === 1)){
        return true;
    }else{
        return false;
    }

    
}