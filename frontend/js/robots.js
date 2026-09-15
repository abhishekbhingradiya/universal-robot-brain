async function loadRobots() {

    const data =
        await getData(
            "/robots"
        );

    document.getElementById(
        "robot-count"
    ).textContent =
        data.count;

    const body =
        document.getElementById(
            "robots-body"
        );

    body.innerHTML = "";

    data.robots.forEach(
        robot => {

            body.innerHTML += `
            <tr class="border-b border-slate-800">

                <td class="py-3">
                    ${robot.id}
                </td>

                <td class="py-3">
                    ${robot.robot_id}
                </td>

                <td class="py-3">
                    ${robot.robot_type}
                </td>

                <td class="py-3">
                    ${robot.status}
                </td>

            </tr>
            `;
        }
    );
}

async function createRobot() {

    const robotId =
        document.getElementById(
            "robot-id"
        ).value;

    const robotType =
        document.getElementById(
            "robot-type"
        ).value;

    await fetch(
        "http://127.0.0.1:8000/api/v1/robots",
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({
                robot_id: robotId,
                robot_type: robotType
            })
        }
    );

    document.getElementById(
        "robot-id"
    ).value = "";

    document.getElementById(
        "robot-type"
    ).value = "";

    await loadRobots();
}

loadRobots();