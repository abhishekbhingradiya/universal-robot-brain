async function loadExperiences() {

    const data =
        await getData(
            "/experiences"
        );

    renderExperiences(
        data.experiences
    );

    document.getElementById(
        "experience-count"
    ).textContent =
        data.count;
}

function renderExperiences(
    experiences
) {

    const body =
        document.getElementById(
            "experience-body"
        );

    body.innerHTML = "";

    experiences.forEach(
        exp => {

            body.innerHTML += `
            <tr class="border-b border-slate-800">

                <td class="py-3">${exp.id}</td>

                <td class="py-3">
                    ${exp.robot_id}
                </td>

                <td class="py-3">
                    ${exp.task}
                </td>

                <td class="py-3">
                    ${exp.strategy}
                </td>

                <td class="py-3">
                    ${exp.reward}
                </td>

            </tr>
            `;
        }
    );
}

async function createExperience() {

    const robotId =
        document.getElementById(
            "robot-id"
        ).value;

    const task =
        document.getElementById(
            "task"
        ).value;

    const strategy =
        document.getElementById(
            "strategy"
        ).value;

    const reward =
        parseFloat(
            document.getElementById(
                "reward"
            ).value
        );

    await fetch(
        "http://127.0.0.1:8000/api/v1/experiences",
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({

                robot_id: robotId,

                task: task,

                strategy: strategy,

                reward: reward
            })
        }
    );

    await loadExperiences();
}

async function filterRobot() {

    const robotId =
        document.getElementById(
            "robot-filter"
        ).value;

    if (!robotId) {

        await loadExperiences();

        return;
    }

    const data =
        await getData(
            `/experiences/${robotId}`
        );

    renderExperiences(
        data.experiences
    );
}

loadExperiences();