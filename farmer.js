// ===== API BASE (same origin on Replit; override in .env or config) =====
const API_BASE = window.API_BASE || 'http://localhost:5000';

// ===== ELEMENTS =====
const loginTab = document.getElementById("loginTab");
const registerTab = document.getElementById("registerTab");

const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");

const dobInput = document.getElementById("dob");
const ageError = document.getElementById("ageError");

// ===== TAB SWITCHING =====
loginTab.addEventListener("click", () => {
    loginTab.classList.add("active");
    registerTab.classList.remove("active");

    loginForm.style.display = "flex";
    registerForm.style.display = "none";
});

registerTab.addEventListener("click", () => {
    registerTab.classList.add("active");
    loginTab.classList.remove("active");

    registerForm.style.display = "flex";
    loginForm.style.display = "none";
});

// ===== OTP FUNCTION – call backend =====
async function sendOTP(type) {
    const phoneEl = type === 'login' ? document.getElementById('loginPhone') : document.getElementById('regPhone');
    const phone = (phoneEl && phoneEl.value || '').trim();
    if (phone.length !== 10) {
        alert('Please enter a valid 10-digit phone number.');
        return;
    }
    try {
        const res = await fetch(`${API_BASE}/api/send-otp`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phone })
        });
        const data = await res.json().catch(() => ({}));
        if (!res.ok) {
            alert(data.error || 'Failed to send OTP');
            return;
        }
        if (type === 'login') {
            document.getElementById('loginOtp').style.display = 'block';
            document.getElementById('loginBtn').style.display = 'block';
            if (data.demo_otp) alert('Demo OTP: ' + data.demo_otp);
            else alert('OTP sent successfully.');
        } else {
            document.getElementById('registerOtp').style.display = 'block';
            document.getElementById('registerBtn').style.display = 'block';
            if (data.demo_otp) alert('Demo OTP: ' + data.demo_otp);
            else alert('OTP sent successfully.');
        }
    } catch (e) {
        alert('Network error. Is the backend running at ' + API_BASE + '?');
    }
}

// ===== AGE VALIDATION =====
if (dobInput) {
    dobInput.addEventListener("change", () => {
        const dob = new Date(dobInput.value);
        const today = new Date();

        let age = today.getFullYear() - dob.getFullYear();
        const monthDiff = today.getMonth() - dob.getMonth();

        if (
            monthDiff < 0 ||
            (monthDiff === 0 && today.getDate() < dob.getDate())
        ) {
            age--;
        }

        if (age < 18) {
            if (ageError) ageError.style.display = "block";
            dobInput.value = "";
        } else {
            if (ageError) ageError.style.display = "none";
        }
    });
}

// ===== REGISTER SUBMIT – call backend =====
async function registerUser(event) {
    event.preventDefault();
    const full_name = document.getElementById('regFullName')?.value?.trim();
    const phone = document.getElementById('regPhone')?.value?.trim();
    const otp = document.getElementById('registerOtp')?.value?.trim();
    const age = document.getElementById('age')?.value;
    const dob = document.getElementById('dob')?.value;
    const preferred_language = document.getElementById('regLanguage')?.value || 'English';
    const location = document.getElementById('regLocation')?.value?.trim() || '';
    const soil_type = document.getElementById('regSoilType')?.value?.trim() || '';

    if (!full_name || !phone || phone.length !== 10) {
        alert('Full name and valid 10-digit phone required.');
        return;
    }
    if (!otp) {
        alert('Please enter OTP.');
        return;
    }
    try {
        const res = await fetch(`${API_BASE}/api/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                full_name, phone, otp, age: age ? parseInt(age, 10) : null, dob: dob || null,
                preferred_language, location, soil_type
            })
        });
        const data = await res.json().catch(() => ({}));
        if (!res.ok) {
            alert(data.error || 'Registration failed');
            return;
        }
        if (data.token) {
            localStorage.setItem('agri_token', data.token);
            localStorage.setItem('agri_user', data.full_name || full_name);
        }
        alert('Registration successful! Redirecting...');
        loginTab.click();
    } catch (e) {
        alert('Network error.');
    }
}

// ===== LOGIN SUBMIT – call backend =====
async function loginUser(event) {
    event.preventDefault();
    const phone = document.getElementById('loginPhone')?.value?.trim();
    const otp = document.getElementById('loginOtp')?.value?.trim();

    if (!phone || phone.length !== 10 || !otp) {
        alert('Phone and OTP required.');
        return;
    }
    try {
        const res = await fetch(`${API_BASE}/api/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phone, otp, user_name: document.getElementById('loginUserName')?.value?.trim() })
        });
        const data = await res.json().catch(() => ({}));
        if (!res.ok) {
            alert(data.error || 'Login failed');
            return;
        }
        if (data.token) {
            localStorage.setItem('agri_token', data.token);
            localStorage.setItem('agri_user', data.full_name || 'Farmer');
        }
        alert('Login successful!');
        window.location.href = 'index.html';
    } catch (e) {
        alert('Network error.');
    }
}

// ===== BIND FORMS =====
if (registerForm) {
    registerForm.addEventListener('submit', registerUser);
}
if (loginForm) {
    loginForm.addEventListener('submit', loginUser);
}

// ===== LOCATION / SOIL (demo – set defaults or open map) =====
function openMap() {
    const loc = prompt('Enter your location (e.g. Andhra Pradesh):', document.getElementById('regLocation')?.value || 'Andhra Pradesh');
    const soil = prompt('Enter soil type (e.g. Loamy, Clayey):', document.getElementById('regSoilType')?.value || 'Loamy');
    if (loc != null) document.getElementById('regLocation').value = loc || '';
    if (soil != null) document.getElementById('regSoilType').value = soil || '';
}
