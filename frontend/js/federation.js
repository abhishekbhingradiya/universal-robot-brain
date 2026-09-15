async function loadNodes() {

    const data =
        await getData(
            "/federation/nodes"
        );

    const body =
        document.getElementById(
            "nodes-body"
        );

    body.innerHTML = "";

    data.nodes.forEach(
        node => {

            body.innerHTML += `
            <tr>

                <td>${node.id}</td>

                <td>${node.node_id}</td>

                <td>${node.region}</td>

                <td>${node.status}</td>

            </tr>
            `;
        }
    );
}

async function createNode() {

    const nodeId =
        document.getElementById(
            "node-id"
        ).value;

    const region =
        document.getElementById(
            "region"
        ).value;

    await fetch(
        "http://127.0.0.1:8000/api/v1/federation/nodes",
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({

                node_id: nodeId,

                region: region
            })
        }
    );

    await loadNodes();
}

loadNodes();