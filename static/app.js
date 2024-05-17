function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}
document.getElementById('user-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const gender = document.getElementById('gender').value;
    const csrfToken = getCSRFToken();

    const response = await fetch('/api/users/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ name, age, gender }),
    });
    const data = await response.json();
    console.log('User created:', data);
});

// document.getElementById('health-data-form').addEventListener('submit', async (e) => {
//     e.preventDefault();
//     const csrfToken = getCSRFToken();
//     console.log("sjhdfsd")
//     const userId = document.getElementById('user-id').value;
//     const symptoms = document.getElementById('symptoms').value;

//     const response = await fetch('/api/healthdata/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrfToken
//         },
//         body: JSON.stringify({ user: userId, symptoms }),
//     });
//     const data = await response.json();
//     document.getElementById('recommendations').innerText = data.recommendations;
//     console.log('Health data submitted:', data);
// });
