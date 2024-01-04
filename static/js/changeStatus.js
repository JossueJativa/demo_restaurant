function changeOrderStatus(id, newStatus) {
    const url = `http://127.0.0.1:8080/api/orders/${id}/`;
    const data = { "status": newStatus };

    fetch(url, {
        method: 'PATCH',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json; charset=UTF-8'
        },
    })
    .then(response => response.json())
    .then(json => console.log(json))
    .finally(() => location.reload());
}

function changeStatusPreparando(id) {
    changeOrderStatus(id, "Preparando");
}

function changeStatusListo(id) {
    changeOrderStatus(id, "Listo");
}

function changeStatusEntregado(id) {
    changeOrderStatus(id, "Entregado");
}
