let chart = null;

async function loadDashboard(type){

    document
        .getElementById("loader")
        .classList.remove("hidden");

    document
        .getElementById("dashboardContent")
        .classList.add("hidden");

    try{

        const data = await getDashboard(type);

        renderSummary(data.summary);

        renderChart(data);

        renderTable(data.recent_requests);

        document
            .getElementById("dashboardContent")
            .classList.remove("hidden");

    }

    catch(err){

        alert(err.message);

    }

    finally{

        document
            .getElementById("loader")
            .classList.add("hidden");

    }

}


function renderSummary(summary){

    const container =
        document.getElementById("summaryCards");

    container.innerHTML = "";

    Object.entries(summary).forEach(([key,value])=>{

        container.innerHTML += `

            <div class="summary-card">

                <h3>${formatTitle(key)}</h3>

                <p>${value}</p>

            </div>

        `;

    });

}


function renderChart(data){

    const ctx =
        document
        .getElementById("dashboardChart")
        .getContext("2d");

    if(chart)
        chart.destroy();

    let labels = [];
    let values = [];

    if(data.by_team){

        labels = data.by_team.map(x=>x.team);
        values = data.by_team.map(x=>x.count);

    }

    else if(data.by_service){

        labels = data.by_service.map(x=>x.service_type);
        values = data.by_service.map(x=>x.count);

    }

    else if(data.by_status){

        labels = data.by_status.map(x=>x.status);
        values = data.by_status.map(x=>x.count);

    }

    chart = new Chart(ctx,{

        type:"pie",

        data:{

            labels,

            datasets:[{

                data:values

            }]

        }

    });

}


function renderTable(requests){

    const tbody =
        document
        .querySelector("#requestTable tbody");

    tbody.innerHTML = "";

    requests.forEach(r=>{

        tbody.innerHTML += `

        <tr>

            <td>${r.id}</td>

            <td>${r.request}</td>

            <td>${r.status}</td>

            <td>${r.assigned_team ?? "-"}</td>

            <td>${new Date(r.created_at).toLocaleString()}</td>

        </tr>

        `;

    });

}


function formatTitle(str){

    return str

        .replaceAll("_"," ")

        .replace(/\b\w/g,c=>c.toUpperCase());

}