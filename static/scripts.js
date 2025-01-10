document.getElementById('start-extraction').addEventListener('click', async () => {
    const response = await fetch('/extract_match_data');
    const result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
});

document.getElementById('next-page').addEventListener('click', async () => {
    const response = await fetch('/next_page');
    const result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
});

document.getElementById('previous-page').addEventListener('click', async () => {
    const response = await fetch('/previous_page');
    const result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
});
