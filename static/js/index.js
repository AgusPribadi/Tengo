// index.js

// Efek animasi ketika menggulung halaman
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    const headerHeight = document.querySelector("header").offsetHeight;
    const elementPosition = element.getBoundingClientRect().top;
    const offsetPosition = elementPosition - headerHeight;

    window.scrollBy({
        top: offsetPosition,
        behavior: "smooth",
    });
}

// Tambahkan event listener untuk tombol "Daftar Sekarang" di header
const ctaButton = document.querySelector(".cta-btn");
ctaButton.addEventListener("click", function (event) {
    event.preventDefault();
    scrollToSection("register");
});

// Efek animasi pada gambar fitur saat dihover
const featureImages = document.querySelectorAll(".feature-card img");
featureImages.forEach((image) => {
    image.addEventListener("mouseenter", function () {
        image.style.transform = "scale(1.1)";
    });

    image.addEventListener("mouseleave", function () {
        image.style.transform = "scale(1)";
    });
});
