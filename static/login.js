const submitButton = document.getElementById('submit');
const email = document.getElementById('email');
const password = document.getElementById('password');

document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
})

submitButton.addEventListener('click', async () => {
    const data = await login(email.value, password.value);
    if (data.token) {
        writeCookie('session', data.token);
        window.location.href = '/';
    } else {
        alert(data);
    }
})

async function login(email, password) {
    const response = await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    })
    const data = await response.json();
    return data;
}

function writeCookie(key, val) {
    document.cookie = `${key}=${val}`;
}