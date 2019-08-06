// from data.js
var tableData = data;

// YOUR CODE HERE!

console.log(data);

// Create table of records in given webpage
var UFODATA = d3.select("tbody")
.selectAll("tr")
.data(data)
.enter()
.append("tr")
.html(function(d){
    return `<th class="table-head">${d.datetime}</th>
    <th class="table-head">${d.city}</th>
    <th class="table-head">${d.state}</th>
    <th class="table-head">${d.country}</th>
    <th class="table-head">${d.shape}</th>
    <th class="table-head">${d.durationMinutes}</th>
    <th class="table-head">${d.comments}</th>`
});


// Filter table by date
var submit = d3.select("#filter-btn");
var input = d3.select("#datetime");    
var tbody = d3.select("tbody");


submit.on("click", handleclick) 

function handleclick() {
    
    var inputValue = input.property("value");

    d3.event.preventDefault();

    var filteredData = tableData.filter(sighting => sighting.datetime === inputValue);

        d3.selectAll("tbody tr").remove();
        d3.selectAll("tbody td").remove();
        
        filteredData.forEach((sightingEvents) => {
    
        var row = tbody.append("tr");

        Object.entries(sightingEvents).forEach(function([key, value]) {

            var cell = tbody.append("td");
            cell.text(value);
        })
        
    })
  
};


