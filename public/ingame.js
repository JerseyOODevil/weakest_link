let game_started = false;
let timer = 90;
let timerInterval = null;

function updateTimerDisplay() {
    const timerElement = document.getElementById('Timer');
    timerElement.textContent = `Timer: ${timer}`;
}

function startCountdown() {
    timerInterval = setInterval(() => {
        if (timer > 0) {
            timer--;
            updateTimerDisplay();
        } else {
            clearInterval(timerInterval);
            game_started = false;
            // Можно добавить обработку окончания таймера
        }
    }, 1000);
}

function btnClick() {
    if (!game_started) {
        game_started = true;
        timer = 90;
        updateTimerDisplay();
        startCountdown();
    }
}