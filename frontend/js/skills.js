async function loadTopSkills() {

    const data =
        await getData(
            "/dashboard/top-skills"
        );

    const body =
        document.getElementById(
            "skills-body"
        );

    body.innerHTML = "";

    data.skills.forEach(
        skill => {

            body.innerHTML += `
            <tr class="border-b border-slate-800">

                <td class="py-3">
                    ${skill.strategy}
                </td>

                <td class="py-3">
                    ${skill.avg_reward}
                </td>

            </tr>
            `;
        }
    );
}

async function loadTimeline() {

    const skill =
        document.getElementById(
            "skill-name"
        ).value;

    const data =
        await getData(
            `/skills/${skill}/timeline`
        );

    const body =
        document.getElementById(
            "timeline-body"
        );

    body.innerHTML = "";

    data.versions.forEach(
        item => {

            body.innerHTML += `
            <tr class="border-b border-slate-800">

                <td class="py-3">
                    ${item.version}
                </td>

                <td class="py-3">
                    ${item.fitness}
                </td>

            </tr>
            `;
        }
    );
}

async function evolveSkill() {

    const skill =
        document.getElementById(
            "evolve-skill"
        ).value;

    const fitness =
        parseFloat(
            document.getElementById(
                "evolve-fitness"
            ).value
        );

    const response =
        await fetch(
            "http://127.0.0.1:8000/api/v1/skills/evolve",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    skill_name: skill,
                    fitness: fitness
                })
            }
        );

    const result =
        await response.json();

    document.getElementById(
        "evolution-result"
    ).textContent =
        JSON.stringify(
            result,
            null,
            2
        );

    await loadTopSkills();
}

loadTopSkills();