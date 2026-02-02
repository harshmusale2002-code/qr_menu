fetch("http://127.0.0.1:5000/menu")
  .then(function (res) {
    return res.json();
  })
  .then(function (data) {
    const menuDiv = document.getElementById("menu");

    data.forEach(function (item) {
      const div = document.createElement("div");

      div.innerHTML =
        "<h3>" + item.name + "</h3>" +
        "<p>₹" + item.price + "</p>" +
        "<button onclick=\"addToCart(" + item.id + ", '" + item.name + "', " + item.price + ")\">Add</button>";

      menuDiv.appendChild(div);
    });
  });

function addToCart(id, name, price) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  cart.push({ id: id, name: name, price: price });
  localStorage.setItem("cart", JSON.stringify(cart));
  alert("Item added to cart");
}
