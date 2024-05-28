document.getElementById('paymentForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form from submitting normally

    // Validate personal information fields
    const name = document.getElementById('name').value.trim();
    const address = document.getElementById('address').value.trim();
    const mobile = document.getElementById('mobile').value.trim();
    const pin = document.getElementById('pin').value.trim();

    if (!name || !address || !mobile || !pin) {
        alert('Please fill out all required fields.');
        return;
    }

    // Validate payment method selection
    const paymentMethod = document.getElementById('paymentMethod').value;
    if (!paymentMethod) {
        alert('Please select a payment method.');
        return;
    }

    // Validate additional payment fields for non-COD methods
    if (paymentMethod !== 'cod') {
        const cardNumber = document.getElementById('cardNumber')?.value.trim();
        const expiryDate = document.getElementById('expiryDate')?.value.trim();
        const cvv = document.getElementById('cvv')?.value.trim();
        const paypalEmail = document.getElementById('paypalEmail')?.value.trim();
        const upiId = document.getElementById('upiId')?.value.trim();

        if (paymentMethod === 'creditCard' || paymentMethod === 'debitCard') {
            if (!cardNumber || !expiryDate || !cvv) {
                alert('Please fill out all credit/debit card details.');
                return;
            }
        } else if (paymentMethod === 'paypal') {
            if (!paypalEmail) {
                alert('Please fill out your PayPal email.');
                return;
            }
        } else if (paymentMethod === 'phonepe') {
            if (!upiId) {
                alert('Please fill out your UPI ID.');
                return;
            }
        }
    }

    // If all validations pass, proceed with form submission
    alert('Order placed successfully!');
    // Optionally, here you could send the form data to the server using AJAX or other methods
});

// Update payment details section based on payment method selection
document.getElementById('paymentMethod').addEventListener('change', function () {
    const paymentDetails = document.getElementById('paymentDetails');
    paymentDetails.innerHTML = ''; // Clear previous fields

    const paymentMethod = this.value;

    if (paymentMethod === 'creditCard' || paymentMethod === 'debitCard') {
        paymentDetails.innerHTML = `
            <div class="input-group">
                <label for="cardNumber">Card Number:</label>
                <input type="text" id="cardNumber" name="cardNumber" required>
            </div>
            <div class="input-group">
                <label for="expiryDate">Expiry Date:</label>
                <input type="text" id="expiryDate" name="expiryDate" placeholder="MM/YY" required>
            </div>
            <div class="input-group">
                <label for="cvv">CVV:</label>
                <input type="text" id="cvv" name="cvv" required>
            </div>
        `;
    } else if (paymentMethod === 'paypal') {
        paymentDetails.innerHTML = `
            <div class="input-group">
                <label for="paypalEmail">PayPal Email:</label>
                <input type="email" id="paypalEmail" name="paypalEmail" required>
            </div>
        `;
    } else if (paymentMethod === 'phonepe') {
        paymentDetails.innerHTML = `
            <div class="input-group">
                <label for="upiId">PhonePe UPI ID:</label>
                <input type="text" id="upiId" name="upiId" required>
            </div>
        `;
    }
});
