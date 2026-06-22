document.addEventListener("DOMContentLoaded", () => {

    const inputs = document.querySelectorAll(
        ".account-form input, .account-form select"
    );

    inputs.forEach((input) => {

        input.addEventListener("focus", () => {

            input.parentElement.style.transform = "scale(1.02)";

            input.parentElement.style.transition = "0.3s";

        });

        input.addEventListener("blur", () => {

            input.parentElement.style.transform = "scale(1)";

        });

    });

});