/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 100.0, "KoPercent": 0.0};
    var dataset = [
        {
            "label" : "KO",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "OK",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.7166666666666667, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/users-3"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/users-4"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/users-1"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/users-2"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/users"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/users-0"], "isController": false}, {"data": [0.37, 500, 1500, "http:\/\/localhost:3000\/api\/v1\/users\/5e8643edd411aa54c0357fbd"], "isController": false}, {"data": [0.0, 500, 1500, "Users"], "isController": true}, {"data": [0.08, 500, 1500, "http:\/\/localhost:3000\/api\/v1\/users\/login"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 400, 0, 0.0, 438.7374999999999, 3, 3373, 32.5, 1655.000000000001, 2042.8999999999996, 2384.120000000001, 2.3376092101802883, 3323.6896490481545, 0.8623358194781287], "isController": false}, "titles": ["Label", "#Samples", "KO", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions\/s", "Received", "Sent"], "items": [{"data": ["http:\/\/localhost:3001\/users-3", 50, 0, 0.0, 41.25999999999999, 36, 50, 42.0, 45.9, 48.449999999999996, 50.0, 0.2978743685063388, 1243.3628121909553, 0.06545091104875608], "isController": false}, {"data": ["http:\/\/localhost:3001\/users-4", 50, 0, 0.0, 18.899999999999988, 13, 29, 19.0, 24.9, 26.89999999999999, 29.0, 0.2979205148066496, 357.176148762885, 0.06633386462491807], "isController": false}, {"data": ["http:\/\/localhost:3001\/users-1", 50, 0, 0.0, 14.8, 13, 17, 14.0, 17.0, 17.0, 17.0, 0.2979187396845636, 1.005184810166179, 0.06284223415221264], "isController": false}, {"data": ["http:\/\/localhost:3001\/users-2", 50, 0, 0.0, 11.079999999999998, 4, 21, 12.5, 15.899999999999999, 16.449999999999996, 21.0, 0.2979187396845636, 9.366111315102692, 0.0651697243059983], "isController": false}, {"data": ["http:\/\/localhost:3001\/users", 50, 0, 0.0, 47.04, 41, 89, 46.0, 50.9, 54.449999999999996, 89.0, 0.29780162837930396, 1611.0559156990596, 0.32077655869372296], "isController": false}, {"data": ["http:\/\/localhost:3001\/users-0", 50, 0, 0.0, 3.8799999999999994, 3, 6, 4.0, 4.899999999999999, 5.0, 6.0, 0.2978743685063388, 0.5960396299506721, 0.061087516978839004], "isController": false}, {"data": ["http:\/\/localhost:3000\/api\/v1\/users\/5e8643edd411aa54c0357fbd", 50, 0, 0.0, 1501.84, 1341, 3373, 1430.5, 1608.5, 2122.649999999998, 3373.0, 0.29509144883999555, 82.97645903356076, 0.12823798313847462], "isController": false}, {"data": ["Users", 50, 0, 0.0, 3419.98, 2879, 5464, 3461.0, 3785.6, 4030.4499999999994, 5464.0, 0.292107261786528, 1742.3713221870073, 0.5474158548519017], "isController": true}, {"data": ["http:\/\/localhost:3000\/api\/v1\/users\/login", 50, 0, 0.0, 1871.1000000000001, 1467, 2543, 1982.5, 2152.8, 2355.0499999999993, 2543.0, 0.29464974984236236, 80.679791732349, 0.10675298553859026], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": []}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 400, 0, null, null, null, null, null, null, null, null, null, null], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
