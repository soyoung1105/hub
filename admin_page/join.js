document.getElementById("signupBtn").addEventListener("click", function() {
    const formContainer = document.getElementById("container");
    
    // 폼이 숨겨져 있으면 보이게, 보이면 숨김
    if (formContainer.style.display === "none") {
      formContainer.style.display = "block";
    } else {
      formContainer.style.display = "none";
    }
  });
  