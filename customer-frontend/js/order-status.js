const params = new URLSearchParams(window.location.search);
const orderId = params.get('orderId');


document.getElementById('status').innerText = `Your Order ID: ${orderId}`;