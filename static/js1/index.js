var x = document.getElementById("login-form");
		var y = document.getElementById("register-form");
		var z = document.getElementById("pointer-btn");
		var l = document.getElementById("login");
		var r = document.getElementById("register");
		var ac = document.getElementById("action_title");

		function register(){
			x.style.left = "-398px";
			y.style.left = "0px";
			z.style.left = "229px";
			l.style.color = "#a0a0a0";
			r.style.color = "#ccaa45";
			ac.textContent = "Register";
		}

		function login(){
			x.style.left = "0px";
			y.style.left = "398px";
			z.style.left = "30px";
			l.style.color = "#ccaa45";
			r.style.color = "#a0a0a0";
			ac.textContent = "Login";
		}