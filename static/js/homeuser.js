const links = document.querySelector("#links");
const link_dropdown = document.querySelector("#link-dropdown");


links.addEventListener("click", (e) => {
    e.preventDefault();
    link_dropdown.classList.toggle("is-hidden");
});

console.log("ok");