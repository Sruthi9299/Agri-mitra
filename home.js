const API_BASE = window.API_BASE || 'http://localhost:5000';

function openMenu(){
    document.getElementById("menu").style.left="0";
}

function closeMenu(){
    document.getElementById("menu").style.left="-260px";
}

// Username: from localStorage or /api/me
let user = localStorage.getItem('agri_user') || 'Farmer';
const usernameEl = document.getElementById("username");
if (usernameEl) usernameEl.innerText = user;

(async function() {
    const token = localStorage.getItem('agri_token');
    if (!token || !usernameEl) return;
    try {
        const res = await fetch(API_BASE + '/api/me', { headers: { 'Authorization': 'Bearer ' + token, 'X-Token': token } });
        const data = await res.json().catch(function() { return {}; });
        if (data.logged_in && data.full_name) {
            user = data.full_name;
            usernameEl.innerText = user;
            localStorage.setItem('agri_user', user);
        }
    } catch (e) {}
})();