document.querySelectorAll(".official-links a").forEach(link => {
    link.addEventListener("click", (e) => {
        const confirmVisit = confirm(
            "You are now being redirected to an official Government of India website.\n\n" +
            "Do you want to continue?"
        );

        if (!confirmVisit) {
            e.preventDefault();
        }
    });
});
// Card animation on load
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

// Click interaction (govt-style info)
document.querySelectorAll(".fertilizer-card").forEach(card => {
    card.addEventListener("click", () => {
        alert(
            `ℹ️ ${card.firstChild.textContent}\n\n` +
            "Use as per soil test recommendations.\n" +
            "Avoid overuse to protect soil health."
        );
    });
});