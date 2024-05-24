const calendar = document.getElementById('calendar');
const daysInMonth = 30; // Assuming a month with 30 days for simplicity

for (let i = 1; i <= daysInMonth; i++) {
  const day = document.createElement('div');
  day.className = 'day';
  day.innerText = i;
  day.addEventListener('click', () => {
    day.classList.toggle('present');
    day.classList.toggle('absent');
  });
  calendar.appendChild(day);
}
