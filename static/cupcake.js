const BASE_URL = 'http://localhost:5000/api';

// Create the HTML of the cupcake
function generateCupcakeHTML(cupcake) {
    return `
      <div data-cupcake-id=${cupcake.id}>
        <li>
          ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
          <button class="delete">X</button>
        </li>
        <img class="Cupcake-img"
              src="${cupcake.image}"
              alt="(no image provided)">
      </div>
    `;
}

// Add the new cupcake to the cupcakes list on the page.
async function showInitialCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);

    for (let cupcakeData of response.data.cupcakes) {
        let newCupcake = $(generateCupcakeHTML(cupcakeData));
        $('#cupcakes-list').append(newCupcake);
    }
}

// Handles the form for adding/creating a new cupcake.
$('#new-cupcake-form').on('submit', async function (evt) {
    evt.preventDefault();

    //////////////Pulls the data entered from the form
    let flavor = $('#flavor-form').val();
    let rating = $('#rating-form').val();
    let size = $('#size-form').val();
    let image = $('#image-form').val();

    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor,
        rating,
        size,
        image,
    });

    let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
    $('#cupcakes-list').append(newCupcake);
    $('#new-cupcake-form').trigger('reset');
});

// Handles deleting a cupcake.
$('#cupcakes-list').on('click', '.delete', async function (evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest('div');
    let cupcakeId = $cupcake.attr('data-cupcake-id');

    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
});

$(showInitialCupcakes);
