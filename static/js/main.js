const loadTables = async () => {
    try {
        const responseTables = await fetch("http://127.0.0.1:8000/api/tables/", {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json; charset=UTF-8'
            },
        });
        const tables = await responseTables.json();

        const responseOrders = await fetch("http://127.0.0.1:8000/api/orders/", {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json; charset=UTF-8'
            },
        })
        const orders = await responseOrders.json();

        const responseProducts = await fetch("http://127.0.0.1:8000/api/foods/", {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json; charset=UTF-8'
            },
        })
        const products = await responseProducts.json();

        const responseUsers = await fetch("http://127.0.0.1:8000/api/users/", {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json; charset=UTF-8'
            },
        })
        const users = await responseUsers.json();

        for (let i = 0; i < tables.length; i++) {
            for (let j = 0; j < orders.length; j++) {
                if (tables[i].order == orders[j].id) {
                    tables[i].order = orders[j];
                    for (let k = 0; k < products.length; k++) {
                        if (orders[j].dish == products[k].id) {
                            tables[i].order.dish = products[k].name;
                        }
                    }
                    for (let k = 0; k < users.length; k++) {
                        if (orders[j].user == users[k].id) {
                            tables[i].order.user = {
                                "name": users[k].username,
                                "phone": users[k].phone,
                            };
                        }
                    }
                }
            }
        }

        let tableData = ""; // Mover la declaración fuera del bucle

        tables.forEach(elements => {
            tableData += `
            <tr>
                <td class="container-order">
                    Nombre del plato: ${elements.order.dish} <br>
                    Cantidad: ${elements.order.quantity} <br>
                    Usuario: ${elements.order.user.name} <br>
                    Celular de usuario: ${elements.order.user.phone} <br>
                </td>
                <td class="container-number-order">
                    Numero de orden: ${elements.order.BillHeader}
                </td>
                <td class="container-status-order">
                    Estado: ${elements.order.status}
                </td>
            </tr>
            `;
        });

        let tarjet = document.getElementById("tarjet-complement");
        tarjet.innerHTML = tableData;
    } catch (error) {
        console.error("Error:", error);
    }
};

const initialLoad = async () => {
    await loadTables();
};

window.addEventListener("load", async () => {
    await initialLoad();

    // Recargar la página cada minuto
    setInterval(() => {
        location.reload();
    }, 30000);
});