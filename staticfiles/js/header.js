const menuBtn = document.getElementById("menuBtn");
const navMenu = document.getElementById("navMenu");
const navbar = document.querySelector(".navbar");
const navLinks = document.querySelectorAll(".nav-links a");

menuBtn.addEventListener("click", () => {
    navMenu.classList.toggle("show");

    if (navMenu.classList.contains("show")) {
        menuBtn.innerHTML = "&times;";
    } else {
        menuBtn.innerHTML = "&#9776;";
    }
});

window.addEventListener("scroll", () => {
    if (window.scrollY > 15) {
        navbar.classList.add("active");
    } else {
        navbar.classList.remove("active");
    }
});

navLinks.forEach((link) => {
    link.addEventListener("click", () => {
        navLinks.forEach((item) => item.classList.remove("current"));
        link.classList.add("current");

        if (window.innerWidth <= 992) {
            navMenu.classList.remove("show");
            menuBtn.innerHTML = "&#9776;";
        }
    });
});

window.addEventListener("resize", () => {
    if (window.innerWidth > 992) {
        navMenu.classList.remove("show");
        menuBtn.innerHTML = "&#9776;";
    }
});