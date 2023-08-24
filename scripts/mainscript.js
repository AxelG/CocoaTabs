function scrollToTop() {
    const htmlElement = document.querySelector('html');

    htmlElement.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

function deployMenu() {
    const menu = document.getElementById('menu');
    const menu_ov = document.getElementById('menu-ov');

    menu.style.display = "block";
    menu_ov.style.display = "block";
}

function delMenu() {
    const menu = document.getElementById('menu');
    const menu_ov = document.getElementById('menu-ov');

    menu.style.display = "none";
    menu_ov.style.display = "none";
}