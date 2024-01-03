function changeStatusPreparando(id) {
    var url = `http://127.0.0.1:8000/api/orders/${id}/`;
    var data = { "status": "Preparando" };
    fetch(url, {
        method: 'PATCH',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json; charset=UTF-8'
        },
    })
        .then(response => response.json())
        .then(json => console.log(json))
    location.reload();
}

function changeStatusListo(id) {
    var url = `http://127.0.0.1:8000/api/orders/${id}/`;
    var data = { "status": "Listo" };
    fetch(url, {
        method: 'PATCH',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json; charset=UTF-8'
        },
    })
        .then(response => response.json())
        .then(json => console.log(json))
    location.reload();
}

function changeStatusEntregado(id) {
    var url = `http://127.0.0.1:8000/api/orders/${id}/`;
    var data = { "status": "Entregado" };
    fetch(url, {
        method: 'PATCH',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json; charset=UTF-8'
        },
    })
        .then(response => response.json())
        .then(json => console.log(json))
    location.reload();
}