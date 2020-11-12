const donationTable = document.querySelector('#donations');
donationTable.addEventListener('click', (event) => {
	const clicked = event.target.parentNode;

	if (clicked.dataset.type === 'update') {
		const donationId = clicked.dataset.ref;
		fetch(`http://localhost:5000/collect/${donationId}`, {
			method: 'PUT',
		})
			.then((result) => {
				if (result.status == 200) {
					const tr = clicked.closest(`#donation_${donationId}`);
					if (tr.classList.contains('collected')) {
						tr.classList.remove('collected');
					} else {
						tr.classList.add('collected');
					}
				}
			})
			.catch((error) => {
				console.log(error);
			});
	}
});
