const cropDetails = {
    rice: `
        <h2>🌱 Rice (Paddy) – Crop Guide</h2>
        <ul>
            <li>Soil: Clayey / Loamy</li>
            <li>Water: High requirement</li>
            <li>Climate: Warm & humid</li>
            <li>Duration: 3–6 months</li>
            <li>Stages: Nursery → Transplant → Flower → Harvest</li>
        </ul>
    `,
    wheat: `
        <h2>🌾 Wheat – Crop Guide</h2>
        <ul>
            <li>Soil: Well-drained loam</li>
            <li>Water: Moderate</li>
            <li>Climate: Cool & dry</li>
            <li>Duration: 4–5 months</li>
        </ul>
    `,
    maize: `
        <h2>🌽 Maize – Crop Guide</h2>
        <ul>
            <li>Soil: Fertile loam</li>
            <li>Water: Moderate</li>
            <li>Climate: Warm</li>
            <li>Duration: 3–4 months</li>
        </ul>
    `
};

// Crop switching
document.querySelectorAll(".crop-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".crop-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        document.getElementById("cropDetails").innerHTML = cropDetails[btn.dataset.crop];
    });
});

// Add post (Instagram-style)
function addPost() {
    const text = document.getElementById("postText").value;
    if (!text) return;

    const post = document.createElement("div");
    post.className = "post";
    post.innerHTML = `
        <p>${text}</p>
        <span>Posted just now</span>
    `;

    document.getElementById("feed").prepend(post);
    document.getElementById("postText").value = "";
}