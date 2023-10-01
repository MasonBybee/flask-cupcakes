const URL = "http://127.0.0.1:8080/api";

// spent too long trying to understand what the assignment was so I added the notes from the solution to work off that

/** given data about a cupcake, generate html */

function capitalize(word) {
  const str = String(word);
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function gen_html(cupcake) {
  return `
        <li data-id= "${cupcake.id}" class="list-group-item">
        Flavor: ${capitalize(cupcake.flavor)} - Size: ${capitalize(
    cupcake.size
  )} - Rating: ${cupcake.rating}
        <img class="img-thumbnail list-cupcake-img" src="${cupcake.image}">
        <button id="delete-cupcake" class="btn btn-danger btn-sm">X</button>
        </li>
        `;
}

/** put initial cupcakes on page. */

async function showCupcakes() {
  const resp = await axios.get(`${URL}/cupcakes`);
  data = resp.data;
  for (let cupcake_data of data.cupcakes) {
    let cupcake = $(gen_html(cupcake_data));
    $("#cupcake-ul").append(cupcake);
  }
}

$(showCupcakes);

/** handle form for adding of new cupcakes */

$("#create-cupcake-form").on("submit", async function (e) {
  //   console.log("CLICKED");
  e.preventDefault();
  const flavor = $("#flavor").val();
  const size = $("#size").val();
  const rating = $("#rating").val();
  const image = $("#image").val();
  //   data = {
  //     flavor: flavor,
  //     size: size,
  //     rating: rating,
  //     image: image,
  //   };
  const response = await axios.post(`${URL}/cupcakes`, {
    flavor,
    rating,
    size,
    image,
  });
  const newCupcake = $(gen_html(response.data.cupcake));
  //   console.log(newCupcake);
  //   console.log($("#cupcakes-ul"));
  $("#cupcake-ul").append(newCupcake);
  $("#new-cupcake-form").trigger("reset");
});

/** handle clicking delete: delete cupcake */

$("#cupcake-ul").on("click", "#delete-cupcake", async function (e) {
  e.preventDefault;
  let $cupcake = $(e.target).closest("li");
  let id = $cupcake.attr("data-id");
  await axios.delete(`${URL}/cupcakes/${id}`);
  $cupcake.remove();
});
