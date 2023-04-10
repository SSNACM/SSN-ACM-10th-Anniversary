const submitButton = document.getElementById('submit');
const email = document.getElementById('email');
const password = document.getElementById('password');
const username = document.getElementById('username');

document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
})

submitButton.addEventListener('click', async () => {
    const data = await register(email.value, password.value, username.value);
    if (data.token) {
        writeCookie('session', data.token);
        window.location.href = '/';
    } else {
        alert(data);
    }
})

document.addEventListener('DOMContentLoaded', () => {
    console.log('loaded');
})

async function register(email, password, username) {
    const response = await fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            password: password,
            username: username
        })
    })
    const data = await response.json();
    return data;
}

function writeCookie(key, val) {
    document.cookie = `${key}=${val}`;
}