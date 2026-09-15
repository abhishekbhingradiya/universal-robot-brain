async function loadGraph() {

    const data =
        await getData(
            "/network/graph"
        );

    document.getElementById(
        "node-count"
    ).textContent =
        data.nodes.length;

    document.getElementById(
        "edge-count"
    ).textContent =
        data.edges.length;

    const nodesBody =
        document.getElementById(
            "nodes-body"
        );

    const edgesBody =
        document.getElementById(
            "edges-body"
        );

    nodesBody.innerHTML = "";
    edgesBody.innerHTML = "";

    data.nodes.forEach(
        node => {

            nodesBody.innerHTML += `
            <tr class="border-b border-slate-800">

                <td class="py-3">
                    ${node.id}
                </td>

                <td class="py-3">
                    ${node.type}
                </td>

            </tr>
            `;
        }
    );

    data.edges.forEach(
        edge => {

            edgesBody.innerHTML += `
            <tr class="border-b border-slate-800">

                <td class="py-3">
                    ${edge.source}
                </td>

                <td class="py-3">
                    ${edge.target}
                </td>

                <td class="py-3">
                    ${edge.relationship}
                </td>

            </tr>
            `;
        }
    );
}

loadGraph();