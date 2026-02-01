// Highlight active navbar link
document.querySelectorAll(".gov-nav a").forEach(link => {
    link.addEventListener("click", () => {
        document.querySelectorAll(".gov-nav a").forEach(l => l.classList.remove("active"));
        link.classList.add("active");
    });
});

// Show official alert on guideline click
document.querySelectorAll(".details-btn").forEach(button => {
    button.addEventListener("click", (e) => {
        e.preventDefault();

        alert(
            "You are being redirected to the official Government of India fertilizer guidelines.\n\n" +
            "Please follow soil-test-based fertilizer recommendations for better yield and sustainability."
        );
    });
});

// Simple page load animation (govt-style subtle)
window.addEventListener("load", () => {
    document.querySelectorAll(".fertilizer-card").forEach((card, index) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(20px)";

        setTimeout(() => {
            card.style.transition = "all 0.5s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 200);
    });
});