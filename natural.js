// Animate cards on load
window.addEventListener("load", () => {
    const cards = document.querySelectorAll(".fertilizer-card");

    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
            card.style.transition = "all 0.6s ease";
        }, index * 120);
    });
});

// Click guidance
document.querySelectorAll(".fertilizer-card").forEach(card => {
    card.addEventListener("click", () => {
        alert(
            `🌿 ${card.firstChild.textContent}\n\n` +
            "Organic fertilizers improve long-term soil health.\n" +
            "Recommended under sustainable agriculture practices."
        );
    });
});

// Safe redirect confirmation
document.querySelectorAll(".official-links a").forEach(link => {
    link.addEventListener("click", (e) => {
        if (!confirm("You are visiting an official Government of India website. Continue?")) {
            e.preventDefault();
        }
    });
});