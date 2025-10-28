const sidebar = document.querySelector('.sidebar');

// Cuando el mouse entra a la zona izquierda de la pantalla
document.addEventListener('mousemove', (e) => {
  if (e.clientX < 50) {
    sidebar.classList.add('open');
  } else if (!sidebar.matches(':hover')) {
    sidebar.classList.remove('open');
  }
});

// Si el mouse sale del sidebar, se oculta
sidebar.addEventListener('mouseleave', () => {
  sidebar.classList.remove('open');
});
