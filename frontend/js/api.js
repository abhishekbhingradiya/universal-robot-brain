const API_BASE =
    "http://127.0.0.1:8000/api/v1";

async function getData(
    endpoint
) {

    const response =
        await fetch(
            `${API_BASE}${endpoint}`
        );

    return await response.json();
}