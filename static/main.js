let current = 1;
let max = 4;
let completed = false;

let currentUser = null;

function getMe(callback = (d) => {}) {
    fetch('/me')
        .then(r =>{ 
            if (r.status === 404) {
                window.location.href = '/login';
            }
            return r.json()
        })
        .then(data => {
            currentUser = data;
            console.log(currentUser);
            callback(currentUser)
        });
}

const stepDelay = {
    1: 5000,
    2: 10000,
    3: 4000,
}

function yetto(index) {
    const progress = document.querySelector(`[data-index="${index}"]`);
    progress.querySelector('.loader').style.opacity = 0;
    progress.querySelector('.loader').style.width = 0;
    progress.querySelector('.loader').style.marginLeft = '0';
    progress.querySelector('.loader').style.marginRight = '0';
    progress.querySelector('.check').style.opacity = 0;
    progress.querySelector('.check').style.width = 0;
    progress.querySelector('.idle').style.opacity = 1;
    progress.querySelector('.idle').style.width = 'fit-content';
    progress.style.transform = `translateY(70%)`;
    progress.style.opacity = 0;
}    

function doing(index) {
    const progress = document.querySelector(`[data-index="${index}"]`);
    progress.querySelector('.loader').style.opacity = 1;
    progress.querySelector('.loader').style.width = '1.5em';
    progress.querySelector('.loader').style.marginLeft = '1em';
    progress.querySelector('.loader').style.marginRight = '.25em';
    progress.querySelector('.check').style.opacity = 0;
    progress.querySelector('.check').style.width = 0;
    progress.querySelector('.idle').style.opacity = 0;
    progress.querySelector('.idle').style.width = 0;
    progress.style.transform = `translateY(0%)`;
    progress.style.opacity = 1;
}    

function done(index) {
    const progress = document.querySelector(`[data-index="${index}"]`);
    progress.querySelector('.loader').style.opacity = 0;
    progress.querySelector('.loader').style.width = 0;
    progress.querySelector('.loader').style.marginLeft = '0';
    progress.querySelector('.loader').style.marginRight = '0';
    progress.querySelector('.check').style.opacity = 1;
    progress.querySelector('.check').style.width = 'fit-content';
    progress.querySelector('.idle').style.opacity = 0;
    progress.querySelector('.idle').style.width = 0;
    progress.style.transform = `translateY(-80%)`;
    progress.style.opacity = 0;
}    


function trigger() {
    doing(current);
    if (completed) {
        [1, 2, 3, 4].forEach((index) => {
            done(index);
        });
    }
    if (current === max) {
        if (!completed) {
            setTimeout(() => {
                trigger();
            }, 1/24 * 1000);
        }
    } else {
        setTimeout(() => {
            done(current);
            current++;
            trigger();
        }, stepDelay[current]);
    }
}

function reset() {
    current = 1;
    completed = false;
    [1, 2, 3, 4].forEach((index) => {
        yetto(index);
    });
}

function complete() {
    completed = true;
}

function writeBreakdown(consept, topics) {
    /* existing = JSON.parse(localStorage.getItem("generations"));
    if (existing == null) {
        existing = {};
    }
    existing[consept] = topics;
    localStorage.setItem("generations", JSON.stringify(existing)); */
    fetch("/api/create", {
        method: "POST",
        body: JSON.stringify( {topic: consept, subtopics: topics} ),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(r => r.json()).then(data => console.log("SYNC SUCCESS: ", data))
}

function clean(data) {
    console.log(data);
    data["subtopics"] = JSON.parse(data["subtopics"]);
    return data
}

function readBreakdowns(callback) {
    /* return JSON.parse(localStorage.getItem("generations")); */
    return fetch("/api/getPrompts").then(r => r.json()).then(data => callback(clean(data)));
}

function readBreakdown(consept, callback) {
    /* return JSON.parse(localStorage.getItem("generations"))[consept]; */
    return fetch("/api/getPrompts").then(r => r.json()).then(data => callback(data.filter(d => d.topic === consept)[0]));
}

function readConsepts(callback) {
    /* return Object.keys(JSON.parse(localStorage.getItem("generations"))); */
    return fetch("/api/getPrompts").then(r =>  r.json()).then(data => {
        data = data || [];
        console.log(data);
        callback(data.map(d => d.topic));
    });
}


async function getBreakdown(consept) {
    reset();
    trigger();
    const response = await fetch('/api/breakdown', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            consept: consept
        })
    });
    const data = await response.json();
    complete();
    return data;
}

const btn = document.getElementById('btn');
const result = document.getElementById('result');
const conseptInput = document.getElementById('consept');


function renderData(data) {
    console.log("renderData", data);
    result.innerHTML = '';
    data.subtopics.forEach(topic => {
        const div = document.createElement('div');
        div.classList.add('topic');
        div.innerHTML = `<div class="name">${topic.name}</div><div class="description">${topic.description}</div>`;
        result.appendChild(div);
        setTimeout(() => {
            div.style.opacity = 1;
        }, Math.random() * 750);
    })
}

btn.addEventListener('click', async () => {

    if (!currentUser) {
        alert("You must be logged in to use this feature");
        return;
    }

    result.innerHTML = '';
    btn.disabled = true;
    const data = await getBreakdown(conseptInput.value);
    renderData(data);
    btn.disabled = false;
    writeBreakdown(consept.value, data.subtopics);
    readConsepts(renderConsepts);
});


document.addEventListener('DOMContentLoaded', () => {
    readConsepts(renderConsepts);
    getMe(userData => {
        
        if (userData) {
            currentUser = userData;
            document.getElementById('user').innerHTML = `Logged in as ${userData.username}`;
        }


    });
})


const conseptsMenu = document.getElementById('consepts__toggle');
const consepts = document.getElementById('consepts');

conseptsMenu.addEventListener('click', () => {
    consepts.classList.toggle('show');
    conseptsMenu.classList.toggle('locked');
});

function renderConsepts(consepts) {
    const conseptsContainer = document.getElementById('consepts__inner')
    conseptsContainer.innerHTML = '';
    consepts.forEach(consept => {
        const div = document.createElement('div');
        div.classList.add('consept');
        div.innerHTML = consept;
        div.addEventListener('click', async () => {
            readBreakdown(consept, renderData);
            conseptInput.value = consept;
        });
        conseptsContainer.appendChild(div);
    });
}


function readCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for(let i=0;i < ca.length;i++) {
        let c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}