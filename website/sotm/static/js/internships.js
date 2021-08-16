document.addEventListener('input', function (event) {

	// Only run for #wizard select
	if (event.target.id !== 'position-filter') return;

    let position = event.target.value;
    let new_active_element = document.getElementById(position + '_opportunities');
    let prev_active_element = document.getElementsByClassName("active_position")[0];
    prev_active_element.classList.remove('active_position');
    new_active_element.classList.add('active_position');
}, false);