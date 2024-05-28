function updateCartSummary() {
  let totalQuantity = 0;
  let totalPrice = 0;

  const cartItems = document.querySelectorAll('.cart-item');

  cartItems.forEach(item => {
      const quantity = parseInt(item.querySelector('.quantity-buttons span').textContent);
      const price = parseFloat(item.getAttribute('data-price'));
      totalQuantity += quantity;
      totalPrice += quantity * price;
  });

  const totalQuantityElement = document.getElementById('total-quantity');
  const totalPriceElement = document.getElementById('total-price');
  const emptyMessage = document.getElementById('empty-message');
  const cartSummary = document.querySelector('.cart-summary');

  totalQuantityElement.textContent = totalQuantity;
  totalPriceElement.textContent = 'Rs ' + totalPrice.toFixed(2);

  // Check if cart is empty
  if (cartItems.length === 0) {
      emptyMessage.classList.remove('hidden');
      cartSummary.classList.add('hidden');
  } else {
      emptyMessage.classList.add('hidden');
      cartSummary.classList.remove('hidden');
  }
}

function increaseQuantity(itemId) {
  const item = document.getElementById(itemId);
  let quantityElement = item.querySelector('.quantity-buttons span');
  let quantity = parseInt(quantityElement.textContent);
  quantity++;
  quantityElement.textContent = quantity;
  updateCartSummary();
}

function decreaseQuantity(itemId) {
  const item = document.getElementById(itemId);
  let quantityElement = item.querySelector('.quantity-buttons span');
  let quantity = parseInt(quantityElement.textContent);
  if (quantity > 1) {
      quantity--;
      quantityElement.textContent = quantity;
      updateCartSummary();
  }
}

function removeItem(itemId) {
  const item = document.getElementById(itemId);
  item.parentNode.removeChild(item);
  updateCartSummary();
}

function placeOrder() {
  window.location.href = "payment.html"; // Replace with your payment page URL
}

// Initial call to update the summary based on initial quantities
updateCartSummary();
